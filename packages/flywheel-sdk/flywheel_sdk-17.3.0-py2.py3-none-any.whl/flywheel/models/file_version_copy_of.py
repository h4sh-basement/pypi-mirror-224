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

from flywheel.models.file_parents import FileParents  # noqa: F401,E501

class FileVersionCopyOf(object):

    swagger_types = {
        'file_id': 'str',
        'version': 'int',
        'parents': 'FileParents',
        'project_label': 'str',
        'group_label': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'version': 'version',
        'parents': 'parents',
        'project_label': 'project_label',
        'group_label': 'group_label'
    }

    rattribute_map = {
        'file_id': 'file_id',
        'version': 'version',
        'parents': 'parents',
        'project_label': 'project_label',
        'group_label': 'group_label'
    }

    def __init__(self, file_id=None, version=None, parents=None, project_label=None, group_label=None):  # noqa: E501
        """FileVersionCopyOf - a model defined in Swagger"""
        super(FileVersionCopyOf, self).__init__()

        self._file_id = None
        self._version = None
        self._parents = None
        self._project_label = None
        self._group_label = None
        self.discriminator = None
        self.alt_discriminator = None

        self.file_id = file_id
        self.version = version
        if parents is not None:
            self.parents = parents
        if project_label is not None:
            self.project_label = project_label
        if group_label is not None:
            self.group_label = group_label

    @property
    def file_id(self):
        """Gets the file_id of this FileVersionCopyOf.


        :return: The file_id of this FileVersionCopyOf.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileVersionCopyOf.


        :param file_id: The file_id of this FileVersionCopyOf.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def version(self):
        """Gets the version of this FileVersionCopyOf.


        :return: The version of this FileVersionCopyOf.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileVersionCopyOf.


        :param version: The version of this FileVersionCopyOf.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def parents(self):
        """Gets the parents of this FileVersionCopyOf.


        :return: The parents of this FileVersionCopyOf.
        :rtype: FileParents
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this FileVersionCopyOf.


        :param parents: The parents of this FileVersionCopyOf.  # noqa: E501
        :type: FileParents
        """

        self._parents = parents

    @property
    def project_label(self):
        """Gets the project_label of this FileVersionCopyOf.


        :return: The project_label of this FileVersionCopyOf.
        :rtype: str
        """
        return self._project_label

    @project_label.setter
    def project_label(self, project_label):
        """Sets the project_label of this FileVersionCopyOf.


        :param project_label: The project_label of this FileVersionCopyOf.  # noqa: E501
        :type: str
        """

        self._project_label = project_label

    @property
    def group_label(self):
        """Gets the group_label of this FileVersionCopyOf.


        :return: The group_label of this FileVersionCopyOf.
        :rtype: str
        """
        return self._group_label

    @group_label.setter
    def group_label(self, group_label):
        """Sets the group_label of this FileVersionCopyOf.


        :param group_label: The group_label of this FileVersionCopyOf.  # noqa: E501
        :type: str
        """

        self._group_label = group_label


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
        if not isinstance(other, FileVersionCopyOf):
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
