"""Provide SQL Queries to be used in Airflow DAGs related to SQL Server."""
from typing import List

from regscale.utils.string import (
    replace_unknown_spaces_and_newlines,
    extract_double_curly_braces_contents,
    extract_dag_run_conf_key,
    extract_param,
)
from regscale.utils.lists import add_and_return_unique


class SQLQuery:
    def __init__(self, query: str = "", **kwargs):
        """Initialize a SQLQuery Class.
        :param str query: a SQL query
        :param kwargs: additional keyword arguments
        """
        self.raw = query
        self.query = replace_unknown_spaces_and_newlines(query)
        self.kwargs = kwargs
        self.vars: List[str] = []
        self.dag_run_vars: List[str] = []
        self.params: List[str] = []
        self._populate_jinja_vars(**kwargs)

    def __repr__(self):
        """Return the SQLQuery object."""
        return f"SQLQuery(query={self.query}, kwargs={self.kwargs})"

    def __str__(self):
        """Return the SQLQuery object."""
        return f"{self.dag_run_vars=}\n{self.params=}\n{self.unique_vars=}"

    def _populate_jinja_vars(self, **kwargs):
        """Populate the SQLQuery object with Jinja variables.
        :param kwargs: keyword arguments
        """
        self.vars = extract_double_curly_braces_contents(self.query)
        self.dag_run_vars = [extract_dag_run_conf_key(__) for __ in self.vars]
        self.params = [extract_param(_) for _ in self.vars]

    @property
    def unique_vars(self) -> List[str]:
        """Return a list of unique Jinja variables."""
        return list(set(self.dag_run_vars + self.params))
