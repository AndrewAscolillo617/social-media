from fastapi import FastAPI, Request
from app.api.routes.health import router as health_router
from app.core.logging import setup_logging
import logging

# Initialize logging before the app starts
setup_logging()
logger = logging.getLogger("app")

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Completed request: {request.method} {request.url} - {response.status_code}")
    return response


app.include_router(health_router)

