"""
Type annotations for m2 service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_m2.client import MainframeModernizationClient
    from types_aiobotocore_m2.paginator import (
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
        ListBatchJobDefinitionsPaginator,
        ListBatchJobExecutionsPaginator,
        ListDataSetImportHistoryPaginator,
        ListDataSetsPaginator,
        ListDeploymentsPaginator,
        ListEngineVersionsPaginator,
        ListEnvironmentsPaginator,
    )

    session = get_session()
    with session.create_client("m2") as client:
        client: MainframeModernizationClient

        list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
        list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
        list_batch_job_definitions_paginator: ListBatchJobDefinitionsPaginator = client.get_paginator("list_batch_job_definitions")
        list_batch_job_executions_paginator: ListBatchJobExecutionsPaginator = client.get_paginator("list_batch_job_executions")
        list_data_set_import_history_paginator: ListDataSetImportHistoryPaginator = client.get_paginator("list_data_set_import_history")
        list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
        list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
        list_engine_versions_paginator: ListEngineVersionsPaginator = client.get_paginator("list_engine_versions")
        list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import BatchJobExecutionStatusType, EngineTypeType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListBatchJobDefinitionsResponseTypeDef,
    ListBatchJobExecutionsResponseTypeDef,
    ListDataSetImportHistoryResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEngineVersionsResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
    "ListBatchJobDefinitionsPaginator",
    "ListBatchJobExecutionsPaginator",
    "ListDataSetImportHistoryPaginator",
    "ListDataSetsPaginator",
    "ListDeploymentsPaginator",
    "ListEngineVersionsPaginator",
    "ListEnvironmentsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListApplicationVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListApplicationVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listapplicationversionspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListApplicationVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listapplicationversionspaginator)
        """

class ListApplicationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListApplications)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        environmentId: str = ...,
        names: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListApplications.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listapplicationspaginator)
        """

class ListBatchJobDefinitionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobDefinitions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listbatchjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        prefix: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBatchJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobDefinitions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listbatchjobdefinitionspaginator)
        """

class ListBatchJobExecutionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobExecutions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listbatchjobexecutionspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        executionIds: Sequence[str] = ...,
        jobName: str = ...,
        startedAfter: TimestampTypeDef = ...,
        startedBefore: TimestampTypeDef = ...,
        status: BatchJobExecutionStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListBatchJobExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobExecutions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listbatchjobexecutionspaginator)
        """

class ListDataSetImportHistoryPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDataSetImportHistory)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdatasetimporthistorypaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDataSetImportHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDataSetImportHistory.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdatasetimporthistorypaginator)
        """

class ListDataSetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDataSets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdatasetspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        prefix: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDataSets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdatasetspaginator)
        """

class ListDeploymentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDeployments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdeploymentspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListDeployments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listdeploymentspaginator)
        """

class ListEngineVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListEngineVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listengineversionspaginator)
    """

    def paginate(
        self, *, engineType: EngineTypeType = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListEngineVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listengineversionspaginator)
        """

class ListEnvironmentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListEnvironments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        engineType: EngineTypeType = ...,
        names: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html#MainframeModernization.Paginator.ListEnvironments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_m2/paginators/#listenvironmentspaginator)
        """
