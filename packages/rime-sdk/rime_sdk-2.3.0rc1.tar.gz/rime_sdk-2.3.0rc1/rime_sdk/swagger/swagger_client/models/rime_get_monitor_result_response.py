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

class RimeGetMonitorResultResponse(object):
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
        'monitor_id': 'RimeUUID',
        'monitor_name': 'str',
        'metric_name': 'str',
        'threshold': 'MonitorThreshold',
        'data_points': 'list[RimeMonitorDataPoint]',
        'description_html': 'str',
        'long_description_tabs': 'list[RimeLongDescriptionTab]'
    }

    attribute_map = {
        'monitor_id': 'monitorId',
        'monitor_name': 'monitorName',
        'metric_name': 'metricName',
        'threshold': 'threshold',
        'data_points': 'dataPoints',
        'description_html': 'descriptionHtml',
        'long_description_tabs': 'longDescriptionTabs'
    }

    def __init__(self, monitor_id=None, monitor_name=None, metric_name=None, threshold=None, data_points=None, description_html=None, long_description_tabs=None):  # noqa: E501
        """RimeGetMonitorResultResponse - a model defined in Swagger"""  # noqa: E501
        self._monitor_id = None
        self._monitor_name = None
        self._metric_name = None
        self._threshold = None
        self._data_points = None
        self._description_html = None
        self._long_description_tabs = None
        self.discriminator = None
        if monitor_id is not None:
            self.monitor_id = monitor_id
        if monitor_name is not None:
            self.monitor_name = monitor_name
        if metric_name is not None:
            self.metric_name = metric_name
        if threshold is not None:
            self.threshold = threshold
        if data_points is not None:
            self.data_points = data_points
        if description_html is not None:
            self.description_html = description_html
        if long_description_tabs is not None:
            self.long_description_tabs = long_description_tabs

    @property
    def monitor_id(self):
        """Gets the monitor_id of this RimeGetMonitorResultResponse.  # noqa: E501


        :return: The monitor_id of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: RimeUUID
        """
        return self._monitor_id

    @monitor_id.setter
    def monitor_id(self, monitor_id):
        """Sets the monitor_id of this RimeGetMonitorResultResponse.


        :param monitor_id: The monitor_id of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: RimeUUID
        """

        self._monitor_id = monitor_id

    @property
    def monitor_name(self):
        """Gets the monitor_name of this RimeGetMonitorResultResponse.  # noqa: E501

        The name of the monitor.  # noqa: E501

        :return: The monitor_name of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._monitor_name

    @monitor_name.setter
    def monitor_name(self, monitor_name):
        """Sets the monitor_name of this RimeGetMonitorResultResponse.

        The name of the monitor.  # noqa: E501

        :param monitor_name: The monitor_name of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: str
        """

        self._monitor_name = monitor_name

    @property
    def metric_name(self):
        """Gets the metric_name of this RimeGetMonitorResultResponse.  # noqa: E501


        :return: The metric_name of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this RimeGetMonitorResultResponse.


        :param metric_name: The metric_name of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def threshold(self):
        """Gets the threshold of this RimeGetMonitorResultResponse.  # noqa: E501


        :return: The threshold of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: MonitorThreshold
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this RimeGetMonitorResultResponse.


        :param threshold: The threshold of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: MonitorThreshold
        """

        self._threshold = threshold

    @property
    def data_points(self):
        """Gets the data_points of this RimeGetMonitorResultResponse.  # noqa: E501

        The monitor data points.  # noqa: E501

        :return: The data_points of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: list[RimeMonitorDataPoint]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this RimeGetMonitorResultResponse.

        The monitor data points.  # noqa: E501

        :param data_points: The data_points of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: list[RimeMonitorDataPoint]
        """

        self._data_points = data_points

    @property
    def description_html(self):
        """Gets the description_html of this RimeGetMonitorResultResponse.  # noqa: E501

        Description of the monitor that may contain HTML.  # noqa: E501

        :return: The description_html of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._description_html

    @description_html.setter
    def description_html(self, description_html):
        """Sets the description_html of this RimeGetMonitorResultResponse.

        Description of the monitor that may contain HTML.  # noqa: E501

        :param description_html: The description_html of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: str
        """

        self._description_html = description_html

    @property
    def long_description_tabs(self):
        """Gets the long_description_tabs of this RimeGetMonitorResultResponse.  # noqa: E501

        More detailed information about the monitor.  # noqa: E501

        :return: The long_description_tabs of this RimeGetMonitorResultResponse.  # noqa: E501
        :rtype: list[RimeLongDescriptionTab]
        """
        return self._long_description_tabs

    @long_description_tabs.setter
    def long_description_tabs(self, long_description_tabs):
        """Sets the long_description_tabs of this RimeGetMonitorResultResponse.

        More detailed information about the monitor.  # noqa: E501

        :param long_description_tabs: The long_description_tabs of this RimeGetMonitorResultResponse.  # noqa: E501
        :type: list[RimeLongDescriptionTab]
        """

        self._long_description_tabs = long_description_tabs

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
        if issubclass(RimeGetMonitorResultResponse, dict):
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
        if not isinstance(other, RimeGetMonitorResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
