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


class RequiredOptionLeg(TypedDict):
    pass

class OptionalOptionLeg(TypedDict, total=False):
    action: str

    # Obtained from calling options chain endpoint (option_id)
    option_symbol_id: str

    quantity: typing.Union[int, float]

class OptionLeg(RequiredOptionLeg, OptionalOptionLeg):
    pass
