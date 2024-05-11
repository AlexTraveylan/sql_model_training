"""
Main module for the application
"""

import logging

from app.adapter.exception.app_exception import AppException
from app.core.constants import LOGGER_NAME
from app.core.controller import PersonageController
from app.core.models import Personage, unit

logger = logging.getLogger(LOGGER_NAME)


def main():
    """Entry point for the application."""

    try:
        with unit() as session:
            personage_1 = Personage(name="Guillaume", age=12)
            personage_2 = Personage(name="a", age=-2.3)
            PersonageController.create(session, personage_1)
            PersonageController.create(session, personage_2)
    except AppException as e:
        logger.error("Error %s", e)


if __name__ == "__main__":
    main()
