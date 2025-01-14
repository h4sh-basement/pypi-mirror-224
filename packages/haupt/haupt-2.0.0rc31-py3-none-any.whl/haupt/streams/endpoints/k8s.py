from typing import Dict, Optional, Union

from django.core.handlers.asgi import ASGIRequest
from django.db import transaction
from django.http import HttpResponse
from django.urls import path

from haupt.common.endpoints.files import FilePathResponse
from haupt.common.endpoints.validation import validate_methods
from haupt.streams.connections.fs import AppFS
from haupt.streams.controllers.k8s_crd import get_k8s_operation
from haupt.streams.controllers.k8s_op_spec import get_op_spec
from haupt.streams.endpoints.base import UJSONResponse
from haupt.streams.tasks.op_spec import download_op_spec
from polyaxon import settings
from polyaxon.k8s.manager.async_manager import AsyncK8sManager
from polyaxon.lifecycle import LifeCycle
from polyaxon.utils.fqn_utils import get_resource_name_for_kind


@transaction.non_atomic_requests
async def k8s_inspect(
    request: ASGIRequest,
    namespace: str,
    owner: str,
    project: str,
    run_uuid: str,
    methods: Optional[Dict] = None,
) -> Union[HttpResponse, FilePathResponse]:
    validate_methods(request, methods)
    resource_name = get_resource_name_for_kind(run_uuid=run_uuid)
    connection = request.GET.get("connection")
    status = request.GET.get("status")
    if LifeCycle.is_done(status):
        spec_path = await download_op_spec(
            fs=await AppFS.get_fs(connection=connection),
            store_path=AppFS.get_fs_root_path(connection=connection),
            run_uuid=run_uuid,
        )
        if spec_path:
            return FilePathResponse(filepath=spec_path)

    k8s_manager = AsyncK8sManager(
        namespace=namespace,
        in_cluster=settings.CLIENT_CONFIG.in_cluster,
    )
    await k8s_manager.setup()
    k8s_operation = await get_k8s_operation(
        k8s_manager=k8s_manager, resource_name=resource_name
    )
    data = None
    if k8s_operation:
        run_kind = k8s_operation["metadata"]["annotations"][
            "operation.polyaxon.com/kind"
        ]
        data = await get_op_spec(
            k8s_manager=k8s_manager, run_uuid=run_uuid, run_kind=run_kind
        )
    if k8s_manager:
        await k8s_manager.close()
    return UJSONResponse(data or {})


URLS_RUNS_K8S_INSPECT = (
    "<str:namespace>/<str:owner>/<str:project>/runs/<str:run_uuid>/k8s_inspect"
)

# fmt: off
k8s_routes = [
    path(
        URLS_RUNS_K8S_INSPECT,
        k8s_inspect,
        name="k8s_inspect",
        kwargs=dict(methods=["GET"]),
    ),
]
