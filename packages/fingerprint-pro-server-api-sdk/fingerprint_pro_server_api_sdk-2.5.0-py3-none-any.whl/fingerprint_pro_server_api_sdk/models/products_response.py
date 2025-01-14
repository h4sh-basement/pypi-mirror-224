# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductsResponse(object):
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
        'identification': 'ProductsResponseIdentification',
        'botd': 'ProductsResponseBotd',
        'ip_info': 'SignalResponseIpInfo',
        'incognito': 'SignalResponseIncognito',
        'root_apps': 'SignalResponseRootApps',
        'emulator': 'SignalResponseEmulator',
        'cloned_app': 'SignalResponseClonedApp',
        'factory_reset': 'SignalResponseFactoryReset',
        'jailbroken': 'SignalResponseJailbroken',
        'frida': 'SignalResponseFrida',
        'ip_blocklist': 'SignalResponseIpBlocklist',
        'tor': 'SignalResponseTor',
        'privacy_settings': 'SignalResponsePrivacySettings',
        'virtual_machine': 'SignalResponseVirtualMachine',
        'vpn': 'SignalResponseVpn',
        'proxy': 'SignalResponseProxy',
        'tampering': 'SignalResponseTampering',
        'raw_device_attributes': 'SignalResponseRawDeviceAttributes'
    }

    attribute_map = {
        'identification': 'identification',
        'botd': 'botd',
        'ip_info': 'ipInfo',
        'incognito': 'incognito',
        'root_apps': 'rootApps',
        'emulator': 'emulator',
        'cloned_app': 'clonedApp',
        'factory_reset': 'factoryReset',
        'jailbroken': 'jailbroken',
        'frida': 'frida',
        'ip_blocklist': 'ipBlocklist',
        'tor': 'tor',
        'privacy_settings': 'privacySettings',
        'virtual_machine': 'virtualMachine',
        'vpn': 'vpn',
        'proxy': 'proxy',
        'tampering': 'tampering',
        'raw_device_attributes': 'rawDeviceAttributes'
    }

    def __init__(self, identification=None, botd=None, ip_info=None, incognito=None, root_apps=None, emulator=None, cloned_app=None, factory_reset=None, jailbroken=None, frida=None, ip_blocklist=None, tor=None, privacy_settings=None, virtual_machine=None, vpn=None, proxy=None, tampering=None, raw_device_attributes=None):  # noqa: E501
        """ProductsResponse - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._botd = None
        self._ip_info = None
        self._incognito = None
        self._root_apps = None
        self._emulator = None
        self._cloned_app = None
        self._factory_reset = None
        self._jailbroken = None
        self._frida = None
        self._ip_blocklist = None
        self._tor = None
        self._privacy_settings = None
        self._virtual_machine = None
        self._vpn = None
        self._proxy = None
        self._tampering = None
        self._raw_device_attributes = None
        self.discriminator = None
        if identification is not None:
            self.identification = identification
        if botd is not None:
            self.botd = botd
        if ip_info is not None:
            self.ip_info = ip_info
        if incognito is not None:
            self.incognito = incognito
        if root_apps is not None:
            self.root_apps = root_apps
        if emulator is not None:
            self.emulator = emulator
        if cloned_app is not None:
            self.cloned_app = cloned_app
        if factory_reset is not None:
            self.factory_reset = factory_reset
        if jailbroken is not None:
            self.jailbroken = jailbroken
        if frida is not None:
            self.frida = frida
        if ip_blocklist is not None:
            self.ip_blocklist = ip_blocklist
        if tor is not None:
            self.tor = tor
        if privacy_settings is not None:
            self.privacy_settings = privacy_settings
        if virtual_machine is not None:
            self.virtual_machine = virtual_machine
        if vpn is not None:
            self.vpn = vpn
        if proxy is not None:
            self.proxy = proxy
        if tampering is not None:
            self.tampering = tampering
        if raw_device_attributes is not None:
            self.raw_device_attributes = raw_device_attributes

    @property
    def identification(self):
        """Gets the identification of this ProductsResponse.  # noqa: E501


        :return: The identification of this ProductsResponse.  # noqa: E501
        :rtype: ProductsResponseIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this ProductsResponse.


        :param identification: The identification of this ProductsResponse.  # noqa: E501
        :type: ProductsResponseIdentification
        """

        self._identification = identification

    @property
    def botd(self):
        """Gets the botd of this ProductsResponse.  # noqa: E501


        :return: The botd of this ProductsResponse.  # noqa: E501
        :rtype: ProductsResponseBotd
        """
        return self._botd

    @botd.setter
    def botd(self, botd):
        """Sets the botd of this ProductsResponse.


        :param botd: The botd of this ProductsResponse.  # noqa: E501
        :type: ProductsResponseBotd
        """

        self._botd = botd

    @property
    def ip_info(self):
        """Gets the ip_info of this ProductsResponse.  # noqa: E501


        :return: The ip_info of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseIpInfo
        """
        return self._ip_info

    @ip_info.setter
    def ip_info(self, ip_info):
        """Sets the ip_info of this ProductsResponse.


        :param ip_info: The ip_info of this ProductsResponse.  # noqa: E501
        :type: SignalResponseIpInfo
        """

        self._ip_info = ip_info

    @property
    def incognito(self):
        """Gets the incognito of this ProductsResponse.  # noqa: E501


        :return: The incognito of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseIncognito
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito):
        """Sets the incognito of this ProductsResponse.


        :param incognito: The incognito of this ProductsResponse.  # noqa: E501
        :type: SignalResponseIncognito
        """

        self._incognito = incognito

    @property
    def root_apps(self):
        """Gets the root_apps of this ProductsResponse.  # noqa: E501


        :return: The root_apps of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseRootApps
        """
        return self._root_apps

    @root_apps.setter
    def root_apps(self, root_apps):
        """Sets the root_apps of this ProductsResponse.


        :param root_apps: The root_apps of this ProductsResponse.  # noqa: E501
        :type: SignalResponseRootApps
        """

        self._root_apps = root_apps

    @property
    def emulator(self):
        """Gets the emulator of this ProductsResponse.  # noqa: E501


        :return: The emulator of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseEmulator
        """
        return self._emulator

    @emulator.setter
    def emulator(self, emulator):
        """Sets the emulator of this ProductsResponse.


        :param emulator: The emulator of this ProductsResponse.  # noqa: E501
        :type: SignalResponseEmulator
        """

        self._emulator = emulator

    @property
    def cloned_app(self):
        """Gets the cloned_app of this ProductsResponse.  # noqa: E501


        :return: The cloned_app of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseClonedApp
        """
        return self._cloned_app

    @cloned_app.setter
    def cloned_app(self, cloned_app):
        """Sets the cloned_app of this ProductsResponse.


        :param cloned_app: The cloned_app of this ProductsResponse.  # noqa: E501
        :type: SignalResponseClonedApp
        """

        self._cloned_app = cloned_app

    @property
    def factory_reset(self):
        """Gets the factory_reset of this ProductsResponse.  # noqa: E501


        :return: The factory_reset of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseFactoryReset
        """
        return self._factory_reset

    @factory_reset.setter
    def factory_reset(self, factory_reset):
        """Sets the factory_reset of this ProductsResponse.


        :param factory_reset: The factory_reset of this ProductsResponse.  # noqa: E501
        :type: SignalResponseFactoryReset
        """

        self._factory_reset = factory_reset

    @property
    def jailbroken(self):
        """Gets the jailbroken of this ProductsResponse.  # noqa: E501


        :return: The jailbroken of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseJailbroken
        """
        return self._jailbroken

    @jailbroken.setter
    def jailbroken(self, jailbroken):
        """Sets the jailbroken of this ProductsResponse.


        :param jailbroken: The jailbroken of this ProductsResponse.  # noqa: E501
        :type: SignalResponseJailbroken
        """

        self._jailbroken = jailbroken

    @property
    def frida(self):
        """Gets the frida of this ProductsResponse.  # noqa: E501


        :return: The frida of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseFrida
        """
        return self._frida

    @frida.setter
    def frida(self, frida):
        """Sets the frida of this ProductsResponse.


        :param frida: The frida of this ProductsResponse.  # noqa: E501
        :type: SignalResponseFrida
        """

        self._frida = frida

    @property
    def ip_blocklist(self):
        """Gets the ip_blocklist of this ProductsResponse.  # noqa: E501


        :return: The ip_blocklist of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseIpBlocklist
        """
        return self._ip_blocklist

    @ip_blocklist.setter
    def ip_blocklist(self, ip_blocklist):
        """Sets the ip_blocklist of this ProductsResponse.


        :param ip_blocklist: The ip_blocklist of this ProductsResponse.  # noqa: E501
        :type: SignalResponseIpBlocklist
        """

        self._ip_blocklist = ip_blocklist

    @property
    def tor(self):
        """Gets the tor of this ProductsResponse.  # noqa: E501


        :return: The tor of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseTor
        """
        return self._tor

    @tor.setter
    def tor(self, tor):
        """Sets the tor of this ProductsResponse.


        :param tor: The tor of this ProductsResponse.  # noqa: E501
        :type: SignalResponseTor
        """

        self._tor = tor

    @property
    def privacy_settings(self):
        """Gets the privacy_settings of this ProductsResponse.  # noqa: E501


        :return: The privacy_settings of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponsePrivacySettings
        """
        return self._privacy_settings

    @privacy_settings.setter
    def privacy_settings(self, privacy_settings):
        """Sets the privacy_settings of this ProductsResponse.


        :param privacy_settings: The privacy_settings of this ProductsResponse.  # noqa: E501
        :type: SignalResponsePrivacySettings
        """

        self._privacy_settings = privacy_settings

    @property
    def virtual_machine(self):
        """Gets the virtual_machine of this ProductsResponse.  # noqa: E501


        :return: The virtual_machine of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseVirtualMachine
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine):
        """Sets the virtual_machine of this ProductsResponse.


        :param virtual_machine: The virtual_machine of this ProductsResponse.  # noqa: E501
        :type: SignalResponseVirtualMachine
        """

        self._virtual_machine = virtual_machine

    @property
    def vpn(self):
        """Gets the vpn of this ProductsResponse.  # noqa: E501


        :return: The vpn of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseVpn
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn):
        """Sets the vpn of this ProductsResponse.


        :param vpn: The vpn of this ProductsResponse.  # noqa: E501
        :type: SignalResponseVpn
        """

        self._vpn = vpn

    @property
    def proxy(self):
        """Gets the proxy of this ProductsResponse.  # noqa: E501


        :return: The proxy of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseProxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ProductsResponse.


        :param proxy: The proxy of this ProductsResponse.  # noqa: E501
        :type: SignalResponseProxy
        """

        self._proxy = proxy

    @property
    def tampering(self):
        """Gets the tampering of this ProductsResponse.  # noqa: E501


        :return: The tampering of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseTampering
        """
        return self._tampering

    @tampering.setter
    def tampering(self, tampering):
        """Sets the tampering of this ProductsResponse.


        :param tampering: The tampering of this ProductsResponse.  # noqa: E501
        :type: SignalResponseTampering
        """

        self._tampering = tampering

    @property
    def raw_device_attributes(self):
        """Gets the raw_device_attributes of this ProductsResponse.  # noqa: E501


        :return: The raw_device_attributes of this ProductsResponse.  # noqa: E501
        :rtype: SignalResponseRawDeviceAttributes
        """
        return self._raw_device_attributes

    @raw_device_attributes.setter
    def raw_device_attributes(self, raw_device_attributes):
        """Sets the raw_device_attributes of this ProductsResponse.


        :param raw_device_attributes: The raw_device_attributes of this ProductsResponse.  # noqa: E501
        :type: SignalResponseRawDeviceAttributes
        """

        self._raw_device_attributes = raw_device_attributes

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
        if issubclass(ProductsResponse, dict):
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
        if not isinstance(other, ProductsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductsResponse):
            return True

        return self.to_dict() != other.to_dict()
