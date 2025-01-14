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


class RequiredModel401FailedRequestResponse(TypedDict):
    pass

class OptionalModel401FailedRequestResponse(TypedDict, total=False):
    default_detail: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    default_code: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Model401FailedRequestResponse(RequiredModel401FailedRequestResponse, OptionalModel401FailedRequestResponse):
    pass
