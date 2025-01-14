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


class OrmRunExecution(object):
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
        'arguments': 'dict[str, object]',
        'artifacts': 'dict[str, object]',
        'created_dt': 'datetime',
        'edges': 'OrmRunExecutionEdges',
        'exposed_services': 'dict[str, object]',
        'id': 'int',
        'immutable_slug': 'str',
        'local_experiment_id': 'int',
        'pipeline_step_execution_id': 'int',
        'run_spec_id': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'arguments': 'arguments',
        'artifacts': 'artifacts',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'exposed_services': 'exposed_services',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'local_experiment_id': 'local_experiment_id',
        'pipeline_step_execution_id': 'pipeline_step_execution_id',
        'run_spec_id': 'run_spec_id',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, arguments=None, artifacts=None, created_dt=None, edges=None, exposed_services=None, id=None, immutable_slug=None, local_experiment_id=None, pipeline_step_execution_id=None, run_spec_id=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmRunExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._arguments = None
        self._artifacts = None
        self._created_dt = None
        self._edges = None
        self._exposed_services = None
        self._id = None
        self._immutable_slug = None
        self._local_experiment_id = None
        self._pipeline_step_execution_id = None
        self._run_spec_id = None
        self._updated_dt = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if artifacts is not None:
            self.artifacts = artifacts
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if exposed_services is not None:
            self.exposed_services = exposed_services
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        self.local_experiment_id = local_experiment_id
        self.pipeline_step_execution_id = pipeline_step_execution_id
        if run_spec_id is not None:
            self.run_spec_id = run_spec_id
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def arguments(self):
        """Gets the arguments of this OrmRunExecution.  # noqa: E501


        :return: The arguments of this OrmRunExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this OrmRunExecution.


        :param arguments: The arguments of this OrmRunExecution.  # noqa: E501
        :type arguments: dict[str, object]
        """

        self._arguments = arguments

    @property
    def artifacts(self):
        """Gets the artifacts of this OrmRunExecution.  # noqa: E501


        :return: The artifacts of this OrmRunExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this OrmRunExecution.


        :param artifacts: The artifacts of this OrmRunExecution.  # noqa: E501
        :type artifacts: dict[str, object]
        """

        self._artifacts = artifacts

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmRunExecution.  # noqa: E501


        :return: The created_dt of this OrmRunExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmRunExecution.


        :param created_dt: The created_dt of this OrmRunExecution.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmRunExecution.  # noqa: E501


        :return: The edges of this OrmRunExecution.  # noqa: E501
        :rtype: OrmRunExecutionEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmRunExecution.


        :param edges: The edges of this OrmRunExecution.  # noqa: E501
        :type edges: OrmRunExecutionEdges
        """

        self._edges = edges

    @property
    def exposed_services(self):
        """Gets the exposed_services of this OrmRunExecution.  # noqa: E501


        :return: The exposed_services of this OrmRunExecution.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._exposed_services

    @exposed_services.setter
    def exposed_services(self, exposed_services):
        """Sets the exposed_services of this OrmRunExecution.


        :param exposed_services: The exposed_services of this OrmRunExecution.  # noqa: E501
        :type exposed_services: dict[str, object]
        """

        self._exposed_services = exposed_services

    @property
    def id(self):
        """Gets the id of this OrmRunExecution.  # noqa: E501


        :return: The id of this OrmRunExecution.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmRunExecution.


        :param id: The id of this OrmRunExecution.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmRunExecution.  # noqa: E501


        :return: The immutable_slug of this OrmRunExecution.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmRunExecution.


        :param immutable_slug: The immutable_slug of this OrmRunExecution.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def local_experiment_id(self):
        """Gets the local_experiment_id of this OrmRunExecution.  # noqa: E501


        :return: The local_experiment_id of this OrmRunExecution.  # noqa: E501
        :rtype: int
        """
        return self._local_experiment_id

    @local_experiment_id.setter
    def local_experiment_id(self, local_experiment_id):
        """Sets the local_experiment_id of this OrmRunExecution.


        :param local_experiment_id: The local_experiment_id of this OrmRunExecution.  # noqa: E501
        :type local_experiment_id: int
        """

        self._local_experiment_id = local_experiment_id

    @property
    def pipeline_step_execution_id(self):
        """Gets the pipeline_step_execution_id of this OrmRunExecution.  # noqa: E501


        :return: The pipeline_step_execution_id of this OrmRunExecution.  # noqa: E501
        :rtype: int
        """
        return self._pipeline_step_execution_id

    @pipeline_step_execution_id.setter
    def pipeline_step_execution_id(self, pipeline_step_execution_id):
        """Sets the pipeline_step_execution_id of this OrmRunExecution.


        :param pipeline_step_execution_id: The pipeline_step_execution_id of this OrmRunExecution.  # noqa: E501
        :type pipeline_step_execution_id: int
        """

        self._pipeline_step_execution_id = pipeline_step_execution_id

    @property
    def run_spec_id(self):
        """Gets the run_spec_id of this OrmRunExecution.  # noqa: E501


        :return: The run_spec_id of this OrmRunExecution.  # noqa: E501
        :rtype: int
        """
        return self._run_spec_id

    @run_spec_id.setter
    def run_spec_id(self, run_spec_id):
        """Sets the run_spec_id of this OrmRunExecution.


        :param run_spec_id: The run_spec_id of this OrmRunExecution.  # noqa: E501
        :type run_spec_id: int
        """

        self._run_spec_id = run_spec_id

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmRunExecution.  # noqa: E501


        :return: The updated_dt of this OrmRunExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmRunExecution.


        :param updated_dt: The updated_dt of this OrmRunExecution.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, OrmRunExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmRunExecution):
            return True

        return self.to_dict() != other.to_dict()
