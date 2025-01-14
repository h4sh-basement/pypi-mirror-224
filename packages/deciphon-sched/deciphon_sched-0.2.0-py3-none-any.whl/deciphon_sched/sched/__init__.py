from fastapi import APIRouter, Request
from starlette.status import HTTP_200_OK

from . import dbs, hmms, jobs, scans

# from deciphon_api.api import dbs, hmms, jobs, scans, wipe
# from deciphon_api.responses import PrettyJSONResponse

router = APIRouter()

router.include_router(hmms.router)
router.include_router(dbs.router)
router.include_router(jobs.router)
# router.include_router(jobs.router)
router.include_router(scans.router)


@router.get("/", summary="list of all endpoints", status_code=HTTP_200_OK)
def root(request: Request):
    routes = request.app.routes
    return [{"path": route.path, "name": route.name} for route in routes]
