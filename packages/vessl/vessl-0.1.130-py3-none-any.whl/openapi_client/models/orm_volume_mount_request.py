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


class OrmVolumeMountRequest(object):
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
        'archive_file': 'OrmVolumeMountRequestSourceArchiveFile',
        'code': 'OrmVolumeMountRequestSourceCode',
        'dataset': 'OrmVolumeMountRequestSourceDataset',
        'dataset_version': 'OrmVolumeMountRequestSourceDatasetVersion',
        'empty_dir': 'object',
        'model_volume': 'OrmVolumeMountRequestSourceModelVolume',
        'mount_path': 'str',
        'object_storage': 'OrmVolumeMountRequestSourceObjectStorage',
        'on_premise': 'OrmOnPremiseVolumeConfig',
        'output': 'object',
        'readonly': 'bool',
        'source_type': 'str',
        'volume': 'OrmVolumeMountRequestSourceVolume'
    }

    attribute_map = {
        'archive_file': 'archive_file',
        'code': 'code',
        'dataset': 'dataset',
        'dataset_version': 'dataset_version',
        'empty_dir': 'empty_dir',
        'model_volume': 'model_volume',
        'mount_path': 'mount_path',
        'object_storage': 'object_storage',
        'on_premise': 'on_premise',
        'output': 'output',
        'readonly': 'readonly',
        'source_type': 'source_type',
        'volume': 'volume'
    }

    def __init__(self, archive_file=None, code=None, dataset=None, dataset_version=None, empty_dir=None, model_volume=None, mount_path=None, object_storage=None, on_premise=None, output=None, readonly=None, source_type=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """OrmVolumeMountRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._archive_file = None
        self._code = None
        self._dataset = None
        self._dataset_version = None
        self._empty_dir = None
        self._model_volume = None
        self._mount_path = None
        self._object_storage = None
        self._on_premise = None
        self._output = None
        self._readonly = None
        self._source_type = None
        self._volume = None
        self.discriminator = None

        if archive_file is not None:
            self.archive_file = archive_file
        if code is not None:
            self.code = code
        if dataset is not None:
            self.dataset = dataset
        if dataset_version is not None:
            self.dataset_version = dataset_version
        if empty_dir is not None:
            self.empty_dir = empty_dir
        if model_volume is not None:
            self.model_volume = model_volume
        self.mount_path = mount_path
        if object_storage is not None:
            self.object_storage = object_storage
        if on_premise is not None:
            self.on_premise = on_premise
        if output is not None:
            self.output = output
        if readonly is not None:
            self.readonly = readonly
        self.source_type = source_type
        if volume is not None:
            self.volume = volume

    @property
    def archive_file(self):
        """Gets the archive_file of this OrmVolumeMountRequest.  # noqa: E501


        :return: The archive_file of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceArchiveFile
        """
        return self._archive_file

    @archive_file.setter
    def archive_file(self, archive_file):
        """Sets the archive_file of this OrmVolumeMountRequest.


        :param archive_file: The archive_file of this OrmVolumeMountRequest.  # noqa: E501
        :type archive_file: OrmVolumeMountRequestSourceArchiveFile
        """

        self._archive_file = archive_file

    @property
    def code(self):
        """Gets the code of this OrmVolumeMountRequest.  # noqa: E501


        :return: The code of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OrmVolumeMountRequest.


        :param code: The code of this OrmVolumeMountRequest.  # noqa: E501
        :type code: OrmVolumeMountRequestSourceCode
        """

        self._code = code

    @property
    def dataset(self):
        """Gets the dataset of this OrmVolumeMountRequest.  # noqa: E501


        :return: The dataset of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceDataset
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this OrmVolumeMountRequest.


        :param dataset: The dataset of this OrmVolumeMountRequest.  # noqa: E501
        :type dataset: OrmVolumeMountRequestSourceDataset
        """

        self._dataset = dataset

    @property
    def dataset_version(self):
        """Gets the dataset_version of this OrmVolumeMountRequest.  # noqa: E501


        :return: The dataset_version of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceDatasetVersion
        """
        return self._dataset_version

    @dataset_version.setter
    def dataset_version(self, dataset_version):
        """Sets the dataset_version of this OrmVolumeMountRequest.


        :param dataset_version: The dataset_version of this OrmVolumeMountRequest.  # noqa: E501
        :type dataset_version: OrmVolumeMountRequestSourceDatasetVersion
        """

        self._dataset_version = dataset_version

    @property
    def empty_dir(self):
        """Gets the empty_dir of this OrmVolumeMountRequest.  # noqa: E501


        :return: The empty_dir of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: object
        """
        return self._empty_dir

    @empty_dir.setter
    def empty_dir(self, empty_dir):
        """Sets the empty_dir of this OrmVolumeMountRequest.


        :param empty_dir: The empty_dir of this OrmVolumeMountRequest.  # noqa: E501
        :type empty_dir: object
        """

        self._empty_dir = empty_dir

    @property
    def model_volume(self):
        """Gets the model_volume of this OrmVolumeMountRequest.  # noqa: E501


        :return: The model_volume of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceModelVolume
        """
        return self._model_volume

    @model_volume.setter
    def model_volume(self, model_volume):
        """Sets the model_volume of this OrmVolumeMountRequest.


        :param model_volume: The model_volume of this OrmVolumeMountRequest.  # noqa: E501
        :type model_volume: OrmVolumeMountRequestSourceModelVolume
        """

        self._model_volume = model_volume

    @property
    def mount_path(self):
        """Gets the mount_path of this OrmVolumeMountRequest.  # noqa: E501


        :return: The mount_path of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this OrmVolumeMountRequest.


        :param mount_path: The mount_path of this OrmVolumeMountRequest.  # noqa: E501
        :type mount_path: str
        """
        if self.local_vars_configuration.client_side_validation and mount_path is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_path`, must not be `None`")  # noqa: E501

        self._mount_path = mount_path

    @property
    def object_storage(self):
        """Gets the object_storage of this OrmVolumeMountRequest.  # noqa: E501


        :return: The object_storage of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceObjectStorage
        """
        return self._object_storage

    @object_storage.setter
    def object_storage(self, object_storage):
        """Sets the object_storage of this OrmVolumeMountRequest.


        :param object_storage: The object_storage of this OrmVolumeMountRequest.  # noqa: E501
        :type object_storage: OrmVolumeMountRequestSourceObjectStorage
        """

        self._object_storage = object_storage

    @property
    def on_premise(self):
        """Gets the on_premise of this OrmVolumeMountRequest.  # noqa: E501


        :return: The on_premise of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmOnPremiseVolumeConfig
        """
        return self._on_premise

    @on_premise.setter
    def on_premise(self, on_premise):
        """Sets the on_premise of this OrmVolumeMountRequest.


        :param on_premise: The on_premise of this OrmVolumeMountRequest.  # noqa: E501
        :type on_premise: OrmOnPremiseVolumeConfig
        """

        self._on_premise = on_premise

    @property
    def output(self):
        """Gets the output of this OrmVolumeMountRequest.  # noqa: E501


        :return: The output of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this OrmVolumeMountRequest.


        :param output: The output of this OrmVolumeMountRequest.  # noqa: E501
        :type output: object
        """

        self._output = output

    @property
    def readonly(self):
        """Gets the readonly of this OrmVolumeMountRequest.  # noqa: E501


        :return: The readonly of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this OrmVolumeMountRequest.


        :param readonly: The readonly of this OrmVolumeMountRequest.  # noqa: E501
        :type readonly: bool
        """

        self._readonly = readonly

    @property
    def source_type(self):
        """Gets the source_type of this OrmVolumeMountRequest.  # noqa: E501


        :return: The source_type of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this OrmVolumeMountRequest.


        :param source_type: The source_type of this OrmVolumeMountRequest.  # noqa: E501
        :type source_type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501
        allowed_values = ["empty-dir", "code", "archive-file", "dataset", "dataset-version", "output", "volume", "on-premise", "model-volume", "object-storage"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and source_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def volume(self):
        """Gets the volume of this OrmVolumeMountRequest.  # noqa: E501


        :return: The volume of this OrmVolumeMountRequest.  # noqa: E501
        :rtype: OrmVolumeMountRequestSourceVolume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OrmVolumeMountRequest.


        :param volume: The volume of this OrmVolumeMountRequest.  # noqa: E501
        :type volume: OrmVolumeMountRequestSourceVolume
        """

        self._volume = volume

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
        if not isinstance(other, OrmVolumeMountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmVolumeMountRequest):
            return True

        return self.to_dict() != other.to_dict()
