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


class PeerInfo(object):
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
        'node_name': 'str',
        'peer_addr': 'str',
        'node_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'node_name': 'nodeName',
        'peer_addr': 'peerAddr',
        'node_id': 'nodeId',
        'tags': 'tags'
    }

    def __init__(self, node_name=None, peer_addr=None, node_id=None, tags=None):  # noqa: E501
        """PeerInfo - a model defined in OpenAPI"""  # noqa: E501

        self._node_name = None
        self._peer_addr = None
        self._node_id = None
        self._tags = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        self.peer_addr = peer_addr
        if node_id is not None:
            self.node_id = node_id
        if tags is not None:
            self.tags = tags

    @property
    def node_name(self):
        """Gets the node_name of this PeerInfo.  # noqa: E501

        Node name or hostname from reverse dns if node name is not set  # noqa: E501

        :return: The node_name of this PeerInfo.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this PeerInfo.

        Node name or hostname from reverse dns if node name is not set  # noqa: E501

        :param node_name: The node_name of this PeerInfo.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def peer_addr(self):
        """Gets the peer_addr of this PeerInfo.  # noqa: E501

        node address from current connection formated as <ip-addr>:<port>  # noqa: E501

        :return: The peer_addr of this PeerInfo.  # noqa: E501
        :rtype: str
        """
        return self._peer_addr

    @peer_addr.setter
    def peer_addr(self, peer_addr):
        """Sets the peer_addr of this PeerInfo.

        node address from current connection formated as <ip-addr>:<port>  # noqa: E501

        :param peer_addr: The peer_addr of this PeerInfo.  # noqa: E501
        :type: str
        """
        if peer_addr is None:
            raise ValueError("Invalid value for `peer_addr`, must not be `None`")  # noqa: E501

        self._peer_addr = peer_addr

    @property
    def node_id(self):
        """Gets the node_id of this PeerInfo.  # noqa: E501

        node public key hash in etherium format  # noqa: E501

        :return: The node_id of this PeerInfo.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PeerInfo.

        node public key hash in etherium format  # noqa: E501

        :param node_id: The node_id of this PeerInfo.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def tags(self):
        """Gets the tags of this PeerInfo.  # noqa: E501


        :return: The tags of this PeerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PeerInfo.


        :param tags: The tags of this PeerInfo.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, PeerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other