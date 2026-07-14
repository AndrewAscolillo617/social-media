from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler,
)
from app.api.routes.health import router as health_router
from app.core.logging import setup_logging
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

from app.core.config import settings


# Initialize logging before the app starts
setup_logging()
logger = logging.getLogger("app")

app = FastAPI()

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"[{request.state.request_id}] Incoming request: {request.method} {request.url}")

    response = await call_next(request)
    logger.info(f"[{request.state.request_id}] Completed request: {request.method} {request.url} - {response.status_code}")
    return response


app.include_router(health_router)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip
if settings.ENABLE_GZIP:
    app.add_middleware(GZipMiddleware, minimum_size=500)

# Request ID
app.add_middleware(RequestIDMiddleware)

# Trusted Hosts
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.TRUSTED_HOSTS)


