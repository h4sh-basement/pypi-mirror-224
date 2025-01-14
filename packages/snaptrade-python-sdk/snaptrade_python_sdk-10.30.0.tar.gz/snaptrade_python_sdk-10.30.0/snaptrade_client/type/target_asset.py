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

from snaptrade_client.type.percent import Percent
from snaptrade_client.type.target_asset_meta import TargetAssetMeta
from snaptrade_client.type.universal_symbol import UniversalSymbol

class RequiredTargetAsset(TypedDict):
    pass

class OptionalTargetAsset(TypedDict, total=False):
    id: str

    symbol: UniversalSymbol

    percent: Percent

    is_supported: bool

    is_excluded: bool

    meta: TargetAssetMeta

class TargetAsset(RequiredTargetAsset, OptionalTargetAsset):
    pass
