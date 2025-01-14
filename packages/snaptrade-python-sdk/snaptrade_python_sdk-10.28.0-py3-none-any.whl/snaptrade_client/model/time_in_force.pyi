# coding: utf-8

"""
    SnapTrade

    Connect brokerage accounts to your app for live positions and trading

    The version of the OpenAPI document: 1.0.0
    Contact: api@snaptrade.com
    Created by: https://snaptrade.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from snaptrade_client import schemas  # noqa: F401


class TimeInForce(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Trade time in force:
  * FOK - Fill Or Kill
  * Day - Day
  * GTC - Good Til Canceled

    """
    
    @schemas.classproperty
    def DAY(cls):
        return cls("Day")
    
    @schemas.classproperty
    def FOK(cls):
        return cls("FOK")
    
    @schemas.classproperty
    def GTC(cls):
        return cls("GTC")
