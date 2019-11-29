# -*- coding: utf-8 -*-
"""
.. module:: logger
    :platform: Unix, Windows
    :synopsis: Shared logger for pyptouch

.. moduleauthor:: Terje Elde <terje@elde.net>

"""

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

logger = logging.getLogger(__name__)

logger.debug("Logger initialized.")
