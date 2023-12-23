from fastapi import APIRouter
from .test import router as test


def setup_routers(app):
    router = APIRouter(prefix='v1')
    router.include_router(test)
    app.include_router(router)
