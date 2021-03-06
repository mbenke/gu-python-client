# coding: utf-8

"""
    Golem unlimited low level hub API

    API description in Markdown.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class HubSessionCommand(object):
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
        'command_type': 'str',
        'ts': 'datetime'
    }

    attribute_map = {
        'command_type': 'commandType',
        'ts': 'ts'
    }

    discriminator_value_class_map = {
        'HubSessionTouchCommand': 'HubSessionTouchCommand'
    }

    def __init__(self, command_type=None, ts=None):  # noqa: E501
        """HubSessionCommand - a model defined in OpenAPI"""  # noqa: E501

        self._command_type = None
        self._ts = None
        self.discriminator = 'command_type'

        self.command_type = command_type
        if ts is not None:
            self.ts = ts

    @property
    def command_type(self):
        """Gets the command_type of this HubSessionCommand.  # noqa: E501


        :return: The command_type of this HubSessionCommand.  # noqa: E501
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this HubSessionCommand.


        :param command_type: The command_type of this HubSessionCommand.  # noqa: E501
        :type: str
        """
        if command_type is None:
            raise ValueError("Invalid value for `command_type`, must not be `None`")  # noqa: E501

        self._command_type = command_type

    @property
    def ts(self):
        """Gets the ts of this HubSessionCommand.  # noqa: E501


        :return: The ts of this HubSessionCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this HubSessionCommand.


        :param ts: The ts of this HubSessionCommand.  # noqa: E501
        :type: datetime
        """

        self._ts = ts

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HubSessionCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
