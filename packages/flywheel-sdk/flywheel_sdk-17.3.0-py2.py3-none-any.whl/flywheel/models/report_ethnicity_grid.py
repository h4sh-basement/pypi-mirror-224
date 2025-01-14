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

from flywheel.models.report_gender_count import ReportGenderCount  # noqa: F401,E501

class ReportEthnicityGrid(object):

    swagger_types = {
        'not_hispanic_or_latino': 'ReportGenderCount',
        'hispanic_or_latino': 'ReportGenderCount',
        'unknown_or_not_reported': 'ReportGenderCount',
        'total': 'int'
    }

    attribute_map = {
        'not_hispanic_or_latino': 'Not Hispanic or Latino',
        'hispanic_or_latino': 'Hispanic or Latino',
        'unknown_or_not_reported': 'Unknown or Not Reported',
        'total': 'Total'
    }

    rattribute_map = {
        'Not Hispanic or Latino': 'not_hispanic_or_latino',
        'Hispanic or Latino': 'hispanic_or_latino',
        'Unknown or Not Reported': 'unknown_or_not_reported',
        'Total': 'total'
    }

    def __init__(self, not_hispanic_or_latino=None, hispanic_or_latino=None, unknown_or_not_reported=None, total=None):  # noqa: E501
        """ReportEthnicityGrid - a model defined in Swagger"""
        super(ReportEthnicityGrid, self).__init__()

        self._not_hispanic_or_latino = None
        self._hispanic_or_latino = None
        self._unknown_or_not_reported = None
        self._total = None
        self.discriminator = None
        self.alt_discriminator = None

        if not_hispanic_or_latino is not None:
            self.not_hispanic_or_latino = not_hispanic_or_latino
        if hispanic_or_latino is not None:
            self.hispanic_or_latino = hispanic_or_latino
        if unknown_or_not_reported is not None:
            self.unknown_or_not_reported = unknown_or_not_reported
        if total is not None:
            self.total = total

    @property
    def not_hispanic_or_latino(self):
        """Gets the not_hispanic_or_latino of this ReportEthnicityGrid.


        :return: The not_hispanic_or_latino of this ReportEthnicityGrid.
        :rtype: ReportGenderCount
        """
        return self._not_hispanic_or_latino

    @not_hispanic_or_latino.setter
    def not_hispanic_or_latino(self, not_hispanic_or_latino):
        """Sets the not_hispanic_or_latino of this ReportEthnicityGrid.


        :param not_hispanic_or_latino: The not_hispanic_or_latino of this ReportEthnicityGrid.  # noqa: E501
        :type: ReportGenderCount
        """

        self._not_hispanic_or_latino = not_hispanic_or_latino

    @property
    def hispanic_or_latino(self):
        """Gets the hispanic_or_latino of this ReportEthnicityGrid.


        :return: The hispanic_or_latino of this ReportEthnicityGrid.
        :rtype: ReportGenderCount
        """
        return self._hispanic_or_latino

    @hispanic_or_latino.setter
    def hispanic_or_latino(self, hispanic_or_latino):
        """Sets the hispanic_or_latino of this ReportEthnicityGrid.


        :param hispanic_or_latino: The hispanic_or_latino of this ReportEthnicityGrid.  # noqa: E501
        :type: ReportGenderCount
        """

        self._hispanic_or_latino = hispanic_or_latino

    @property
    def unknown_or_not_reported(self):
        """Gets the unknown_or_not_reported of this ReportEthnicityGrid.


        :return: The unknown_or_not_reported of this ReportEthnicityGrid.
        :rtype: ReportGenderCount
        """
        return self._unknown_or_not_reported

    @unknown_or_not_reported.setter
    def unknown_or_not_reported(self, unknown_or_not_reported):
        """Sets the unknown_or_not_reported of this ReportEthnicityGrid.


        :param unknown_or_not_reported: The unknown_or_not_reported of this ReportEthnicityGrid.  # noqa: E501
        :type: ReportGenderCount
        """

        self._unknown_or_not_reported = unknown_or_not_reported

    @property
    def total(self):
        """Gets the total of this ReportEthnicityGrid.


        :return: The total of this ReportEthnicityGrid.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportEthnicityGrid.


        :param total: The total of this ReportEthnicityGrid.  # noqa: E501
        :type: int
        """

        self._total = total


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
        if not isinstance(other, ReportEthnicityGrid):
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
