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

from .mixins import CollectionMixin
class SearchCollectionResponse(CollectionMixin):

    swagger_types = {
        'id': 'str',
        'label': 'str',
        'curator': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'id': '_id',
        'label': 'label',
        'curator': 'curator',
        'created': 'created'
    }

    rattribute_map = {
        '_id': 'id',
        'label': 'label',
        'curator': 'curator',
        'created': 'created'
    }

    def __init__(self, id=None, label=None, curator=None, created=None):  # noqa: E501
        """SearchCollectionResponse - a model defined in Swagger"""
        super(SearchCollectionResponse, self).__init__()

        self._id = None
        self._label = None
        self._curator = None
        self._created = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if curator is not None:
            self.curator = curator
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this SearchCollectionResponse.

        Unique database ID

        :return: The id of this SearchCollectionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchCollectionResponse.

        Unique database ID

        :param id: The id of this SearchCollectionResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SearchCollectionResponse.

        Application-specific label

        :return: The label of this SearchCollectionResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SearchCollectionResponse.

        Application-specific label

        :param label: The label of this SearchCollectionResponse.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def curator(self):
        """Gets the curator of this SearchCollectionResponse.

        Database ID of a user

        :return: The curator of this SearchCollectionResponse.
        :rtype: str
        """
        return self._curator

    @curator.setter
    def curator(self, curator):
        """Sets the curator of this SearchCollectionResponse.

        Database ID of a user

        :param curator: The curator of this SearchCollectionResponse.  # noqa: E501
        :type: str
        """

        self._curator = curator

    @property
    def created(self):
        """Gets the created of this SearchCollectionResponse.

        Creation time (automatically set)

        :return: The created of this SearchCollectionResponse.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SearchCollectionResponse.

        Creation time (automatically set)

        :param created: The created of this SearchCollectionResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created


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
        if not isinstance(other, SearchCollectionResponse):
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
