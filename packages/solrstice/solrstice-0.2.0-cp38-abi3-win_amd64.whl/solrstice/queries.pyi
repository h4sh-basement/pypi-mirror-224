from enum import Enum
from typing import TYPE_CHECKING, Dict, List, Optional

if TYPE_CHECKING:
    from solrstice.def_type import DefType
    from solrstice.group import GroupingComponent
    from solrstice.hosts import SolrServerContext
    from solrstice.response import SolrResponse

class SelectQueryBuilder:
    """Builder for a select query

    :param q: The query string
    :param fq: The filter queries
    :param fl: The fields to return
    :param sort: The sort order
    :param rows: The number of rows to return
    :param start: Set the start index
    :param cursor_mark: Set the cursor mark
    :param grouping: Set the grouping component
    :param def_type: Set the query type
    """

    def __init__(
        self,
        q: Optional[str] = None,
        fq: Optional[List[str]] = None,
        fl: Optional[List[str]] = None,
        sort: Optional[List[str]] = None,
        rows: Optional[int] = None,
        start: Optional[int] = None,
        cursor_mark: Optional[str] = None,
        grouping: Optional["GroupingComponent"] = None,
        def_type: Optional["DefType"] = None,
    ) -> None:
        pass
    q: str
    fq: Optional[List[str]]
    fl: Optional[List[str]]
    sort: Optional[List[str]]
    rows: int
    start: int
    cursor_mark: str
    grouping: Optional["GroupingComponent"]
    def_type: Optional["DefType"]

    async def execute(
        self, context: "SolrServerContext", collection: str
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to query
        """
    def execute_blocking(
        self, context: "SolrServerContext", collection: str
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to query
        """

class CommitType(Enum):
    Hard = ("Hard",)
    Soft = "Soft"

class UpdateQueryBuilder:
    """Builder for an update query

    :param handler: The handler for the update query
    :param commit_type: The commit type for the update query
    """

    def __init__(
        self,
        handler: Optional[str] = "update",
        commit_type: Optional[CommitType] = CommitType.Hard,
    ) -> None:
        pass
    handler: str
    commit_type: CommitType

    async def execute(
        self, context: "SolrServerContext", collection: str, data: List[Dict]
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to update
        :param data: The data to update
        """
    def execute_blocking(
        self, context: "SolrServerContext", collection: str, data: List[Dict]
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to update
        :param data: The data to update
        """

class DeleteQueryBuilder:
    """Builder for a delete query

    :param handler: The handler for the delete query
    :param commit_type: The commit type for the delete query
    """

    def __init__(
        self,
        handler: Optional[str] = "update",
        commit_type: Optional[CommitType] = CommitType.Hard,
        ids: Optional[List[str]] = None,
        queries: Optional[List[str]] = None,
    ) -> None:
        pass
    handler: str
    commit_type: CommitType
    ids: List[str]
    queries: List[str]

    async def execute(
        self, context: "SolrServerContext", collection: str
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to delete from
        """
    def execute_blocking(
        self, context: "SolrServerContext", collection: str
    ) -> "SolrResponse":
        """Execute the query

        :param context: The context for the connection to the solr instance
        :param collection: The collection to delete from
        """
