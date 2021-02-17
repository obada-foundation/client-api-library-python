"""
    OBADA Client Helper API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: techops@obada.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from obada_client.model_utils import (  # noqa: F401
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
    from obada_client.model.local_obit_documents import LocalObitDocuments
    from obada_client.model.local_obit_metadata import LocalObitMetadata
    from obada_client.model.local_obit_structured_data import LocalObitStructuredData
    globals()['LocalObitDocuments'] = LocalObitDocuments
    globals()['LocalObitMetadata'] = LocalObitMetadata
    globals()['LocalObitStructuredData'] = LocalObitStructuredData


class LocalObit(ModelNormal):
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
        ('obit_status',): {
            'FUNCTIONAL': "FUNCTIONAL",
            'NON_FUNCTIONAL': "NON_FUNCTIONAL",
            'DISPOSED': "DISPOSED",
            'STOLEN': "STOLEN",
            'DISABLED_BY_OWNER': "DISABLED_BY_OWNER",
        },
    }

    validations = {
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
            'owner': (str,),  # noqa: E501
            'obit_status': (str,),  # noqa: E501
            'manufacturer': (str,),  # noqa: E501
            'part_number': (str,),  # noqa: E501
            'serial_number': (str,),  # noqa: E501
            'modified_at': (datetime,),  # noqa: E501
            'metadata': ([LocalObitMetadata],),  # noqa: E501
            'documents': ([LocalObitDocuments],),  # noqa: E501
            'structured_data': ([LocalObitStructuredData],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'owner': 'owner',  # noqa: E501
        'obit_status': 'obit_status',  # noqa: E501
        'manufacturer': 'manufacturer',  # noqa: E501
        'part_number': 'part_number',  # noqa: E501
        'serial_number': 'serial_number',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'documents': 'documents',  # noqa: E501
        'structured_data': 'structured_data',  # noqa: E501
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
    def __init__(self, owner, obit_status, manufacturer, part_number, serial_number, modified_at, *args, **kwargs):  # noqa: E501
        """LocalObit - a model defined in OpenAPI

        Args:
            owner (str): Owner is the person/entity that owns the obit and the physical asset it represents.
            obit_status (str): Represent available Obit statuses:   - FUNCTIONAL   - NON_FUNCTIONAL   - DISPOSED   - STOLEN   - DISABLED_BY_OWNER 
            manufacturer (str): Waiting more specific details from Rohi
            part_number (str): Manufacturer provided. In cases where no part number is provided for the product, use model, or the most specific ID available from the manufacturer. MWCN2LL/A (an iPhone 11 Pro, Silver, 256GB, model A2160)
            serial_number (str): Serial Number
            modified_at (datetime):

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
            metadata ([LocalObitMetadata]): Get description from Rohi. [optional]  # noqa: E501
            documents ([LocalObitDocuments]): To generate this link, take an SHA-256 hash of the document, and link to it as https://www.some-website.com?h1=hash-of-document. Note this does not yet adhere to the hashlink standard. . [optional]  # noqa: E501
            structured_data ([LocalObitStructuredData]): Same as metadata but bigger. Key (string) => Value (string) (hash per line sha256(key + value)). [optional]  # noqa: E501
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

        self.owner = owner
        self.obit_status = obit_status
        self.manufacturer = manufacturer
        self.part_number = part_number
        self.serial_number = serial_number
        self.modified_at = modified_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
