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


class User(
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
            "state",
            "userId",
            "email",
        }
        
        class properties:
            userId = schemas.UUIDSchema
            email = schemas.StrSchema
        
            @staticmethod
            def state() -> typing.Type['UserState']:
                return UserState
            updateTime = schemas.DateTimeSchema
            creationTime = schemas.DateTimeSchema
            id = schemas.UUIDSchema
            deleted = schemas.BoolSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            companyId = schemas.UUIDSchema
            jobTitle = schemas.StrSchema
            
            
            class featureFlags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserFeatureFlagMetadata']:
                        return UserFeatureFlagMetadata
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['UserFeatureFlagMetadata'], typing.List['UserFeatureFlagMetadata']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'featureFlags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserFeatureFlagMetadata':
                    return super().__getitem__(i)
            
            
            class deciRole(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            DeciRole,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'deciRole':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            authProvider = schemas.StrSchema
            __annotations__ = {
                "userId": userId,
                "email": email,
                "state": state,
                "updateTime": updateTime,
                "creationTime": creationTime,
                "id": id,
                "deleted": deleted,
                "firstName": firstName,
                "lastName": lastName,
                "companyId": companyId,
                "jobTitle": jobTitle,
                "featureFlags": featureFlags,
                "deciRole": deciRole,
                "authProvider": authProvider,
            }
    
    state: 'UserState'
    userId: MetaOapg.properties.userId
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'UserState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateTime"]) -> MetaOapg.properties.updateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationTime"]) -> MetaOapg.properties.creationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobTitle"]) -> MetaOapg.properties.jobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featureFlags"]) -> MetaOapg.properties.featureFlags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deciRole"]) -> MetaOapg.properties.deciRole: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authProvider"]) -> MetaOapg.properties.authProvider: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userId", "email", "state", "updateTime", "creationTime", "id", "deleted", "firstName", "lastName", "companyId", "jobTitle", "featureFlags", "deciRole", "authProvider", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> 'UserState': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateTime"]) -> typing.Union[MetaOapg.properties.updateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationTime"]) -> typing.Union[MetaOapg.properties.creationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union[MetaOapg.properties.deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobTitle"]) -> typing.Union[MetaOapg.properties.jobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featureFlags"]) -> typing.Union[MetaOapg.properties.featureFlags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deciRole"]) -> typing.Union[MetaOapg.properties.deciRole, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authProvider"]) -> typing.Union[MetaOapg.properties.authProvider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userId", "email", "state", "updateTime", "creationTime", "id", "deleted", "firstName", "lastName", "companyId", "jobTitle", "featureFlags", "deciRole", "authProvider", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        state: 'UserState',
        userId: typing.Union[MetaOapg.properties.userId, str, uuid.UUID, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        updateTime: typing.Union[MetaOapg.properties.updateTime, str, datetime, schemas.Unset] = schemas.unset,
        creationTime: typing.Union[MetaOapg.properties.creationTime, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        deleted: typing.Union[MetaOapg.properties.deleted, bool, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        jobTitle: typing.Union[MetaOapg.properties.jobTitle, str, schemas.Unset] = schemas.unset,
        featureFlags: typing.Union[MetaOapg.properties.featureFlags, list, tuple, schemas.Unset] = schemas.unset,
        deciRole: typing.Union[MetaOapg.properties.deciRole, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        authProvider: typing.Union[MetaOapg.properties.authProvider, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            state=state,
            userId=userId,
            email=email,
            updateTime=updateTime,
            creationTime=creationTime,
            id=id,
            deleted=deleted,
            firstName=firstName,
            lastName=lastName,
            companyId=companyId,
            jobTitle=jobTitle,
            featureFlags=featureFlags,
            deciRole=deciRole,
            authProvider=authProvider,
            _configuration=_configuration,
            **kwargs,
        )

from deci_platform_client.model.deci_role import DeciRole
from deci_platform_client.model.user_feature_flag_metadata import UserFeatureFlagMetadata
from deci_platform_client.model.user_state import UserState
