import time

from app.log import logger
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


def setup_exceptions(app):
    # 捕获所有的 HTTP 异常
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error(f'HTTP error occurred: {exc.detail}')
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "code": exc.status_code,
                "msg": f"HTTP error occurred: {exc.detail}",
            }
        )

    # 捕获请求验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        err = exc.errors()
        logger.error(f"Validation error,details: {err}")
        return JSONResponse(
            status_code=422,
            content={"code": 422, "msg": f"Validation error,details: {err}"},
        )

    # 捕获其他异常
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"Validation error,details: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"code": 500, "msg": f"An error occurred: {str(exc)}"},
        )
    
    # 添加每个请求的时间统计
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"Request: {request.url} completed in {process_time} seconds")
        return response