import logging
import sys
from pathlib import Path

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        try:
            logger.bind(name=record.name).opt(
                depth=depth, exception=record.exc_info
            ).log(level, record.getMessage())
        except Exception:
            self.handleError(record)


def setup_logging(base_dir: Path, *, debug: bool = False):
    logs_dir = base_dir / "logs"
    logs_dir.mkdir(exist_ok=True)

    console_level = "DEBUG" if debug else "INFO"

    logger.remove()

    logger.add(
        sys.stderr,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{extra[name]}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level=console_level,
    )

    file_sink_kwargs = {
        "rotation": "10 MB",
        "retention": "10 days",
        "compression": "zip",
        "encoding": "utf-8",
        "enqueue": True,
    }

    logger.add(
        logs_dir / "django.log",
        format=(
            "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | "
            "{extra[name]}:{function}:{line} - {message}"
        ),
        level="INFO",
        **file_sink_kwargs,
    )

    logger.add(
        logs_dir / "errors.log",
        format=(
            "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | "
            "{extra[name]}:{function}:{line} - {message}"
        ),
        level="ERROR",
        **file_sink_kwargs,
    )

    logger.configure(extra={"name": "loguru"})
