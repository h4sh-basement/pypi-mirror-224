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

from flywheel.models.file_entry import FileEntry  # noqa: F401,E501
from flywheel.models.subject import Subject  # noqa: F401,E501

class SessionMetadataInput(object):

    swagger_types = {
        'label': 'str',
        'info': 'object',
        'operator': 'str',
        'uid': 'str',
        'timestamp': 'datetime',
        'timezone': 'str',
        'subject': 'Subject',
        'tags': 'list[str]',
        'age': 'int',
        'weight': 'float',
        'files': 'list[FileEntry]'
    }

    attribute_map = {
        'label': 'label',
        'info': 'info',
        'operator': 'operator',
        'uid': 'uid',
        'timestamp': 'timestamp',
        'timezone': 'timezone',
        'subject': 'subject',
        'tags': 'tags',
        'age': 'age',
        'weight': 'weight',
        'files': 'files'
    }

    rattribute_map = {
        'label': 'label',
        'info': 'info',
        'operator': 'operator',
        'uid': 'uid',
        'timestamp': 'timestamp',
        'timezone': 'timezone',
        'subject': 'subject',
        'tags': 'tags',
        'age': 'age',
        'weight': 'weight',
        'files': 'files'
    }

    def __init__(self, label=None, info=None, operator=None, uid=None, timestamp=None, timezone=None, subject=None, tags=None, age=None, weight=None, files=None):  # noqa: E501
        """SessionMetadataInput - a model defined in Swagger"""
        super(SessionMetadataInput, self).__init__()

        self._label = None
        self._info = None
        self._operator = None
        self._uid = None
        self._timestamp = None
        self._timezone = None
        self._subject = None
        self._tags = None
        self._age = None
        self._weight = None
        self._files = None
        self.discriminator = None
        self.alt_discriminator = None

        if label is not None:
            self.label = label
        if info is not None:
            self.info = info
        if operator is not None:
            self.operator = operator
        if uid is not None:
            self.uid = uid
        if timestamp is not None:
            self.timestamp = timestamp
        if timezone is not None:
            self.timezone = timezone
        if subject is not None:
            self.subject = subject
        if tags is not None:
            self.tags = tags
        if age is not None:
            self.age = age
        if weight is not None:
            self.weight = weight
        if files is not None:
            self.files = files

    @property
    def label(self):
        """Gets the label of this SessionMetadataInput.


        :return: The label of this SessionMetadataInput.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SessionMetadataInput.


        :param label: The label of this SessionMetadataInput.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def info(self):
        """Gets the info of this SessionMetadataInput.


        :return: The info of this SessionMetadataInput.
        :rtype: object
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this SessionMetadataInput.


        :param info: The info of this SessionMetadataInput.  # noqa: E501
        :type: object
        """

        self._info = info

    @property
    def operator(self):
        """Gets the operator of this SessionMetadataInput.


        :return: The operator of this SessionMetadataInput.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SessionMetadataInput.


        :param operator: The operator of this SessionMetadataInput.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def uid(self):
        """Gets the uid of this SessionMetadataInput.


        :return: The uid of this SessionMetadataInput.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SessionMetadataInput.


        :param uid: The uid of this SessionMetadataInput.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def timestamp(self):
        """Gets the timestamp of this SessionMetadataInput.


        :return: The timestamp of this SessionMetadataInput.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SessionMetadataInput.


        :param timestamp: The timestamp of this SessionMetadataInput.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def timezone(self):
        """Gets the timezone of this SessionMetadataInput.


        :return: The timezone of this SessionMetadataInput.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SessionMetadataInput.


        :param timezone: The timezone of this SessionMetadataInput.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def subject(self):
        """Gets the subject of this SessionMetadataInput.


        :return: The subject of this SessionMetadataInput.
        :rtype: Subject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SessionMetadataInput.


        :param subject: The subject of this SessionMetadataInput.  # noqa: E501
        :type: Subject
        """

        self._subject = subject

    @property
    def tags(self):
        """Gets the tags of this SessionMetadataInput.

        Array of application-specific tags

        :return: The tags of this SessionMetadataInput.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SessionMetadataInput.

        Array of application-specific tags

        :param tags: The tags of this SessionMetadataInput.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def age(self):
        """Gets the age of this SessionMetadataInput.

        Subject age at time of session, in seconds

        :return: The age of this SessionMetadataInput.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this SessionMetadataInput.

        Subject age at time of session, in seconds

        :param age: The age of this SessionMetadataInput.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def weight(self):
        """Gets the weight of this SessionMetadataInput.

        Subject weight at time of session, in kilograms

        :return: The weight of this SessionMetadataInput.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SessionMetadataInput.

        Subject weight at time of session, in kilograms

        :param weight: The weight of this SessionMetadataInput.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def files(self):
        """Gets the files of this SessionMetadataInput.


        :return: The files of this SessionMetadataInput.
        :rtype: list[FileEntry]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SessionMetadataInput.


        :param files: The files of this SessionMetadataInput.  # noqa: E501
        :type: list[FileEntry]
        """

        self._files = files


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
        if not isinstance(other, SessionMetadataInput):
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
