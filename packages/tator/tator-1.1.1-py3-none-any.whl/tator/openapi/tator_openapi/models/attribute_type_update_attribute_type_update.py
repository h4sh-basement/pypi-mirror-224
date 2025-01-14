# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ..configuration import Configuration


class AttributeTypeUpdateAttributeTypeUpdate(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'autocomplete': 'AutocompleteService',
        'choices': 'list[str]',
        'default': 'object',
        'description': 'str',
        'dtype': 'str',
        'labels': 'list[str]',
        'maximum': 'float',
        'minimum': 'float',
        'name': 'str',
        'order': 'int',
        'required': 'bool',
        'size': 'int',
        'style': 'str',
        'use_current': 'bool',
        'visible': 'bool'
    }

    attribute_map = {
        'autocomplete': 'autocomplete',
        'choices': 'choices',
        'default': 'default',
        'description': 'description',
        'dtype': 'dtype',
        'labels': 'labels',
        'maximum': 'maximum',
        'minimum': 'minimum',
        'name': 'name',
        'order': 'order',
        'required': 'required',
        'size': 'size',
        'style': 'style',
        'use_current': 'use_current',
        'visible': 'visible'
    }

    def __init__(self, autocomplete=None, choices=None, default=None, description=None, dtype=None, labels=None, maximum=None, minimum=None, name=None, order=None, required=None, size=None, style=None, use_current=None, visible=None, local_vars_configuration=None):  # noqa: E501
        """AttributeTypeUpdateAttributeTypeUpdate - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._autocomplete = None
        self._choices = None
        self._default = None
        self._description = None
        self._dtype = None
        self._labels = None
        self._maximum = None
        self._minimum = None
        self._name = None
        self._order = None
        self._required = None
        self._size = None
        self._style = None
        self._use_current = None
        self._visible = None
        self.discriminator = None

        self.autocomplete = autocomplete
        if choices is not None:
            self.choices = choices
        self.default = default
        if description is not None:
            self.description = description
        if dtype is not None:
            self.dtype = dtype
        if labels is not None:
            self.labels = labels
        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum
        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if required is not None:
            self.required = required
        if size is not None:
            self.size = size
        if style is not None:
            self.style = style
        if use_current is not None:
            self.use_current = use_current
        if visible is not None:
            self.visible = visible

    @property
    def autocomplete(self):
        """

        :return: The autocomplete of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: AutocompleteService
        """
        return self._autocomplete

    @autocomplete.setter
    def autocomplete(self, autocomplete):
        """

        :param autocomplete: The autocomplete of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: AutocompleteService
        """

        self._autocomplete = autocomplete

    @property
    def choices(self):
        """
        Array of possible values; required for enum dtype.

        :return: The choices of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: list[str]
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """
        Array of possible values; required for enum dtype.

        :param choices: The choices of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: list[str]
        """

        self._choices = choices

    @property
    def default(self):
        """
        Boolean, integer, float, string, datetime, [lon, lat], float array.

        :return: The default of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Boolean, integer, float, string, datetime, [lon, lat], float array.

        :param default: The default of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: object
        """

        self._default = default

    @property
    def description(self):
        """
        Description of the attribute.

        :return: The description of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Description of the attribute.

        :param description: The description of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: str
        """

        self._description = description

    @property
    def dtype(self):
        """
        Data type of the attribute.

        :return: The dtype of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """
        Data type of the attribute.

        :param dtype: The dtype of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: str
        """
        allowed_values = ["bool", "int", "float", "enum", "string", "datetime", "geopos", "float_array"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dtype not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dtype` ({0}), must be one of {1}"  # noqa: E501
                .format(dtype, allowed_values)
            )

        self._dtype = dtype

    @property
    def labels(self):
        """
        Array of labels for enum dtype.

        :return: The labels of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Array of labels for enum dtype.

        :param labels: The labels of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: list[str]
        """

        self._labels = labels

    @property
    def maximum(self):
        """
        Upper bound for int or float dtype.

        :return: The maximum of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Upper bound for int or float dtype.

        :param maximum: The maximum of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: float
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """
        Lower bound for int or float dtype.

        :return: The minimum of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Lower bound for int or float dtype.

        :param minimum: The minimum of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: float
        """

        self._minimum = minimum

    @property
    def name(self):
        """
        Name of the attribute. The first character must not be '$', which is a reserved character for system usage.

        :return: The name of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Name of the attribute. The first character must not be '$', which is a reserved character for system usage.

        :param name: The name of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """
        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.

        :return: The order of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Integer specifying relative order this attribute is displayed in the UI. Negative values are hidden by default.

        :param order: The order of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: int
        """

        self._order = order

    @property
    def required(self):
        """
        True if this attribute is required for POST requests.

        :return: The required of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        True if this attribute is required for POST requests.

        :param required: The required of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: bool
        """

        self._required = required

    @property
    def size(self):
        """
        Number of elements for `float_array` dtype.

        :return: The size of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Number of elements for `float_array` dtype.

        :param size: The size of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size > 2000):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `2000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 1):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._size = size

    @property
    def style(self):
        """
        Available options: disabled|long_string|start_frame|end_frame|start_frame_check|end_frame_check   Multiple options can be chained together separated by white space. \"disabled\" will not allow the user to edit the attribute in the Tator GUI. Create a text area string if \"long_string\" is combined with \"string\" dtype. \"start_frame\" and \"end_frame\" used in conjunction with \"attr_style_range\" interpolation. \"start_frame_check and \"end_frame_check\" are used in conjunction with \"attr_style_range\" interpolation. \"range_set and in_video_check\" is used in conjunction with \"attr_style_range\" interpolation. When associated with a bool, these checks will result in Tator GUI changes with the corresponding start_frame and end_frame attributes.

        :return: The style of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Available options: disabled|long_string|start_frame|end_frame|start_frame_check|end_frame_check   Multiple options can be chained together separated by white space. \"disabled\" will not allow the user to edit the attribute in the Tator GUI. Create a text area string if \"long_string\" is combined with \"string\" dtype. \"start_frame\" and \"end_frame\" used in conjunction with \"attr_style_range\" interpolation. \"start_frame_check and \"end_frame_check\" are used in conjunction with \"attr_style_range\" interpolation. \"range_set and in_video_check\" is used in conjunction with \"attr_style_range\" interpolation. When associated with a bool, these checks will result in Tator GUI changes with the corresponding start_frame and end_frame attributes.

        :param style: The style of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: str
        """

        self._style = style

    @property
    def use_current(self):
        """
        True to use current datetime as default for datetime dtype.

        :return: The use_current of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: bool
        """
        return self._use_current

    @use_current.setter
    def use_current(self, use_current):
        """
        True to use current datetime as default for datetime dtype.

        :param use_current: The use_current of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: bool
        """

        self._use_current = use_current

    @property
    def visible(self):
        """
        True to make attribute visible.

        :return: The visible of this AttributeTypeUpdateAttributeTypeUpdate. 
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        True to make attribute visible.

        :param visible: The visible of this AttributeTypeUpdateAttributeTypeUpdate.
        :type: bool
        """

        self._visible = visible

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AttributeTypeUpdateAttributeTypeUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttributeTypeUpdateAttributeTypeUpdate):
            return True

        return self.to_dict() != other.to_dict()
