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


class SlpGenesisRequest(object):
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
        'wallet_id': 'str',
        'name': 'str',
        'ticker': 'str',
        'initial_amount': 'str',
        'decimals': 'float',
        'document_url': 'str',
        'document_hash': 'str',
        'end_baton': 'bool',
        'type': 'float',
        'token_receiver_slp_addr': 'str',
        'baton_receiver_slp_addr': 'str',
        'parent_token_id': 'str'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'name': 'name',
        'ticker': 'ticker',
        'initial_amount': 'initialAmount',
        'decimals': 'decimals',
        'document_url': 'documentUrl',
        'document_hash': 'documentHash',
        'end_baton': 'endBaton',
        'type': 'type',
        'token_receiver_slp_addr': 'tokenReceiverSlpAddr',
        'baton_receiver_slp_addr': 'batonReceiverSlpAddr',
        'parent_token_id': 'parentTokenId'
    }

    def __init__(self, wallet_id=None, name=None, ticker=None, initial_amount=None, decimals=None, document_url=None, document_hash=None, end_baton=None, type=None, token_receiver_slp_addr=None, baton_receiver_slp_addr=None, parent_token_id=None, local_vars_configuration=None):  # noqa: E501
        """SlpGenesisRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._name = None
        self._ticker = None
        self._initial_amount = None
        self._decimals = None
        self._document_url = None
        self._document_hash = None
        self._end_baton = None
        self._type = None
        self._token_receiver_slp_addr = None
        self._baton_receiver_slp_addr = None
        self._parent_token_id = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.name = name
        self.ticker = ticker
        self.initial_amount = initial_amount
        self.decimals = decimals
        if document_url is not None:
            self.document_url = document_url
        if document_hash is not None:
            self.document_hash = document_hash
        if end_baton is not None:
            self.end_baton = end_baton
        if type is not None:
            self.type = type
        if token_receiver_slp_addr is not None:
            self.token_receiver_slp_addr = token_receiver_slp_addr
        if baton_receiver_slp_addr is not None:
            self.baton_receiver_slp_addr = baton_receiver_slp_addr
        if parent_token_id is not None:
            self.parent_token_id = parent_token_id

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SlpGenesisRequest.  # noqa: E501

        ID that is returned in `wallet` field of /wallet call   # noqa: E501

        :return: The wallet_id of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SlpGenesisRequest.

        ID that is returned in `wallet` field of /wallet call   # noqa: E501

        :param wallet_id: The wallet_id of this SlpGenesisRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def name(self):
        """Gets the name of this SlpGenesisRequest.  # noqa: E501

        Token name  # noqa: E501

        :return: The name of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlpGenesisRequest.

        Token name  # noqa: E501

        :param name: The name of this SlpGenesisRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this SlpGenesisRequest.  # noqa: E501

        Token ticker  # noqa: E501

        :return: The ticker of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SlpGenesisRequest.

        Token ticker  # noqa: E501

        :param ticker: The ticker of this SlpGenesisRequest.  # noqa: E501
        :type ticker: str
        """
        if self.local_vars_configuration.client_side_validation and ticker is None:  # noqa: E501
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def initial_amount(self):
        """Gets the initial_amount of this SlpGenesisRequest.  # noqa: E501

        Value is represented as a string to avoid precision loss  # noqa: E501

        :return: The initial_amount of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._initial_amount

    @initial_amount.setter
    def initial_amount(self, initial_amount):
        """Sets the initial_amount of this SlpGenesisRequest.

        Value is represented as a string to avoid precision loss  # noqa: E501

        :param initial_amount: The initial_amount of this SlpGenesisRequest.  # noqa: E501
        :type initial_amount: str
        """
        if self.local_vars_configuration.client_side_validation and initial_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_amount`, must not be `None`")  # noqa: E501

        self._initial_amount = initial_amount

    @property
    def decimals(self):
        """Gets the decimals of this SlpGenesisRequest.  # noqa: E501

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :return: The decimals of this SlpGenesisRequest.  # noqa: E501
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SlpGenesisRequest.

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :param decimals: The decimals of this SlpGenesisRequest.  # noqa: E501
        :type decimals: float
        """
        if self.local_vars_configuration.client_side_validation and decimals is None:  # noqa: E501
            raise ValueError("Invalid value for `decimals`, must not be `None`")  # noqa: E501

        self._decimals = decimals

    @property
    def document_url(self):
        """Gets the document_url of this SlpGenesisRequest.  # noqa: E501


        :return: The document_url of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """Sets the document_url of this SlpGenesisRequest.


        :param document_url: The document_url of this SlpGenesisRequest.  # noqa: E501
        :type document_url: str
        """

        self._document_url = document_url

    @property
    def document_hash(self):
        """Gets the document_hash of this SlpGenesisRequest.  # noqa: E501

        Document hash of the token. Empty or 64 character long hex string.  # noqa: E501

        :return: The document_hash of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._document_hash

    @document_hash.setter
    def document_hash(self, document_hash):
        """Sets the document_hash of this SlpGenesisRequest.

        Document hash of the token. Empty or 64 character long hex string.  # noqa: E501

        :param document_hash: The document_hash of this SlpGenesisRequest.  # noqa: E501
        :type document_hash: str
        """

        self._document_hash = document_hash

    @property
    def end_baton(self):
        """Gets the end_baton of this SlpGenesisRequest.  # noqa: E501

        Indicates if token should not be 'mintable', e.g. total circulation amount increased  # noqa: E501

        :return: The end_baton of this SlpGenesisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._end_baton

    @end_baton.setter
    def end_baton(self, end_baton):
        """Sets the end_baton of this SlpGenesisRequest.

        Indicates if token should not be 'mintable', e.g. total circulation amount increased  # noqa: E501

        :param end_baton: The end_baton of this SlpGenesisRequest.  # noqa: E501
        :type end_baton: bool
        """

        self._end_baton = end_baton

    @property
    def type(self):
        """Gets the type of this SlpGenesisRequest.  # noqa: E501

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :return: The type of this SlpGenesisRequest.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlpGenesisRequest.

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :param type: The type of this SlpGenesisRequest.  # noqa: E501
        :type type: float
        """

        self._type = type

    @property
    def token_receiver_slp_addr(self):
        """Gets the token_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501


        :return: The token_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_receiver_slp_addr

    @token_receiver_slp_addr.setter
    def token_receiver_slp_addr(self, token_receiver_slp_addr):
        """Sets the token_receiver_slp_addr of this SlpGenesisRequest.


        :param token_receiver_slp_addr: The token_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501
        :type token_receiver_slp_addr: str
        """

        self._token_receiver_slp_addr = token_receiver_slp_addr

    @property
    def baton_receiver_slp_addr(self):
        """Gets the baton_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501


        :return: The baton_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._baton_receiver_slp_addr

    @baton_receiver_slp_addr.setter
    def baton_receiver_slp_addr(self, baton_receiver_slp_addr):
        """Sets the baton_receiver_slp_addr of this SlpGenesisRequest.


        :param baton_receiver_slp_addr: The baton_receiver_slp_addr of this SlpGenesisRequest.  # noqa: E501
        :type baton_receiver_slp_addr: str
        """

        self._baton_receiver_slp_addr = baton_receiver_slp_addr

    @property
    def parent_token_id(self):
        """Gets the parent_token_id of this SlpGenesisRequest.  # noqa: E501

        Identifier of the NFT parent token  # noqa: E501

        :return: The parent_token_id of this SlpGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_token_id

    @parent_token_id.setter
    def parent_token_id(self, parent_token_id):
        """Sets the parent_token_id of this SlpGenesisRequest.

        Identifier of the NFT parent token  # noqa: E501

        :param parent_token_id: The parent_token_id of this SlpGenesisRequest.  # noqa: E501
        :type parent_token_id: str
        """

        self._parent_token_id = parent_token_id

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
        if not isinstance(other, SlpGenesisRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlpGenesisRequest):
            return True

        return self.to_dict() != other.to_dict()
