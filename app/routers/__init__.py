from .v1 import setup_routers as setup_v1_routers


def setup_routers(app):
    setup_v1_routers(app)
