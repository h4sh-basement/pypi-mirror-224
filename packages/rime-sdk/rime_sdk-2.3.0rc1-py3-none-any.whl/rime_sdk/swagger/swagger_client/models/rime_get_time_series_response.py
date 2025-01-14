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

class RimeGetTimeSeriesResponse(object):
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
        'project_id': 'RimeUUID',
        'time_series_name': 'str',
        'y_axis_label': 'str',
        'threshold': 'MonitorThreshold',
        'data_points': 'list[RimeMonitorDataPoint]',
        'description_html': 'str',
        'long_description_tabs': 'list[RimeLongDescriptionTab]'
    }

    attribute_map = {
        'project_id': 'projectId',
        'time_series_name': 'timeSeriesName',
        'y_axis_label': 'yAxisLabel',
        'threshold': 'threshold',
        'data_points': 'dataPoints',
        'description_html': 'descriptionHtml',
        'long_description_tabs': 'longDescriptionTabs'
    }

    def __init__(self, project_id=None, time_series_name=None, y_axis_label=None, threshold=None, data_points=None, description_html=None, long_description_tabs=None):  # noqa: E501
        """RimeGetTimeSeriesResponse - a model defined in Swagger"""  # noqa: E501
        self._project_id = None
        self._time_series_name = None
        self._y_axis_label = None
        self._threshold = None
        self._data_points = None
        self._description_html = None
        self._long_description_tabs = None
        self.discriminator = None
        if project_id is not None:
            self.project_id = project_id
        if time_series_name is not None:
            self.time_series_name = time_series_name
        if y_axis_label is not None:
            self.y_axis_label = y_axis_label
        if threshold is not None:
            self.threshold = threshold
        if data_points is not None:
            self.data_points = data_points
        if description_html is not None:
            self.description_html = description_html
        if long_description_tabs is not None:
            self.long_description_tabs = long_description_tabs

    @property
    def project_id(self):
        """Gets the project_id of this RimeGetTimeSeriesResponse.  # noqa: E501


        :return: The project_id of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: RimeUUID
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RimeGetTimeSeriesResponse.


        :param project_id: The project_id of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: RimeUUID
        """

        self._project_id = project_id

    @property
    def time_series_name(self):
        """Gets the time_series_name of this RimeGetTimeSeriesResponse.  # noqa: E501

        The name of the time series.  # noqa: E501

        :return: The time_series_name of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._time_series_name

    @time_series_name.setter
    def time_series_name(self, time_series_name):
        """Sets the time_series_name of this RimeGetTimeSeriesResponse.

        The name of the time series.  # noqa: E501

        :param time_series_name: The time_series_name of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: str
        """

        self._time_series_name = time_series_name

    @property
    def y_axis_label(self):
        """Gets the y_axis_label of this RimeGetTimeSeriesResponse.  # noqa: E501


        :return: The y_axis_label of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._y_axis_label

    @y_axis_label.setter
    def y_axis_label(self, y_axis_label):
        """Sets the y_axis_label of this RimeGetTimeSeriesResponse.


        :param y_axis_label: The y_axis_label of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: str
        """

        self._y_axis_label = y_axis_label

    @property
    def threshold(self):
        """Gets the threshold of this RimeGetTimeSeriesResponse.  # noqa: E501


        :return: The threshold of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: MonitorThreshold
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this RimeGetTimeSeriesResponse.


        :param threshold: The threshold of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: MonitorThreshold
        """

        self._threshold = threshold

    @property
    def data_points(self):
        """Gets the data_points of this RimeGetTimeSeriesResponse.  # noqa: E501

        The monitor data points.  # noqa: E501

        :return: The data_points of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: list[RimeMonitorDataPoint]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this RimeGetTimeSeriesResponse.

        The monitor data points.  # noqa: E501

        :param data_points: The data_points of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: list[RimeMonitorDataPoint]
        """

        self._data_points = data_points

    @property
    def description_html(self):
        """Gets the description_html of this RimeGetTimeSeriesResponse.  # noqa: E501

        Description of the time series that may contain HTML.  # noqa: E501

        :return: The description_html of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description_html

    @description_html.setter
    def description_html(self, description_html):
        """Sets the description_html of this RimeGetTimeSeriesResponse.

        Description of the time series that may contain HTML.  # noqa: E501

        :param description_html: The description_html of this RimeGetTimeSeriesResponse.  # noqa: E501
        :type: str
        """

        self._description_html = description_html

    @property
    def long_description_tabs(self):
        """Gets the long_description_tabs of this RimeGetTimeSeriesResponse.  # noqa: E501

        More detailed information about the time series.  # noqa: E501

        :return: The long_description_tabs of this RimeGetTimeSeriesResponse.  # noqa: E501
        :rtype: list[RimeLongDescriptionTab]
        """
        return self._long_description_tabs

    @long_description_tabs.setter
    def long_description_tabs(self, long_description_tabs):
        """Sets the long_description_tabs of this RimeGetTimeSeriesResponse.

        More detailed information about the time series.  # noqa: E501

        :param long_description_tabs: The long_description_tabs of this RimeGetTimeSeriesResponse.  # noqa: E501
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
        if issubclass(RimeGetTimeSeriesResponse, dict):
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
        if not isinstance(other, RimeGetTimeSeriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
