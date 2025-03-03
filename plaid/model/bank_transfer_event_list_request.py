"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.bank_transfer_event_type import BankTransferEventType
    globals()['BankTransferEventType'] = BankTransferEventType


class BankTransferEventListRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('bank_transfer_type',): {
            'None': None,
            'DEBIT': "debit",
            'CREDIT': "credit",
            'NULL': "null",
        },
        ('direction',): {
            'None': None,
            'INBOUND': "inbound",
            'OUTBOUND': "outbound",
            'NULL': "null",
        },
    }

    validations = {
        ('count',): {
            'inclusive_maximum': 25,
            'inclusive_minimum': 1,
        },
        ('offset',): {
            'inclusive_minimum': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'start_date': (datetime, none_type,),  # noqa: E501
            'end_date': (datetime, none_type,),  # noqa: E501
            'bank_transfer_id': (str, none_type,),  # noqa: E501
            'account_id': (str, none_type,),  # noqa: E501
            'bank_transfer_type': (str, none_type,),  # noqa: E501
            'event_types': ([BankTransferEventType],),  # noqa: E501
            'count': (int, none_type,),  # noqa: E501
            'offset': (int, none_type,),  # noqa: E501
            'origination_account_id': (str, none_type,),  # noqa: E501
            'direction': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'bank_transfer_id': 'bank_transfer_id',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'bank_transfer_type': 'bank_transfer_type',  # noqa: E501
        'event_types': 'event_types',  # noqa: E501
        'count': 'count',  # noqa: E501
        'offset': 'offset',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'direction': 'direction',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """BankTransferEventListRequest - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            start_date (datetime, none_type): The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`). [optional]  # noqa: E501
            end_date (datetime, none_type): The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`). [optional]  # noqa: E501
            bank_transfer_id (str, none_type): Plaid’s unique identifier for a bank transfer.. [optional]  # noqa: E501
            account_id (str, none_type): The account ID to get events for all transactions to/from an account.. [optional]  # noqa: E501
            bank_transfer_type (str, none_type): The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account.. [optional]  # noqa: E501
            event_types ([BankTransferEventType]): Filter events by event type.. [optional]  # noqa: E501
            count (int, none_type): The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.. [optional] if omitted the server will use the default value of 25  # noqa: E501
            offset (int, none_type): The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.. [optional] if omitted the server will use the default value of 0  # noqa: E501
            origination_account_id (str, none_type): The origination account ID to get events for transfers from a specific origination account.. [optional]  # noqa: E501
            direction (str, none_type): Indicates the direction of the transfer: `outbound`: for API-initiated transfers `inbound`: for payments received by the FBO account.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
