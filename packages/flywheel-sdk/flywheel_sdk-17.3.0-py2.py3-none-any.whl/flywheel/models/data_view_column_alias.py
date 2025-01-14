# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401
import six

class DataViewColumnAlias(object):

    swagger_types = {
        'name': 'str',
        'src': 'str',
        'group': 'list[str]',
        'description': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'src': 'src',
        'group': 'group',
        'description': 'description',
        'type': 'type'
    }

    rattribute_map = {
        'name': 'name',
        'src': 'src',
        'group': 'group',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, name=None, src=None, group=None, description=None, type=None):  # noqa: E501
        """DataViewColumnAlias - a model defined in Swagger"""
        super(DataViewColumnAlias, self).__init__()

        self._name = None
        self._src = None
        self._group = None
        self._description = None
        self._type = None
        self.discriminator = None
        self.alt_discriminator = None

        self.name = name
        if src is not None:
            self.src = src
        if group is not None:
            self.group = group
        self.description = description
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this DataViewColumnAlias.

        The column alias name

        :return: The name of this DataViewColumnAlias.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataViewColumnAlias.

        The column alias name

        :param name: The name of this DataViewColumnAlias.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def src(self):
        """Gets the src of this DataViewColumnAlias.

        The source for this column's data

        :return: The src of this DataViewColumnAlias.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this DataViewColumnAlias.

        The source for this column's data

        :param src: The src of this DataViewColumnAlias.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def group(self):
        """Gets the group of this DataViewColumnAlias.

        The list of columns that belong to this group

        :return: The group of this DataViewColumnAlias.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DataViewColumnAlias.

        The list of columns that belong to this group

        :param group: The group of this DataViewColumnAlias.  # noqa: E501
        :type: list[str]
        """

        self._group = group

    @property
    def description(self):
        """Gets the description of this DataViewColumnAlias.

        A description of this field

        :return: The description of this DataViewColumnAlias.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataViewColumnAlias.

        A description of this field

        :param description: The description of this DataViewColumnAlias.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this DataViewColumnAlias.

        The type that this value should be translated to (for typed output)

        :return: The type of this DataViewColumnAlias.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataViewColumnAlias.

        The type that this value should be translated to (for typed output)

        :param type: The type of this DataViewColumnAlias.  # noqa: E501
        :type: str
        """

        self._type = type


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, DataViewColumnAlias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
