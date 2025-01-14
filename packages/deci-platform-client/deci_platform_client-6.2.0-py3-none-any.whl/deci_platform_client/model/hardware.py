# coding: utf-8

"""
    Deci Platform API

    Train, deploy, optimize and serve your models using Deci's platform, in your cloud or on premise.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
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

from deci_platform_client import schemas  # noqa: F401


class Hardware(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A base class for all of Deci's model classes.
A model stores data in constant fields, and let us manipulate the data in a more readable way.
    """


    class MetaOapg:
        required = {
            "jobLabel",
            "machineModel",
            "environment",
            "taint",
            "vendor",
            "deprecated",
            "name",
            "label",
            "family",
            "inferyVersion",
            "defaultBatchSizeList",
            "group",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def family() -> typing.Type['InferenceHardware']:
                return InferenceHardware
            machineModel = schemas.StrSchema
        
            @staticmethod
            def environment() -> typing.Type['HardwareEnvironment']:
                return HardwareEnvironment
        
            @staticmethod
            def vendor() -> typing.Type['HardwareVendor']:
                return HardwareVendor
            jobLabel = schemas.StrSchema
            taint = schemas.StrSchema
            label = schemas.StrSchema
        
            @staticmethod
            def group() -> typing.Type['HardwareGroup']:
                return HardwareGroup
        
            @staticmethod
            def inferyVersion() -> typing.Type['InferyVersion']:
                return InferyVersion
            
            
            class defaultBatchSizeList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultBatchSizeList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            deprecated = schemas.BoolSchema
            updateTime = schemas.DateTimeSchema
            creationTime = schemas.DateTimeSchema
            id = schemas.UUIDSchema
            deleted = schemas.BoolSchema
        
            @staticmethod
            def imageRepository() -> typing.Type['HardwareImageRepository']:
                return HardwareImageRepository
        
            @staticmethod
            def imageDistribution() -> typing.Type['HardwareImageDistribution']:
                return HardwareImageDistribution
            __annotations__ = {
                "name": name,
                "family": family,
                "machineModel": machineModel,
                "environment": environment,
                "vendor": vendor,
                "jobLabel": jobLabel,
                "taint": taint,
                "label": label,
                "group": group,
                "inferyVersion": inferyVersion,
                "defaultBatchSizeList": defaultBatchSizeList,
                "deprecated": deprecated,
                "updateTime": updateTime,
                "creationTime": creationTime,
                "id": id,
                "deleted": deleted,
                "imageRepository": imageRepository,
                "imageDistribution": imageDistribution,
            }
    
    jobLabel: MetaOapg.properties.jobLabel
    machineModel: MetaOapg.properties.machineModel
    environment: 'HardwareEnvironment'
    taint: MetaOapg.properties.taint
    vendor: 'HardwareVendor'
    deprecated: MetaOapg.properties.deprecated
    name: MetaOapg.properties.name
    label: MetaOapg.properties.label
    family: 'InferenceHardware'
    inferyVersion: 'InferyVersion'
    defaultBatchSizeList: MetaOapg.properties.defaultBatchSizeList
    group: 'HardwareGroup'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["family"]) -> 'InferenceHardware': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["machineModel"]) -> MetaOapg.properties.machineModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> 'HardwareEnvironment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor"]) -> 'HardwareVendor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobLabel"]) -> MetaOapg.properties.jobLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taint"]) -> MetaOapg.properties.taint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> 'HardwareGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inferyVersion"]) -> 'InferyVersion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultBatchSizeList"]) -> MetaOapg.properties.defaultBatchSizeList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deprecated"]) -> MetaOapg.properties.deprecated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateTime"]) -> MetaOapg.properties.updateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationTime"]) -> MetaOapg.properties.creationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageRepository"]) -> 'HardwareImageRepository': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageDistribution"]) -> 'HardwareImageDistribution': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "family", "machineModel", "environment", "vendor", "jobLabel", "taint", "label", "group", "inferyVersion", "defaultBatchSizeList", "deprecated", "updateTime", "creationTime", "id", "deleted", "imageRepository", "imageDistribution", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["family"]) -> 'InferenceHardware': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["machineModel"]) -> MetaOapg.properties.machineModel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> 'HardwareEnvironment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> 'HardwareVendor': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobLabel"]) -> MetaOapg.properties.jobLabel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taint"]) -> MetaOapg.properties.taint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> 'HardwareGroup': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inferyVersion"]) -> 'InferyVersion': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultBatchSizeList"]) -> MetaOapg.properties.defaultBatchSizeList: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deprecated"]) -> MetaOapg.properties.deprecated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateTime"]) -> typing.Union[MetaOapg.properties.updateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationTime"]) -> typing.Union[MetaOapg.properties.creationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union[MetaOapg.properties.deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageRepository"]) -> typing.Union['HardwareImageRepository', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageDistribution"]) -> typing.Union['HardwareImageDistribution', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "family", "machineModel", "environment", "vendor", "jobLabel", "taint", "label", "group", "inferyVersion", "defaultBatchSizeList", "deprecated", "updateTime", "creationTime", "id", "deleted", "imageRepository", "imageDistribution", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        jobLabel: typing.Union[MetaOapg.properties.jobLabel, str, ],
        machineModel: typing.Union[MetaOapg.properties.machineModel, str, ],
        environment: 'HardwareEnvironment',
        taint: typing.Union[MetaOapg.properties.taint, str, ],
        vendor: 'HardwareVendor',
        deprecated: typing.Union[MetaOapg.properties.deprecated, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        family: 'InferenceHardware',
        inferyVersion: 'InferyVersion',
        defaultBatchSizeList: typing.Union[MetaOapg.properties.defaultBatchSizeList, list, tuple, ],
        group: 'HardwareGroup',
        updateTime: typing.Union[MetaOapg.properties.updateTime, str, datetime, schemas.Unset] = schemas.unset,
        creationTime: typing.Union[MetaOapg.properties.creationTime, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        deleted: typing.Union[MetaOapg.properties.deleted, bool, schemas.Unset] = schemas.unset,
        imageRepository: typing.Union['HardwareImageRepository', schemas.Unset] = schemas.unset,
        imageDistribution: typing.Union['HardwareImageDistribution', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Hardware':
        return super().__new__(
            cls,
            *_args,
            jobLabel=jobLabel,
            machineModel=machineModel,
            environment=environment,
            taint=taint,
            vendor=vendor,
            deprecated=deprecated,
            name=name,
            label=label,
            family=family,
            inferyVersion=inferyVersion,
            defaultBatchSizeList=defaultBatchSizeList,
            group=group,
            updateTime=updateTime,
            creationTime=creationTime,
            id=id,
            deleted=deleted,
            imageRepository=imageRepository,
            imageDistribution=imageDistribution,
            _configuration=_configuration,
            **kwargs,
        )

from deci_platform_client.model.hardware_environment import HardwareEnvironment
from deci_platform_client.model.hardware_group import HardwareGroup
from deci_platform_client.model.hardware_image_distribution import HardwareImageDistribution
from deci_platform_client.model.hardware_image_repository import HardwareImageRepository
from deci_platform_client.model.hardware_vendor import HardwareVendor
from deci_platform_client.model.inference_hardware import InferenceHardware
from deci_platform_client.model.infery_version import InferyVersion
