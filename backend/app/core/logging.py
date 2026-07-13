import logging
import logging.config
from typing import Any, Dict


def get_logging_config() -> Dict[str, Any]:
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            },
            "access": {
                "format": "%(asctime)s - %(levelname)s - %(client_addr)s - %(request_line)s - %(status_code)s",
            },
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "access": {
                "class": "logging.StreamHandler",
                "formatter": "access",
            },
        },
        "loggers": {
            "uvicorn.error": {
                "level": "INFO",
            },
            "uvicorn.access": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            },
            "app": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }


def setup_logging() -> None:
    logging.config.dictConfig(get_logging_config())
