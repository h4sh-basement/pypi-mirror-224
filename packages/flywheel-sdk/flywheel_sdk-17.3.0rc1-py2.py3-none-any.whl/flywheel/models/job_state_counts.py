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

class JobStateCounts(object):

    swagger_types = {
        'pending': 'int',
        'running': 'int',
        'failed': 'int',
        'complete': 'int',
        'cancelled': 'int'
    }

    attribute_map = {
        'pending': 'pending',
        'running': 'running',
        'failed': 'failed',
        'complete': 'complete',
        'cancelled': 'cancelled'
    }

    rattribute_map = {
        'pending': 'pending',
        'running': 'running',
        'failed': 'failed',
        'complete': 'complete',
        'cancelled': 'cancelled'
    }

    def __init__(self, pending=None, running=None, failed=None, complete=None, cancelled=None):  # noqa: E501
        """JobStateCounts - a model defined in Swagger"""
        super(JobStateCounts, self).__init__()

        self._pending = None
        self._running = None
        self._failed = None
        self._complete = None
        self._cancelled = None
        self.discriminator = None
        self.alt_discriminator = None

        self.pending = pending
        self.running = running
        self.failed = failed
        self.complete = complete
        self.cancelled = cancelled

    @property
    def pending(self):
        """Gets the pending of this JobStateCounts.


        :return: The pending of this JobStateCounts.
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this JobStateCounts.


        :param pending: The pending of this JobStateCounts.  # noqa: E501
        :type: int
        """

        self._pending = pending

    @property
    def running(self):
        """Gets the running of this JobStateCounts.


        :return: The running of this JobStateCounts.
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this JobStateCounts.


        :param running: The running of this JobStateCounts.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def failed(self):
        """Gets the failed of this JobStateCounts.


        :return: The failed of this JobStateCounts.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this JobStateCounts.


        :param failed: The failed of this JobStateCounts.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def complete(self):
        """Gets the complete of this JobStateCounts.


        :return: The complete of this JobStateCounts.
        :rtype: int
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this JobStateCounts.


        :param complete: The complete of this JobStateCounts.  # noqa: E501
        :type: int
        """

        self._complete = complete

    @property
    def cancelled(self):
        """Gets the cancelled of this JobStateCounts.


        :return: The cancelled of this JobStateCounts.
        :rtype: int
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this JobStateCounts.


        :param cancelled: The cancelled of this JobStateCounts.  # noqa: E501
        :type: int
        """

        self._cancelled = cancelled


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
        if not isinstance(other, JobStateCounts):
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
