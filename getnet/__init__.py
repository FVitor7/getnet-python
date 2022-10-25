"""
GetNet-Py
=========

This package implements an API client to Santander Getnet.
"""
import logging

from .client import Client
from .environment import Environment

__version__ = "1.1"

import requests

if requests.__version__ < "2.0.0":
    msg = (
        "You are using requests version %s, which is older than "
        "getnet-py expects, please upgrade to 2.0.0 or later."
    )
    raise Warning(msg % requests.__version__)

logging.getLogger(__name__).addHandler(logging.NullHandler())
