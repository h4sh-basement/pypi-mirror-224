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

class ProjectCopyOutput(object):

    swagger_types = {
        'task_id': 'str',
        'snapshot_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'snapshot_id': 'snapshot_id',
        'project_id': 'project_id'
    }

    rattribute_map = {
        'task_id': 'task_id',
        'snapshot_id': 'snapshot_id',
        'project_id': 'project_id'
    }

    def __init__(self, task_id=None, snapshot_id=None, project_id=None):  # noqa: E501
        """ProjectCopyOutput - a model defined in Swagger"""
        super(ProjectCopyOutput, self).__init__()

        self._task_id = None
        self._snapshot_id = None
        self._project_id = None
        self.discriminator = None
        self.alt_discriminator = None

        self.task_id = task_id
        self.snapshot_id = snapshot_id
        self.project_id = project_id

    @property
    def task_id(self):
        """Gets the task_id of this ProjectCopyOutput.


        :return: The task_id of this ProjectCopyOutput.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ProjectCopyOutput.


        :param task_id: The task_id of this ProjectCopyOutput.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this ProjectCopyOutput.


        :return: The snapshot_id of this ProjectCopyOutput.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this ProjectCopyOutput.


        :param snapshot_id: The snapshot_id of this ProjectCopyOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_id = snapshot_id

    @property
    def project_id(self):
        """Gets the project_id of this ProjectCopyOutput.


        :return: The project_id of this ProjectCopyOutput.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ProjectCopyOutput.


        :param project_id: The project_id of this ProjectCopyOutput.  # noqa: E501
        :type: str
        """

        self._project_id = project_id


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
        if not isinstance(other, ProjectCopyOutput):
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
