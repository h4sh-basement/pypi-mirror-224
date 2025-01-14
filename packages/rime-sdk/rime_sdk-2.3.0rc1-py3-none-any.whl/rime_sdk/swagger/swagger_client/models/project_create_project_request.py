# coding: utf-8

"""
    Robust Intelligence REST API

    API methods for Robust Intelligence. Users must authenticate using the `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectCreateProjectRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'use_case': 'str',
        'ethical_consideration': 'str',
        'workspace_id': 'RimeUUID',
        'model_task': 'RimeModelTask',
        'tags': 'list[str]',
        'profiling_config': 'TestrunProfilingConfig',
        'is_published': 'bool',
        'run_time_info': 'RuntimeinfoRunTimeInfo'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'use_case': 'useCase',
        'ethical_consideration': 'ethicalConsideration',
        'workspace_id': 'workspaceId',
        'model_task': 'modelTask',
        'tags': 'tags',
        'profiling_config': 'profilingConfig',
        'is_published': 'isPublished',
        'run_time_info': 'runTimeInfo'
    }

    def __init__(self, name=None, description=None, use_case=None, ethical_consideration=None, workspace_id=None, model_task=None, tags=None, profiling_config=None, is_published=None, run_time_info=None):  # noqa: E501
        """ProjectCreateProjectRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._use_case = None
        self._ethical_consideration = None
        self._workspace_id = None
        self._model_task = None
        self._tags = None
        self._profiling_config = None
        self._is_published = None
        self._run_time_info = None
        self.discriminator = None
        self.name = name
        self.description = description
        if use_case is not None:
            self.use_case = use_case
        if ethical_consideration is not None:
            self.ethical_consideration = ethical_consideration
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if model_task is not None:
            self.model_task = model_task
        if tags is not None:
            self.tags = tags
        if profiling_config is not None:
            self.profiling_config = profiling_config
        if is_published is not None:
            self.is_published = is_published
        if run_time_info is not None:
            self.run_time_info = run_time_info

    @property
    def name(self):
        """Gets the name of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The name of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateProjectRequest.


        :param name: The name of this ProjectCreateProjectRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The description of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectCreateProjectRequest.


        :param description: The description of this ProjectCreateProjectRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def use_case(self):
        """Gets the use_case of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The use_case of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._use_case

    @use_case.setter
    def use_case(self, use_case):
        """Sets the use_case of this ProjectCreateProjectRequest.


        :param use_case: The use_case of this ProjectCreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._use_case = use_case

    @property
    def ethical_consideration(self):
        """Gets the ethical_consideration of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The ethical_consideration of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._ethical_consideration

    @ethical_consideration.setter
    def ethical_consideration(self, ethical_consideration):
        """Sets the ethical_consideration of this ProjectCreateProjectRequest.


        :param ethical_consideration: The ethical_consideration of this ProjectCreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._ethical_consideration = ethical_consideration

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The workspace_id of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: RimeUUID
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ProjectCreateProjectRequest.


        :param workspace_id: The workspace_id of this ProjectCreateProjectRequest.  # noqa: E501
        :type: RimeUUID
        """

        self._workspace_id = workspace_id

    @property
    def model_task(self):
        """Gets the model_task of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The model_task of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: RimeModelTask
        """
        return self._model_task

    @model_task.setter
    def model_task(self, model_task):
        """Sets the model_task of this ProjectCreateProjectRequest.


        :param model_task: The model_task of this ProjectCreateProjectRequest.  # noqa: E501
        :type: RimeModelTask
        """

        self._model_task = model_task

    @property
    def tags(self):
        """Gets the tags of this ProjectCreateProjectRequest.  # noqa: E501

        List of tags associated with the Project to help organizing Projects.  # noqa: E501

        :return: The tags of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProjectCreateProjectRequest.

        List of tags associated with the Project to help organizing Projects.  # noqa: E501

        :param tags: The tags of this ProjectCreateProjectRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def profiling_config(self):
        """Gets the profiling_config of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The profiling_config of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: TestrunProfilingConfig
        """
        return self._profiling_config

    @profiling_config.setter
    def profiling_config(self, profiling_config):
        """Sets the profiling_config of this ProjectCreateProjectRequest.


        :param profiling_config: The profiling_config of this ProjectCreateProjectRequest.  # noqa: E501
        :type: TestrunProfilingConfig
        """

        self._profiling_config = profiling_config

    @property
    def is_published(self):
        """Gets the is_published of this ProjectCreateProjectRequest.  # noqa: E501

        Published projects are shown on the Workspace overview page.  # noqa: E501

        :return: The is_published of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this ProjectCreateProjectRequest.

        Published projects are shown on the Workspace overview page.  # noqa: E501

        :param is_published: The is_published of this ProjectCreateProjectRequest.  # noqa: E501
        :type: bool
        """

        self._is_published = is_published

    @property
    def run_time_info(self):
        """Gets the run_time_info of this ProjectCreateProjectRequest.  # noqa: E501


        :return: The run_time_info of this ProjectCreateProjectRequest.  # noqa: E501
        :rtype: RuntimeinfoRunTimeInfo
        """
        return self._run_time_info

    @run_time_info.setter
    def run_time_info(self, run_time_info):
        """Sets the run_time_info of this ProjectCreateProjectRequest.


        :param run_time_info: The run_time_info of this ProjectCreateProjectRequest.  # noqa: E501
        :type: RuntimeinfoRunTimeInfo
        """

        self._run_time_info = run_time_info

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
        if issubclass(ProjectCreateProjectRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectCreateProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
