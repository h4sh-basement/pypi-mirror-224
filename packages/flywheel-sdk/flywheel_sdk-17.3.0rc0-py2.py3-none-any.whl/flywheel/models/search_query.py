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

class SearchQuery(object):

    swagger_types = {
        'return_type': 'str',
        'search_string': 'str',
        'structured_query': 'str',
        'all_data': 'bool',
        'filters': 'list[object]'
    }

    attribute_map = {
        'return_type': 'return_type',
        'search_string': 'search_string',
        'structured_query': 'structured_query',
        'all_data': 'all_data',
        'filters': 'filters'
    }

    rattribute_map = {
        'return_type': 'return_type',
        'search_string': 'search_string',
        'structured_query': 'structured_query',
        'all_data': 'all_data',
        'filters': 'filters'
    }

    def __init__(self, return_type=None, search_string=None, structured_query=None, all_data=False, filters=None):  # noqa: E501
        """SearchQuery - a model defined in Swagger"""
        super(SearchQuery, self).__init__()

        self._return_type = None
        self._search_string = None
        self._structured_query = None
        self._all_data = None
        self._filters = None
        self.discriminator = None
        self.alt_discriminator = None

        self.return_type = return_type
        if search_string is not None:
            self.search_string = search_string
        if structured_query is not None:
            self.structured_query = structured_query
        if all_data is not None:
            self.all_data = all_data
        if filters is not None:
            self.filters = filters

    @property
    def return_type(self):
        """Gets the return_type of this SearchQuery.

        Sets the type of search results to return

        :return: The return_type of this SearchQuery.
        :rtype: str
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this SearchQuery.

        Sets the type of search results to return

        :param return_type: The return_type of this SearchQuery.  # noqa: E501
        :type: str
        """

        self._return_type = return_type

    @property
    def search_string(self):
        """Gets the search_string of this SearchQuery.

        Represents the plain text search query

        :return: The search_string of this SearchQuery.
        :rtype: str
        """
        return self._search_string

    @search_string.setter
    def search_string(self, search_string):
        """Sets the search_string of this SearchQuery.

        Represents the plain text search query

        :param search_string: The search_string of this SearchQuery.  # noqa: E501
        :type: str
        """

        self._search_string = search_string

    @property
    def structured_query(self):
        """Gets the structured_query of this SearchQuery.

        Represents structured query language search

        :return: The structured_query of this SearchQuery.
        :rtype: str
        """
        return self._structured_query

    @structured_query.setter
    def structured_query(self, structured_query):
        """Sets the structured_query of this SearchQuery.

        Represents structured query language search

        :param structured_query: The structured_query of this SearchQuery.  # noqa: E501
        :type: str
        """

        self._structured_query = structured_query

    @property
    def all_data(self):
        """Gets the all_data of this SearchQuery.

        When set will include all data that the user does not have access to read

        :return: The all_data of this SearchQuery.
        :rtype: bool
        """
        return self._all_data

    @all_data.setter
    def all_data(self, all_data):
        """Sets the all_data of this SearchQuery.

        When set will include all data that the user does not have access to read

        :param all_data: The all_data of this SearchQuery.  # noqa: E501
        :type: bool
        """

        self._all_data = all_data

    @property
    def filters(self):
        """Gets the filters of this SearchQuery.

        See https://www.elastic.co/guide/en/elasticsearch/reference/current/term-level-queries.html

        :return: The filters of this SearchQuery.
        :rtype: list[object]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SearchQuery.

        See https://www.elastic.co/guide/en/elasticsearch/reference/current/term-level-queries.html

        :param filters: The filters of this SearchQuery.  # noqa: E501
        :type: list[object]
        """

        self._filters = filters


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
        if not isinstance(other, SearchQuery):
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
