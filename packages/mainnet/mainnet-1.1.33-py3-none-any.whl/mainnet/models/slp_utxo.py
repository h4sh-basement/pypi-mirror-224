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


class SlpUtxo(object):
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
        'index': 'float',
        'tx_id': 'str',
        'satoshis': 'float',
        'utxo_id': 'str',
        'value': 'str',
        'decimals': 'float',
        'ticker': 'str',
        'token_id': 'str',
        'type': 'float'
    }

    attribute_map = {
        'index': 'index',
        'tx_id': 'txId',
        'satoshis': 'satoshis',
        'utxo_id': 'utxoId',
        'value': 'value',
        'decimals': 'decimals',
        'ticker': 'ticker',
        'token_id': 'tokenId',
        'type': 'type'
    }

    def __init__(self, index=None, tx_id=None, satoshis=None, utxo_id=None, value=None, decimals=None, ticker=None, token_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SlpUtxo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._tx_id = None
        self._satoshis = None
        self._utxo_id = None
        self._value = None
        self._decimals = None
        self._ticker = None
        self._token_id = None
        self._type = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if tx_id is not None:
            self.tx_id = tx_id
        if satoshis is not None:
            self.satoshis = satoshis
        if utxo_id is not None:
            self.utxo_id = utxo_id
        if value is not None:
            self.value = value
        if decimals is not None:
            self.decimals = decimals
        if ticker is not None:
            self.ticker = ticker
        if token_id is not None:
            self.token_id = token_id
        if type is not None:
            self.type = type

    @property
    def index(self):
        """Gets the index of this SlpUtxo.  # noqa: E501


        :return: The index of this SlpUtxo.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this SlpUtxo.


        :param index: The index of this SlpUtxo.  # noqa: E501
        :type index: float
        """

        self._index = index

    @property
    def tx_id(self):
        """Gets the tx_id of this SlpUtxo.  # noqa: E501

        The hash of a transaction  # noqa: E501

        :return: The tx_id of this SlpUtxo.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this SlpUtxo.

        The hash of a transaction  # noqa: E501

        :param tx_id: The tx_id of this SlpUtxo.  # noqa: E501
        :type tx_id: str
        """

        self._tx_id = tx_id

    @property
    def satoshis(self):
        """Gets the satoshis of this SlpUtxo.  # noqa: E501

        Locked satoshi  # noqa: E501

        :return: The satoshis of this SlpUtxo.  # noqa: E501
        :rtype: float
        """
        return self._satoshis

    @satoshis.setter
    def satoshis(self, satoshis):
        """Sets the satoshis of this SlpUtxo.

        Locked satoshi  # noqa: E501

        :param satoshis: The satoshis of this SlpUtxo.  # noqa: E501
        :type satoshis: float
        """

        self._satoshis = satoshis

    @property
    def utxo_id(self):
        """Gets the utxo_id of this SlpUtxo.  # noqa: E501

        serialized outpoint  # noqa: E501

        :return: The utxo_id of this SlpUtxo.  # noqa: E501
        :rtype: str
        """
        return self._utxo_id

    @utxo_id.setter
    def utxo_id(self, utxo_id):
        """Sets the utxo_id of this SlpUtxo.

        serialized outpoint  # noqa: E501

        :param utxo_id: The utxo_id of this SlpUtxo.  # noqa: E501
        :type utxo_id: str
        """

        self._utxo_id = utxo_id

    @property
    def value(self):
        """Gets the value of this SlpUtxo.  # noqa: E501

        Token amount represented as a string to avoid precision loss  # noqa: E501

        :return: The value of this SlpUtxo.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SlpUtxo.

        Token amount represented as a string to avoid precision loss  # noqa: E501

        :param value: The value of this SlpUtxo.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def decimals(self):
        """Gets the decimals of this SlpUtxo.  # noqa: E501

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :return: The decimals of this SlpUtxo.  # noqa: E501
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SlpUtxo.

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :param decimals: The decimals of this SlpUtxo.  # noqa: E501
        :type decimals: float
        """

        self._decimals = decimals

    @property
    def ticker(self):
        """Gets the ticker of this SlpUtxo.  # noqa: E501

        Token ticker  # noqa: E501

        :return: The ticker of this SlpUtxo.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SlpUtxo.

        Token ticker  # noqa: E501

        :param ticker: The ticker of this SlpUtxo.  # noqa: E501
        :type ticker: str
        """

        self._ticker = ticker

    @property
    def token_id(self):
        """Gets the token_id of this SlpUtxo.  # noqa: E501

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :return: The token_id of this SlpUtxo.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SlpUtxo.

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :param token_id: The token_id of this SlpUtxo.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def type(self):
        """Gets the type of this SlpUtxo.  # noqa: E501

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :return: The type of this SlpUtxo.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlpUtxo.

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :param type: The type of this SlpUtxo.  # noqa: E501
        :type type: float
        """

        self._type = type

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
        if not isinstance(other, SlpUtxo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlpUtxo):
            return True

        return self.to_dict() != other.to_dict()
