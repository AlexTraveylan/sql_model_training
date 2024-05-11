"""
Main module for the application
"""

import logging

from app.core.constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


def main():
    """Entry point for the application."""

    logger.info("Application started.")


if __name__ == "__main__":
    main()
