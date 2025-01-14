# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.819
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_scheduler.configuration import Configuration


class ScanSummary(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'fixable': 'int',
        'total': 'int',
        'critical': 'int',
        'high': 'int',
        'medium': 'int',
        'low': 'int',
        'negligible': 'int',
        'unknown': 'int'
    }

    attribute_map = {
        'fixable': 'fixable',
        'total': 'total',
        'critical': 'critical',
        'high': 'high',
        'medium': 'medium',
        'low': 'low',
        'negligible': 'negligible',
        'unknown': 'unknown'
    }

    required_map = {
        'fixable': 'optional',
        'total': 'optional',
        'critical': 'optional',
        'high': 'optional',
        'medium': 'optional',
        'low': 'optional',
        'negligible': 'optional',
        'unknown': 'optional'
    }

    def __init__(self, fixable=None, total=None, critical=None, high=None, medium=None, low=None, negligible=None, unknown=None, local_vars_configuration=None):  # noqa: E501
        """ScanSummary - a model defined in OpenAPI"
        
        :param fixable:  The number of vulnerabilities that have a known fix
        :type fixable: int
        :param total:  The total number of vulnerabilities
        :type total: int
        :param critical:  The number of Critical severity vulnerabilities
        :type critical: int
        :param high:  The number of High severity vulnerabilities
        :type high: int
        :param medium:  The number of Medium severity vulnerabilities
        :type medium: int
        :param low:  The number of Low severity vulnerabilities
        :type low: int
        :param negligible:  The number of Negligible severity vulnerabilities
        :type negligible: int
        :param unknown:  The number of Unknown severity vulnerabilities
        :type unknown: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fixable = None
        self._total = None
        self._critical = None
        self._high = None
        self._medium = None
        self._low = None
        self._negligible = None
        self._unknown = None
        self.discriminator = None

        self.fixable = fixable
        self.total = total
        self.critical = critical
        self.high = high
        self.medium = medium
        self.low = low
        self.negligible = negligible
        self.unknown = unknown

    @property
    def fixable(self):
        """Gets the fixable of this ScanSummary.  # noqa: E501

        The number of vulnerabilities that have a known fix  # noqa: E501

        :return: The fixable of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._fixable

    @fixable.setter
    def fixable(self, fixable):
        """Sets the fixable of this ScanSummary.

        The number of vulnerabilities that have a known fix  # noqa: E501

        :param fixable: The fixable of this ScanSummary.  # noqa: E501
        :type fixable: int
        """

        self._fixable = fixable

    @property
    def total(self):
        """Gets the total of this ScanSummary.  # noqa: E501

        The total number of vulnerabilities  # noqa: E501

        :return: The total of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScanSummary.

        The total number of vulnerabilities  # noqa: E501

        :param total: The total of this ScanSummary.  # noqa: E501
        :type total: int
        """

        self._total = total

    @property
    def critical(self):
        """Gets the critical of this ScanSummary.  # noqa: E501

        The number of Critical severity vulnerabilities  # noqa: E501

        :return: The critical of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this ScanSummary.

        The number of Critical severity vulnerabilities  # noqa: E501

        :param critical: The critical of this ScanSummary.  # noqa: E501
        :type critical: int
        """

        self._critical = critical

    @property
    def high(self):
        """Gets the high of this ScanSummary.  # noqa: E501

        The number of High severity vulnerabilities  # noqa: E501

        :return: The high of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this ScanSummary.

        The number of High severity vulnerabilities  # noqa: E501

        :param high: The high of this ScanSummary.  # noqa: E501
        :type high: int
        """

        self._high = high

    @property
    def medium(self):
        """Gets the medium of this ScanSummary.  # noqa: E501

        The number of Medium severity vulnerabilities  # noqa: E501

        :return: The medium of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this ScanSummary.

        The number of Medium severity vulnerabilities  # noqa: E501

        :param medium: The medium of this ScanSummary.  # noqa: E501
        :type medium: int
        """

        self._medium = medium

    @property
    def low(self):
        """Gets the low of this ScanSummary.  # noqa: E501

        The number of Low severity vulnerabilities  # noqa: E501

        :return: The low of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this ScanSummary.

        The number of Low severity vulnerabilities  # noqa: E501

        :param low: The low of this ScanSummary.  # noqa: E501
        :type low: int
        """

        self._low = low

    @property
    def negligible(self):
        """Gets the negligible of this ScanSummary.  # noqa: E501

        The number of Negligible severity vulnerabilities  # noqa: E501

        :return: The negligible of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._negligible

    @negligible.setter
    def negligible(self, negligible):
        """Sets the negligible of this ScanSummary.

        The number of Negligible severity vulnerabilities  # noqa: E501

        :param negligible: The negligible of this ScanSummary.  # noqa: E501
        :type negligible: int
        """

        self._negligible = negligible

    @property
    def unknown(self):
        """Gets the unknown of this ScanSummary.  # noqa: E501

        The number of Unknown severity vulnerabilities  # noqa: E501

        :return: The unknown of this ScanSummary.  # noqa: E501
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this ScanSummary.

        The number of Unknown severity vulnerabilities  # noqa: E501

        :param unknown: The unknown of this ScanSummary.  # noqa: E501
        :type unknown: int
        """

        self._unknown = unknown

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
        if not isinstance(other, ScanSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanSummary):
            return True

        return self.to_dict() != other.to_dict()
