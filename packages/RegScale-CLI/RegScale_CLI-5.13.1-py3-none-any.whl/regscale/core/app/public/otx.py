#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AlienVault OTX RegScale integration"""


from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.models.regscale_models import Threat
from datetime import date, datetime
import re
import click
import dataclasses
import threading
import time

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

#####################################################################################################
#
# AlienVault API Documentation: https://otx.alienvault.com/api/
#
#####################################################################################################

logger = create_logger()
SERVER = "https://otx.alienvault.com"
API_V1_ROOT = f"{SERVER}/api/v1"
SUBSCRIBED = f"{API_V1_ROOT}/pulses/subscribed"


@click.group()
def alienvault():
    """[BETA] AlienVault OTX Integration to load pulses to RegScale."""


@alienvault.command(name="ingest_pulses")
@click.option(
    "--modified_since",
    type=click.DateTime(),
    required=False,
    help="Enter a local datetime to pull all pulses identified after.",
)
@click.option(
    "--limit",
    type=click.IntRange(min=1, max=50, clamp=True),
    required=False,
    default=50,
    help="Items per request.",
)
def ingest_pulses(modified_since: click.DateTime, limit: click.INT):
    """
    [BETA] Sync RegScale threats with pulse data from AlienVault OTX.
    """
    pulses(modified_since, limit)


def create_url(url_path, **kwargs):
    """
    Turn a path into a valid fully formatted URL. Supports query parameter formatting as well.
    :param url_path: Request path (i.e. "/search/pulses")
    :param kwargs: key value pairs to be added as query parameters (i.e. limit=10, page=5)
    :return: a formatted url (i.e. "/search/pulses")
    """
    uri = url_path.format(SERVER)
    uri = uri if uri.startswith("http") else SERVER.rstrip("/") + uri
    if kwargs:
        uri += f"?{urlencode(kwargs)}"

    return uri


def walkapi_iter(
    app,
    api,
    url,
    args,
):
    """
    Walk OTX API and return results
    :param app: Application instance
    :param api: Api instance
    :param url: OTX URL
    :yield: A dictionary representing an AlienVault OTX threat.
    """
    next_page_url = create_url(url, **args)
    item_count = 0
    api = Api(app)
    api.timeout = 30
    headers = {"X-OTX-API-KEY": app.config["otx"]}
    while next_page_url:
        data = []
        try:
            response = api.get(url=next_page_url, headers=headers)
            if response.json() == {"detail": "Authentication required"}:
                raise ValueError(
                    "Unable to log into AlienVault, please check your API key"
                )

            if response.ok:
                data = response.json()
                count = data["count"]
                for el in data["results"]:
                    item_count += 1
                    if item_count % 100 == 0:
                        logger.info("Processing %i of %i", item_count, count)
                    yield el
        except UnboundLocalError as ex:
            logger.warning("Unable to Pull from API, trying again..\n%s", ex)
            time.sleep(2)
            continue

        next_page_url = data["next"]


def extract_id(descrip: str) -> str:
    """Match RegEx of Alienvault ID

    :param descrip: A string with the AlienVault ID
    :return: A string from the regex match
    :rtype: str
    """
    pattern = r"(?<=AlienVault ID: ).*"
    return match[0] if (match := re.search(pattern, descrip)) else ""


def post_threat(app: Application, api: Api, threat: Threat):
    """
    Post Alienvault Threat to RegScale.
    :param app: Application instance
    :param app: Api instance
    :param threat: RegScale threat object
    """
    response = api.post(
        url=app.config["domain"] + "/api/threats", json=dataclasses.asdict(threat)
    )
    if response.ok:
        logger.info("Successfully posted threat: %s", threat.title)
    else:
        logger.warning("Unable to post threat: %s", threat.title)


def pulses(modified_since, limit):
    """
    Process pulses
    :param modified_since: Local Datetime (Converted to ISO_format before GET), defaults to None
    :param limit: Result limit, defaults to 50

    """
    app = Application()
    api = Api(app)
    args = {"limit": limit}
    existing_threats = []
    response = api.get(app.config["domain"] + "/api/threats/getAll")
    if not response.raise_for_status():
        existing_threats = response.json()
    today = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%SZ")
    if modified_since is not None:
        if isinstance(modified_since, (datetime, date)):
            modified_since = modified_since.isoformat()
        args["modified_since"] = modified_since

    for result in walkapi_iter(app=app, api=api, url=SUBSCRIBED, args=args):
        references = (
            result["references"]
            if "references" in result and result["references"]
            else ""
        )
        threat = Threat(
            title=result["name"],
            targetType="Other",
            vulnerabilityAnalysis="",
            mitigations="",
            notes=", ".join(result["tags"])
            + f" \n{references}"
            + f" \nAlienVault ID: {result['id']}",
            threatType="Specific",
            source="Open Source",
            threatOwnerId=app.config["userId"],
            status="Under Investigation",
            dateIdentified=result["created"],
            dateCreated=today,
            description=f"{result['description']}\n{SERVER}/pulse/{result['id']}",
        )
        logger.debug(threat.notes)
        alienvault_ids = {
            extract_id(thr["notes"])
            for thr in existing_threats
            if "notes" in thr and len(extract_id(thr["notes"])) > 0
        }
        if result["id"] not in alienvault_ids:
            thread = threading.Thread(target=post_threat, args=(app, api, threat))
            thread.start()
