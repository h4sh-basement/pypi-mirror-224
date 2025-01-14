# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
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

from humanloop import schemas  # noqa: F401


class EnvironmentProjectConfigRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            config_id = schemas.StrSchema
            experiment_id = schemas.StrSchema
            
            
            class environments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EnvironmentRequest']:
                        return EnvironmentRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EnvironmentRequest'], typing.List['EnvironmentRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'environments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EnvironmentRequest':
                    return super().__getitem__(i)
            __annotations__ = {
                "config_id": config_id,
                "experiment_id": experiment_id,
                "environments": environments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["experiment_id"]) -> MetaOapg.properties.experiment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environments"]) -> MetaOapg.properties.environments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["config_id", "experiment_id", "environments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_id"]) -> typing.Union[MetaOapg.properties.config_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["experiment_id"]) -> typing.Union[MetaOapg.properties.experiment_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environments"]) -> typing.Union[MetaOapg.properties.environments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config_id", "experiment_id", "environments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        config_id: typing.Union[MetaOapg.properties.config_id, str, schemas.Unset] = schemas.unset,
        experiment_id: typing.Union[MetaOapg.properties.experiment_id, str, schemas.Unset] = schemas.unset,
        environments: typing.Union[MetaOapg.properties.environments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EnvironmentProjectConfigRequest':
        return super().__new__(
            cls,
            *args,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.environment_request import EnvironmentRequest
