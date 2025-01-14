"""
Main interface for redshift-serverless service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_redshift_serverless import (
        Client,
        ListEndpointAccessPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListSnapshotsPaginator,
        ListTableRestoreStatusPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
        RedshiftServerlessClient,
    )

    session = get_session()
    async with session.create_client("redshift-serverless") as client:
        client: RedshiftServerlessClient
        ...


    list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_table_restore_status_paginator: ListTableRestoreStatusPaginator = client.get_paginator("list_table_restore_status")
    list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
    list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""
from .client import RedshiftServerlessClient
from .paginator import (
    ListEndpointAccessPaginator,
    ListNamespacesPaginator,
    ListRecoveryPointsPaginator,
    ListSnapshotsPaginator,
    ListTableRestoreStatusPaginator,
    ListUsageLimitsPaginator,
    ListWorkgroupsPaginator,
)

Client = RedshiftServerlessClient


__all__ = (
    "Client",
    "ListEndpointAccessPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListSnapshotsPaginator",
    "ListTableRestoreStatusPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
    "RedshiftServerlessClient",
)
