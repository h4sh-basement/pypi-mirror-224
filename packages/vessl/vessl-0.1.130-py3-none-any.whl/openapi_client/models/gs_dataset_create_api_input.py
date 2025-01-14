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


class GSDatasetCreateAPIInput(object):
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
        'description': 'str',
        'gs_path': 'str',
        'is_public_bucket': 'bool',
        'is_version_enabled': 'bool',
        'name': 'str',
        'version_gs_path': 'str'
    }

    attribute_map = {
        'description': 'description',
        'gs_path': 'gs_path',
        'is_public_bucket': 'is_public_bucket',
        'is_version_enabled': 'is_version_enabled',
        'name': 'name',
        'version_gs_path': 'version_gs_path'
    }

    def __init__(self, description=None, gs_path=None, is_public_bucket=None, is_version_enabled=None, name=None, version_gs_path=None, local_vars_configuration=None):  # noqa: E501
        """GSDatasetCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._gs_path = None
        self._is_public_bucket = None
        self._is_version_enabled = None
        self._name = None
        self._version_gs_path = None
        self.discriminator = None

        self.description = description
        self.gs_path = gs_path
        if is_public_bucket is not None:
            self.is_public_bucket = is_public_bucket
        if is_version_enabled is not None:
            self.is_version_enabled = is_version_enabled
        self.name = name
        if version_gs_path is not None:
            self.version_gs_path = version_gs_path

    @property
    def description(self):
        """Gets the description of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The description of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GSDatasetCreateAPIInput.


        :param description: The description of this GSDatasetCreateAPIInput.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def gs_path(self):
        """Gets the gs_path of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The gs_path of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._gs_path

    @gs_path.setter
    def gs_path(self, gs_path):
        """Sets the gs_path of this GSDatasetCreateAPIInput.


        :param gs_path: The gs_path of this GSDatasetCreateAPIInput.  # noqa: E501
        :type gs_path: str
        """
        if self.local_vars_configuration.client_side_validation and gs_path is None:  # noqa: E501
            raise ValueError("Invalid value for `gs_path`, must not be `None`")  # noqa: E501

        self._gs_path = gs_path

    @property
    def is_public_bucket(self):
        """Gets the is_public_bucket of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The is_public_bucket of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_bucket

    @is_public_bucket.setter
    def is_public_bucket(self, is_public_bucket):
        """Sets the is_public_bucket of this GSDatasetCreateAPIInput.


        :param is_public_bucket: The is_public_bucket of this GSDatasetCreateAPIInput.  # noqa: E501
        :type is_public_bucket: bool
        """

        self._is_public_bucket = is_public_bucket

    @property
    def is_version_enabled(self):
        """Gets the is_version_enabled of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The is_version_enabled of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_version_enabled

    @is_version_enabled.setter
    def is_version_enabled(self, is_version_enabled):
        """Sets the is_version_enabled of this GSDatasetCreateAPIInput.


        :param is_version_enabled: The is_version_enabled of this GSDatasetCreateAPIInput.  # noqa: E501
        :type is_version_enabled: bool
        """

        self._is_version_enabled = is_version_enabled

    @property
    def name(self):
        """Gets the name of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The name of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GSDatasetCreateAPIInput.


        :param name: The name of this GSDatasetCreateAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def version_gs_path(self):
        """Gets the version_gs_path of this GSDatasetCreateAPIInput.  # noqa: E501


        :return: The version_gs_path of this GSDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._version_gs_path

    @version_gs_path.setter
    def version_gs_path(self, version_gs_path):
        """Sets the version_gs_path of this GSDatasetCreateAPIInput.


        :param version_gs_path: The version_gs_path of this GSDatasetCreateAPIInput.  # noqa: E501
        :type version_gs_path: str
        """

        self._version_gs_path = version_gs_path

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
        if not isinstance(other, GSDatasetCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GSDatasetCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
