# coding: utf-8

"""
    RIME Rest API

    API methods for RIME. Must be authenticated with `rime-api-key` header.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: dev@robustintelligence.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RimeJobMetadata(object):
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
        'job_id': 'str',
        'job_type': 'RimeJobType',
        'status': 'StatedbJobStatus',
        'start_time': 'datetime',
        'creation_time': 'datetime',
        'completion_time': 'datetime',
        'running_time_secs': 'float',
        'job_data': 'RimeJobData',
        'job_progress_str': 'str',
        'cancellation_requested': 'bool',
        'agent_id': 'RimeUUID',
        'archived_job_logs': 'StatedbArchivedJobLogs',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'job_type': 'jobType',
        'status': 'status',
        'start_time': 'startTime',
        'creation_time': 'creationTime',
        'completion_time': 'completionTime',
        'running_time_secs': 'runningTimeSecs',
        'job_data': 'jobData',
        'job_progress_str': 'jobProgressStr',
        'cancellation_requested': 'cancellationRequested',
        'agent_id': 'agentId',
        'archived_job_logs': 'archivedJobLogs',
        'error_msg': 'errorMsg'
    }

    def __init__(self, job_id=None, job_type=None, status=None, start_time=None, creation_time=None, completion_time=None, running_time_secs=None, job_data=None, job_progress_str=None, cancellation_requested=None, agent_id=None, archived_job_logs=None, error_msg=None):  # noqa: E501
        """RimeJobMetadata - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._job_type = None
        self._status = None
        self._start_time = None
        self._creation_time = None
        self._completion_time = None
        self._running_time_secs = None
        self._job_data = None
        self._job_progress_str = None
        self._cancellation_requested = None
        self._agent_id = None
        self._archived_job_logs = None
        self._error_msg = None
        self.discriminator = None
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if creation_time is not None:
            self.creation_time = creation_time
        if completion_time is not None:
            self.completion_time = completion_time
        if running_time_secs is not None:
            self.running_time_secs = running_time_secs
        if job_data is not None:
            self.job_data = job_data
        if job_progress_str is not None:
            self.job_progress_str = job_progress_str
        if cancellation_requested is not None:
            self.cancellation_requested = cancellation_requested
        if agent_id is not None:
            self.agent_id = agent_id
        if archived_job_logs is not None:
            self.archived_job_logs = archived_job_logs
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this RimeJobMetadata.  # noqa: E501

        The identifier within our job tracking system.  # noqa: E501

        :return: The job_id of this RimeJobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RimeJobMetadata.

        The identifier within our job tracking system.  # noqa: E501

        :param job_id: The job_id of this RimeJobMetadata.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this RimeJobMetadata.  # noqa: E501


        :return: The job_type of this RimeJobMetadata.  # noqa: E501
        :rtype: RimeJobType
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this RimeJobMetadata.


        :param job_type: The job_type of this RimeJobMetadata.  # noqa: E501
        :type: RimeJobType
        """

        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this RimeJobMetadata.  # noqa: E501


        :return: The status of this RimeJobMetadata.  # noqa: E501
        :rtype: StatedbJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RimeJobMetadata.


        :param status: The status of this RimeJobMetadata.  # noqa: E501
        :type: StatedbJobStatus
        """

        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this RimeJobMetadata.  # noqa: E501

        The start time of the job (when the job transitions in state to RUNNING). Note, this may not be populated immediately when the job is created.  # noqa: E501

        :return: The start_time of this RimeJobMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RimeJobMetadata.

        The start time of the job (when the job transitions in state to RUNNING). Note, this may not be populated immediately when the job is created.  # noqa: E501

        :param start_time: The start_time of this RimeJobMetadata.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def creation_time(self):
        """Gets the creation_time of this RimeJobMetadata.  # noqa: E501

        The time the job was created.  # noqa: E501

        :return: The creation_time of this RimeJobMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RimeJobMetadata.

        The time the job was created.  # noqa: E501

        :param creation_time: The creation_time of this RimeJobMetadata.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def completion_time(self):
        """Gets the completion_time of this RimeJobMetadata.  # noqa: E501

        The time the job entered a terminal state.  # noqa: E501

        :return: The completion_time of this RimeJobMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this RimeJobMetadata.

        The time the job entered a terminal state.  # noqa: E501

        :param completion_time: The completion_time of this RimeJobMetadata.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def running_time_secs(self):
        """Gets the running_time_secs of this RimeJobMetadata.  # noqa: E501

        The total running time a job took to complete if the job is finished or the current running time if the job is still in progress (seconds).  # noqa: E501

        :return: The running_time_secs of this RimeJobMetadata.  # noqa: E501
        :rtype: float
        """
        return self._running_time_secs

    @running_time_secs.setter
    def running_time_secs(self, running_time_secs):
        """Sets the running_time_secs of this RimeJobMetadata.

        The total running time a job took to complete if the job is finished or the current running time if the job is still in progress (seconds).  # noqa: E501

        :param running_time_secs: The running_time_secs of this RimeJobMetadata.  # noqa: E501
        :type: float
        """

        self._running_time_secs = running_time_secs

    @property
    def job_data(self):
        """Gets the job_data of this RimeJobMetadata.  # noqa: E501


        :return: The job_data of this RimeJobMetadata.  # noqa: E501
        :rtype: RimeJobData
        """
        return self._job_data

    @job_data.setter
    def job_data(self, job_data):
        """Sets the job_data of this RimeJobMetadata.


        :param job_data: The job_data of this RimeJobMetadata.  # noqa: E501
        :type: RimeJobData
        """

        self._job_data = job_data

    @property
    def job_progress_str(self):
        """Gets the job_progress_str of this RimeJobMetadata.  # noqa: E501

        Pretty-printed, human-readable representation of job progress. This will only be populated for Read methods with the FULL job view. To get schema for progress for each type of job, see the field inside that job's job data message (e.g. StressTestJobProgress). Note: this is unstable, do not rely on parsing this.  # noqa: E501

        :return: The job_progress_str of this RimeJobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._job_progress_str

    @job_progress_str.setter
    def job_progress_str(self, job_progress_str):
        """Sets the job_progress_str of this RimeJobMetadata.

        Pretty-printed, human-readable representation of job progress. This will only be populated for Read methods with the FULL job view. To get schema for progress for each type of job, see the field inside that job's job data message (e.g. StressTestJobProgress). Note: this is unstable, do not rely on parsing this.  # noqa: E501

        :param job_progress_str: The job_progress_str of this RimeJobMetadata.  # noqa: E501
        :type: str
        """

        self._job_progress_str = job_progress_str

    @property
    def cancellation_requested(self):
        """Gets the cancellation_requested of this RimeJobMetadata.  # noqa: E501

        Marked when the job has been requested to be cancelled by the user. This is declarative; once the user requests cancellation, the backend will conduct garbage collection on the job in the background and eventually update the status of the job to CANCELLED.  # noqa: E501

        :return: The cancellation_requested of this RimeJobMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._cancellation_requested

    @cancellation_requested.setter
    def cancellation_requested(self, cancellation_requested):
        """Sets the cancellation_requested of this RimeJobMetadata.

        Marked when the job has been requested to be cancelled by the user. This is declarative; once the user requests cancellation, the backend will conduct garbage collection on the job in the background and eventually update the status of the job to CANCELLED.  # noqa: E501

        :param cancellation_requested: The cancellation_requested of this RimeJobMetadata.  # noqa: E501
        :type: bool
        """

        self._cancellation_requested = cancellation_requested

    @property
    def agent_id(self):
        """Gets the agent_id of this RimeJobMetadata.  # noqa: E501


        :return: The agent_id of this RimeJobMetadata.  # noqa: E501
        :rtype: RimeUUID
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this RimeJobMetadata.


        :param agent_id: The agent_id of this RimeJobMetadata.  # noqa: E501
        :type: RimeUUID
        """

        self._agent_id = agent_id

    @property
    def archived_job_logs(self):
        """Gets the archived_job_logs of this RimeJobMetadata.  # noqa: E501


        :return: The archived_job_logs of this RimeJobMetadata.  # noqa: E501
        :rtype: StatedbArchivedJobLogs
        """
        return self._archived_job_logs

    @archived_job_logs.setter
    def archived_job_logs(self, archived_job_logs):
        """Sets the archived_job_logs of this RimeJobMetadata.


        :param archived_job_logs: The archived_job_logs of this RimeJobMetadata.  # noqa: E501
        :type: StatedbArchivedJobLogs
        """

        self._archived_job_logs = archived_job_logs

    @property
    def error_msg(self):
        """Gets the error_msg of this RimeJobMetadata.  # noqa: E501

        User-facing error message for the job.  # noqa: E501

        :return: The error_msg of this RimeJobMetadata.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RimeJobMetadata.

        User-facing error message for the job.  # noqa: E501

        :param error_msg: The error_msg of this RimeJobMetadata.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

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
        if issubclass(RimeJobMetadata, dict):
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
        if not isinstance(other, RimeJobMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
