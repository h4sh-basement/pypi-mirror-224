# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ResponseProject(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_dt': 'datetime',
        'description': 'str',
        'id': 'int',
        'is_example': 'bool',
        'key_metrics': 'OrmKeyMetrics',
        'name': 'str',
        'note': 'str',
        'updated_dt': 'datetime',
        'volume_id': 'int'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'description': 'description',
        'id': 'id',
        'is_example': 'is_example',
        'key_metrics': 'key_metrics',
        'name': 'name',
        'note': 'note',
        'updated_dt': 'updated_dt',
        'volume_id': 'volume_id'
    }

    def __init__(self, created_dt=None, description=None, id=None, is_example=None, key_metrics=None, name=None, note=None, updated_dt=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """ResponseProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._description = None
        self._id = None
        self._is_example = None
        self._key_metrics = None
        self._name = None
        self._note = None
        self._updated_dt = None
        self._volume_id = None
        self.discriminator = None

        self.created_dt = created_dt
        self.description = description
        self.id = id
        self.is_example = is_example
        if key_metrics is not None:
            self.key_metrics = key_metrics
        self.name = name
        self.note = note
        self.updated_dt = updated_dt
        self.volume_id = volume_id

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseProject.  # noqa: E501


        :return: The created_dt of this ResponseProject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseProject.


        :param created_dt: The created_dt of this ResponseProject.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def description(self):
        """Gets the description of this ResponseProject.  # noqa: E501


        :return: The description of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseProject.


        :param description: The description of this ResponseProject.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ResponseProject.  # noqa: E501


        :return: The id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseProject.


        :param id: The id of this ResponseProject.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_example(self):
        """Gets the is_example of this ResponseProject.  # noqa: E501


        :return: The is_example of this ResponseProject.  # noqa: E501
        :rtype: bool
        """
        return self._is_example

    @is_example.setter
    def is_example(self, is_example):
        """Sets the is_example of this ResponseProject.


        :param is_example: The is_example of this ResponseProject.  # noqa: E501
        :type is_example: bool
        """
        if self.local_vars_configuration.client_side_validation and is_example is None:  # noqa: E501
            raise ValueError("Invalid value for `is_example`, must not be `None`")  # noqa: E501

        self._is_example = is_example

    @property
    def key_metrics(self):
        """Gets the key_metrics of this ResponseProject.  # noqa: E501


        :return: The key_metrics of this ResponseProject.  # noqa: E501
        :rtype: OrmKeyMetrics
        """
        return self._key_metrics

    @key_metrics.setter
    def key_metrics(self, key_metrics):
        """Sets the key_metrics of this ResponseProject.


        :param key_metrics: The key_metrics of this ResponseProject.  # noqa: E501
        :type key_metrics: OrmKeyMetrics
        """

        self._key_metrics = key_metrics

    @property
    def name(self):
        """Gets the name of this ResponseProject.  # noqa: E501


        :return: The name of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseProject.


        :param name: The name of this ResponseProject.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def note(self):
        """Gets the note of this ResponseProject.  # noqa: E501


        :return: The note of this ResponseProject.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ResponseProject.


        :param note: The note of this ResponseProject.  # noqa: E501
        :type note: str
        """

        self._note = note

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseProject.  # noqa: E501


        :return: The updated_dt of this ResponseProject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseProject.


        :param updated_dt: The updated_dt of this ResponseProject.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def volume_id(self):
        """Gets the volume_id of this ResponseProject.  # noqa: E501


        :return: The volume_id of this ResponseProject.  # noqa: E501
        :rtype: int
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ResponseProject.


        :param volume_id: The volume_id of this ResponseProject.  # noqa: E501
        :type volume_id: int
        """
        if self.local_vars_configuration.client_side_validation and volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseProject):
            return True

        return self.to_dict() != other.to_dict()
