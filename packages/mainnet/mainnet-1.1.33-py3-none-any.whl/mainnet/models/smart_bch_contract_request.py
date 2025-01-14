# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.32
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractRequest(object):
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
        'address': 'str',
        'abi': 'list[str]'
    }

    attribute_map = {
        'address': 'address',
        'abi': 'abi'
    }

    def __init__(self, address=None, abi=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._abi = None
        self.discriminator = None

        self.address = address
        self.abi = abi

    @property
    def address(self):
        """Gets the address of this SmartBchContractRequest.  # noqa: E501

        Address of an already deployed contract  # noqa: E501

        :return: The address of this SmartBchContractRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SmartBchContractRequest.

        Address of an already deployed contract  # noqa: E501

        :param address: The address of this SmartBchContractRequest.  # noqa: E501
        :type address: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def abi(self):
        """Gets the abi of this SmartBchContractRequest.  # noqa: E501

        Contract ABI (Application Binary Interface), which describes the contract interaction  # noqa: E501

        :return: The abi of this SmartBchContractRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._abi

    @abi.setter
    def abi(self, abi):
        """Sets the abi of this SmartBchContractRequest.

        Contract ABI (Application Binary Interface), which describes the contract interaction  # noqa: E501

        :param abi: The abi of this SmartBchContractRequest.  # noqa: E501
        :type abi: list[str]
        """
        if self.local_vars_configuration.client_side_validation and abi is None:  # noqa: E501
            raise ValueError("Invalid value for `abi`, must not be `None`")  # noqa: E501

        self._abi = abi

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
        if not isinstance(other, SmartBchContractRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractRequest):
            return True

        return self.to_dict() != other.to_dict()
