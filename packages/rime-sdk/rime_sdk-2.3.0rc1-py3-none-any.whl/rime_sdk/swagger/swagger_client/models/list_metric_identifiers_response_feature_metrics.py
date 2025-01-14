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

class ListMetricIdentifiersResponseFeatureMetrics(object):
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
        'feature_metric_without_subsets': 'list[ListMetricIdentifiersResponseFeatureMetricWithoutSubsets]',
        'subset_metrics': 'dict(str, ListMetricIdentifiersResponseSubsetMetrics)'
    }

    attribute_map = {
        'feature_metric_without_subsets': 'featureMetricWithoutSubsets',
        'subset_metrics': 'subsetMetrics'
    }

    def __init__(self, feature_metric_without_subsets=None, subset_metrics=None):  # noqa: E501
        """ListMetricIdentifiersResponseFeatureMetrics - a model defined in Swagger"""  # noqa: E501
        self._feature_metric_without_subsets = None
        self._subset_metrics = None
        self.discriminator = None
        if feature_metric_without_subsets is not None:
            self.feature_metric_without_subsets = feature_metric_without_subsets
        if subset_metrics is not None:
            self.subset_metrics = subset_metrics

    @property
    def feature_metric_without_subsets(self):
        """Gets the feature_metric_without_subsets of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501


        :return: The feature_metric_without_subsets of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501
        :rtype: list[ListMetricIdentifiersResponseFeatureMetricWithoutSubsets]
        """
        return self._feature_metric_without_subsets

    @feature_metric_without_subsets.setter
    def feature_metric_without_subsets(self, feature_metric_without_subsets):
        """Sets the feature_metric_without_subsets of this ListMetricIdentifiersResponseFeatureMetrics.


        :param feature_metric_without_subsets: The feature_metric_without_subsets of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501
        :type: list[ListMetricIdentifiersResponseFeatureMetricWithoutSubsets]
        """

        self._feature_metric_without_subsets = feature_metric_without_subsets

    @property
    def subset_metrics(self):
        """Gets the subset_metrics of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501


        :return: The subset_metrics of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501
        :rtype: dict(str, ListMetricIdentifiersResponseSubsetMetrics)
        """
        return self._subset_metrics

    @subset_metrics.setter
    def subset_metrics(self, subset_metrics):
        """Sets the subset_metrics of this ListMetricIdentifiersResponseFeatureMetrics.


        :param subset_metrics: The subset_metrics of this ListMetricIdentifiersResponseFeatureMetrics.  # noqa: E501
        :type: dict(str, ListMetricIdentifiersResponseSubsetMetrics)
        """

        self._subset_metrics = subset_metrics

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
        if issubclass(ListMetricIdentifiersResponseFeatureMetrics, dict):
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
        if not isinstance(other, ListMetricIdentifiersResponseFeatureMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
