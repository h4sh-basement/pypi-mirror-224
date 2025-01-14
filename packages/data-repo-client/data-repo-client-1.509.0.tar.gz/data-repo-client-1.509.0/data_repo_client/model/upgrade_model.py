# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
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

from data_repo_client import schemas  # noqa: F401


class UpgradeModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "upgradeType",
            "upgradeName",
        }
        
        class properties:
            upgradeName = schemas.StrSchema
            
            
            class upgradeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "custom": "CUSTOM",
                    }
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
            customName = schemas.StrSchema
            
            
            class customArgs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customArgs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "upgradeName": upgradeName,
                "upgradeType": upgradeType,
                "customName": customName,
                "customArgs": customArgs,
            }
    
    upgradeType: MetaOapg.properties.upgradeType
    upgradeName: MetaOapg.properties.upgradeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upgradeName"]) -> MetaOapg.properties.upgradeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upgradeType"]) -> MetaOapg.properties.upgradeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customName"]) -> MetaOapg.properties.customName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customArgs"]) -> MetaOapg.properties.customArgs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["upgradeName", "upgradeType", "customName", "customArgs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upgradeName"]) -> MetaOapg.properties.upgradeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upgradeType"]) -> MetaOapg.properties.upgradeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customName"]) -> typing.Union[MetaOapg.properties.customName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customArgs"]) -> typing.Union[MetaOapg.properties.customArgs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["upgradeName", "upgradeType", "customName", "customArgs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        upgradeType: typing.Union[MetaOapg.properties.upgradeType, str, ],
        upgradeName: typing.Union[MetaOapg.properties.upgradeName, str, ],
        customName: typing.Union[MetaOapg.properties.customName, str, schemas.Unset] = schemas.unset,
        customArgs: typing.Union[MetaOapg.properties.customArgs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpgradeModel':
        return super().__new__(
            cls,
            *_args,
            upgradeType=upgradeType,
            upgradeName=upgradeName,
            customName=customName,
            customArgs=customArgs,
            _configuration=_configuration,
            **kwargs,
        )
