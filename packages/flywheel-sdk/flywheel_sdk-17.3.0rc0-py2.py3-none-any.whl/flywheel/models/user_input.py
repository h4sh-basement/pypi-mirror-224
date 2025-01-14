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

from flywheel.models.role_type import RoleType  # noqa: F401,E501

class UserInput(object):

    swagger_types = {
        'id': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'password': 'str',
        'roles': 'list[RoleType]',
        'disabled': 'bool',
        'avatar': 'str',
        'root': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'password': 'password',
        'roles': 'roles',
        'disabled': 'disabled',
        'avatar': 'avatar',
        'root': 'root'
    }

    rattribute_map = {
        '_id': 'id',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'password': 'password',
        'roles': 'roles',
        'disabled': 'disabled',
        'avatar': 'avatar',
        'root': 'root'
    }

    def __init__(self, id=None, firstname=None, lastname=None, email=None, password=None, roles=None, disabled=None, avatar=None, root=None):  # noqa: E501
        """UserInput - a model defined in Swagger"""
        super(UserInput, self).__init__()

        self._id = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._password = None
        self._roles = None
        self._disabled = None
        self._avatar = None
        self._root = None
        self.discriminator = None
        self.alt_discriminator = None

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if roles is not None:
            self.roles = roles
        if disabled is not None:
            self.disabled = disabled
        if avatar is not None:
            self.avatar = avatar
        if root is not None:
            self.root = root

    @property
    def id(self):
        """Gets the id of this UserInput.


        :return: The id of this UserInput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInput.


        :param id: The id of this UserInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def firstname(self):
        """Gets the firstname of this UserInput.


        :return: The firstname of this UserInput.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserInput.


        :param firstname: The firstname of this UserInput.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserInput.


        :return: The lastname of this UserInput.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserInput.


        :param lastname: The lastname of this UserInput.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this UserInput.


        :return: The email of this UserInput.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInput.


        :param email: The email of this UserInput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this UserInput.


        :return: The password of this UserInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserInput.


        :param password: The password of this UserInput.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def roles(self):
        """Gets the roles of this UserInput.


        :return: The roles of this UserInput.
        :rtype: list[RoleType]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserInput.


        :param roles: The roles of this UserInput.  # noqa: E501
        :type: list[RoleType]
        """

        self._roles = roles

    @property
    def disabled(self):
        """Gets the disabled of this UserInput.


        :return: The disabled of this UserInput.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this UserInput.


        :param disabled: The disabled of this UserInput.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def avatar(self):
        """Gets the avatar of this UserInput.


        :return: The avatar of this UserInput.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this UserInput.


        :param avatar: The avatar of this UserInput.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def root(self):
        """Gets the root of this UserInput.


        :return: The root of this UserInput.
        :rtype: bool
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this UserInput.


        :param root: The root of this UserInput.  # noqa: E501
        :type: bool
        """

        self._root = root


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
        if not isinstance(other, UserInput):
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
