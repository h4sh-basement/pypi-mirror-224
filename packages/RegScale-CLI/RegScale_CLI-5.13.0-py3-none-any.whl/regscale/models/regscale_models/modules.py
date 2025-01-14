#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Class of all RegScale modules """

# standard python imports
from dataclasses import asdict, dataclass

from rich.console import Console
from rich.table import Table

from regscale.core.app.utils.app_utils import uncamel_case


@dataclass
class Modules:
    """Class for all RegScale Modules"""

    assessment: str = "assessments"
    asset: str = "assets"
    case: str = "cases"
    catalogue: str = "catalogues"
    causalAnalysis: str = "causalanalysis"
    component: str = "components"
    dataCall: str = "datacalls"
    exception: str = "exceptions"
    incident: str = "incidents"
    interconnect: str = "interconnects"
    # using _ to replace with ( and will later put POAM in parentheses
    issue_POAM: str = "issues"
    policy: str = "policies"
    project: str = "projects"
    questionnaire: str = "questionnaires"
    requirement: str = "requirements"
    risk: str = "risks"
    securityControl: str = "securitycontrols"
    securityControlImplementation: str = "controls"
    securityPlan: str = "securityplans"
    securityProfile: str = "profiles"
    # using _ to replace with ( and will later put Contract in parentheses
    supplyChain_Contract: str = "supplychain"
    task: str = "tasks"
    threat: str = "threats"

    def __getitem__(self, key: any) -> any:
        """
        Get attribute from Pipeline
        :param any key:
        :return: value of provided key
        :rtype: any
        """
        return getattr(self, key)

    def __setitem__(self, key: any, value: any) -> None:
        """
        Set attribute in Pipeline with provided key
        :param any key: Key to change to provided value
        :param any value: New value for provided Key
        :return: None
        """
        return setattr(self, key, value)

    def dict(self) -> dict:
        """
        Create a dictionary from the Asset dataclass
        :return: Dictionary of Asset
        :rtype: dict
        """
        return dict(asdict(self).items())

    def module_names(self) -> list:
        """
        Function to clean the keys and display them as they are in the application
        :return: list of module names
        :rtype: list
        """
        # create list variable for the cleaned up keys
        clean_keys = []

        # convert the class to a dictionary
        data = self.dict()

        # iterate through the keys
        for key in data.keys():
            # see if there is an _ in the key name, so we can replace it with ()
            if "_" in key:
                # find location of _
                index = key.find("_")

                # use the location to concatenate the key and () value
                clean_key = f"{uncamel_case(key[:index])}({key[index+1:]})"
            else:
                # uncamel case the key and append
                clean_key = uncamel_case(key)
            # append the clean key to the list
            clean_keys.append(clean_key)
        # return the list of clean keys
        return clean_keys

    def api_names(self) -> list:
        """
        Function to get the values from the class, used for RegScale API calls
        :return: List of modules used for RegScale API calls
        :rtype: list
        """
        # convert the class to dictionary
        modules = self.dict()

        # return the values from the dictionary as a list
        return list(modules.values())

    def to_table(self) -> None:
        """
        Displays the customer facing RegScale modules and the API equivalent as a table in the console
        :return: None
        """
        # create console and table objects
        console = Console()
        table = Table(
            "RegScale Module", "Accepted Value", title="RegScale Modules", safe_box=True
        )

        # get list for clean columns and the api names
        columns = self.module_names()
        data = self.api_names()

        # iterate through items and add them to table object
        for i in range(len(columns)):
            table.add_row(columns[i], data[i])

        # print the table object in console
        console.print(table)

    def to_str_table(self) -> str:
        """
        Creates a string table of the data to display in console for click help command
        :return: string table of customer facing RegScale modules and the API equivalent
        :rtype: str
        """
        # create string to store the table
        output = "{:<25} {:<25}\n".format("RegScale Module", "Accepted Value")

        # get list for clean columns and the api names
        columns = self.module_names()
        data = self.api_names()

        # iterate through items and add it to the output string
        for i in range(len(columns)):
            output += "\b{:<25} | {:<25}\n".format(columns[i], data[i])

        # return the string
        return output
