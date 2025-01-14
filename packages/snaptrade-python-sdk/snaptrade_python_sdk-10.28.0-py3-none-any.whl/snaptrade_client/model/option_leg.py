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


class OptionLeg(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Option Leg
    """


    class MetaOapg:
        
        class properties:
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "BUY_TO_OPEN": "BUY_TO_OPEN",
                        "BUY_TO_CLOSE": "BUY_TO_CLOSE",
                        "SELL_TO_OPEN": "SELL_TO_OPEN",
                        "SELL_TO_CLOSE": "SELL_TO_CLOSE",
                    }
                
                @schemas.classproperty
                def BUY_TO_OPEN(cls):
                    return cls("BUY_TO_OPEN")
                
                @schemas.classproperty
                def BUY_TO_CLOSE(cls):
                    return cls("BUY_TO_CLOSE")
                
                @schemas.classproperty
                def SELL_TO_OPEN(cls):
                    return cls("SELL_TO_OPEN")
                
                @schemas.classproperty
                def SELL_TO_CLOSE(cls):
                    return cls("SELL_TO_CLOSE")
            option_symbol_id = schemas.StrSchema
            quantity = schemas.NumberSchema
            __annotations__ = {
                "action": action,
                "option_symbol_id": option_symbol_id,
                "quantity": quantity,
            }
        additional_properties = schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["option_symbol_id"]) -> MetaOapg.properties.option_symbol_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action"], typing_extensions.Literal["option_symbol_id"], typing_extensions.Literal["quantity"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["option_symbol_id"]) -> typing.Union[MetaOapg.properties.option_symbol_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action"], typing_extensions.Literal["option_symbol_id"], typing_extensions.Literal["quantity"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        option_symbol_id: typing.Union[MetaOapg.properties.option_symbol_id, str, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'OptionLeg':
        return super().__new__(
            cls,
            *args,
            action=action,
            option_symbol_id=option_symbol_id,
            quantity=quantity,
            _configuration=_configuration,
            **kwargs,
        )
