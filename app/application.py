from fastapi import FastAPI

from app.routers import setup_routers
from app.exceptions import setup_exceptions


def create_application():
    app = FastAPI(
        title='basic_svc'
    )
    # setup_routers(app)
    setup_exceptions(app)
    return app


if __name__ == '__main__':
    app = create_application()
