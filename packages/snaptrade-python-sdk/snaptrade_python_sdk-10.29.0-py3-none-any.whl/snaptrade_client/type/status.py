# coding: utf-8

"""
    SnapTrade

    Connect brokerage accounts to your app for live positions and trading

    The version of the OpenAPI document: 1.0.0
    Contact: api@snaptrade.com
    Created by: https://snaptrade.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal


class RequiredStatus(TypedDict):
    pass

class OptionalStatus(TypedDict, total=False):
    version: int

    timestamp: str

    online: bool

class Status(RequiredStatus, OptionalStatus):
    pass
