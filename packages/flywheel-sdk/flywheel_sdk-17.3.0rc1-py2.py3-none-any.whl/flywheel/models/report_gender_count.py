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

class ReportGenderCount(object):

    swagger_types = {
        'male': 'int',
        'unknown_or_not_reported': 'int',
        'female': 'int'
    }

    attribute_map = {
        'male': 'Male',
        'unknown_or_not_reported': 'Unknown or Not Reported',
        'female': 'Female'
    }

    rattribute_map = {
        'Male': 'male',
        'Unknown or Not Reported': 'unknown_or_not_reported',
        'Female': 'female'
    }

    def __init__(self, male=None, unknown_or_not_reported=None, female=None):  # noqa: E501
        """ReportGenderCount - a model defined in Swagger"""
        super(ReportGenderCount, self).__init__()

        self._male = None
        self._unknown_or_not_reported = None
        self._female = None
        self.discriminator = None
        self.alt_discriminator = None

        self.male = male
        self.unknown_or_not_reported = unknown_or_not_reported
        self.female = female

    @property
    def male(self):
        """Gets the male of this ReportGenderCount.


        :return: The male of this ReportGenderCount.
        :rtype: int
        """
        return self._male

    @male.setter
    def male(self, male):
        """Sets the male of this ReportGenderCount.


        :param male: The male of this ReportGenderCount.  # noqa: E501
        :type: int
        """

        self._male = male

    @property
    def unknown_or_not_reported(self):
        """Gets the unknown_or_not_reported of this ReportGenderCount.


        :return: The unknown_or_not_reported of this ReportGenderCount.
        :rtype: int
        """
        return self._unknown_or_not_reported

    @unknown_or_not_reported.setter
    def unknown_or_not_reported(self, unknown_or_not_reported):
        """Sets the unknown_or_not_reported of this ReportGenderCount.


        :param unknown_or_not_reported: The unknown_or_not_reported of this ReportGenderCount.  # noqa: E501
        :type: int
        """

        self._unknown_or_not_reported = unknown_or_not_reported

    @property
    def female(self):
        """Gets the female of this ReportGenderCount.


        :return: The female of this ReportGenderCount.
        :rtype: int
        """
        return self._female

    @female.setter
    def female(self, female):
        """Sets the female of this ReportGenderCount.


        :param female: The female of this ReportGenderCount.  # noqa: E501
        :type: int
        """

        self._female = female


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
        if not isinstance(other, ReportGenderCount):
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
