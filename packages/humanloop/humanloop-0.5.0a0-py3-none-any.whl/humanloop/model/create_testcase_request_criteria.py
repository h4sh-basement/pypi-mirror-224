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


class CreateTestcaseRequestCriteria(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Object with criteria necessary to evaluate this testcase.
    """


    class MetaOapg:
        
        
        class additional_properties(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                any_of_0 = schemas.DictSchema
                
                
                class any_of_1(
                    schemas.ListSchema
                ):
                
                
                    class MetaOapg:
                        items = schemas.AnyTypeSchema
                
                    def __new__(
                        cls,
                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                    ) -> 'any_of_1':
                        return super().__new__(
                            cls,
                            arg,
                            _configuration=_configuration,
                        )
                
                    def __getitem__(self, i: int) -> MetaOapg.items:
                        return super().__getitem__(i)
                any_of_2 = schemas.BoolSchema
                any_of_3 = schemas.NumberSchema
                any_of_4 = schemas.IntSchema
                any_of_5 = schemas.StrSchema
                
                @classmethod
                @functools.lru_cache()
                def any_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.any_of_0,
                        cls.any_of_1,
                        cls.any_of_2,
                        cls.any_of_3,
                        cls.any_of_4,
                        cls.any_of_5,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'CreateTestcaseRequestCriteria':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
