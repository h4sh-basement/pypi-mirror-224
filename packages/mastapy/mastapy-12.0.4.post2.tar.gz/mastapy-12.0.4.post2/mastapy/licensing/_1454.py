﻿"""_1454.py

LicenceServer
"""


from typing import List, Iterable

from mastapy._internal import constructor, conversion
from mastapy._internal.class_property import classproperty
from mastapy.licensing import _7502, _7503, _7504
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import('System', 'Array')
_LICENCE_SERVER = python_net_import('SMT.MastaAPI.Licensing', 'LicenceServer')


__docformat__ = 'restructuredtext en'
__all__ = ('LicenceServer',)


class LicenceServer:
    """LicenceServer

    This is a mastapy class.
    """

    TYPE = _LICENCE_SERVER

    def __init__(self, instance_to_wrap: 'LicenceServer.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def server_address(cls) -> 'str':
        """str: 'ServerAddress' is the original name of this property."""

        temp = LicenceServer.TYPE.ServerAddress

        if temp is None:
            return ''

        return temp

    @server_address.setter
    def server_address(cls, value: 'str'):
        LicenceServer.TYPE.ServerAddress = str(value) if value is not None else ''

    @classproperty
    def server_port(cls) -> 'int':
        """int: 'ServerPort' is the original name of this property."""

        temp = LicenceServer.TYPE.ServerPort

        if temp is None:
            return 0

        return temp

    @server_port.setter
    def server_port(cls, value: 'int'):
        LicenceServer.TYPE.ServerPort = int(value) if value is not None else 0

    @classproperty
    def web_server_port(cls) -> 'int':
        """int: 'WebServerPort' is the original name of this property."""

        temp = LicenceServer.TYPE.WebServerPort

        if temp is None:
            return 0

        return temp

    @web_server_port.setter
    def web_server_port(cls, value: 'int'):
        LicenceServer.TYPE.WebServerPort = int(value) if value is not None else 0

    @staticmethod
    def update_server_settings(server_details: '_7502.LicenceServerDetails'):
        """ 'UpdateServerSettings' is the original name of this method.

        Args:
            server_details (mastapy.licensing.LicenceServerDetails)
        """

        LicenceServer.TYPE.UpdateServerSettings(server_details.wrapped if server_details else None)

    @staticmethod
    def get_server_settings() -> '_7502.LicenceServerDetails':
        """ 'GetServerSettings' is the original name of this method.

        Returns:
            mastapy.licensing.LicenceServerDetails
        """

        method_result = LicenceServer.TYPE.GetServerSettings()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @staticmethod
    def request_module(module_code: 'str') -> 'bool':
        """ 'RequestModule' is the original name of this method.

        Args:
            module_code (str)

        Returns:
            bool
        """

        module_code = str(module_code)
        method_result = LicenceServer.TYPE.RequestModule(module_code if module_code else '')
        return method_result

    @staticmethod
    def request_module_and_prerequisites(module_code: 'str') -> 'bool':
        """ 'RequestModuleAndPrerequisites' is the original name of this method.

        Args:
            module_code (str)

        Returns:
            bool
        """

        module_code = str(module_code)
        method_result = LicenceServer.TYPE.RequestModuleAndPrerequisites(module_code if module_code else '')
        return method_result

    @staticmethod
    def request_modules(module_codes: 'List[str]') -> 'bool':
        """ 'RequestModules' is the original name of this method.

        Args:
            module_codes (List[str])

        Returns:
            bool
        """

        module_codes = conversion.to_list_any(module_codes)
        method_result = LicenceServer.TYPE.RequestModules(module_codes)
        return method_result

    @staticmethod
    def get_module_prerequisites(module_code: 'str') -> 'Iterable[str]':
        """ 'GetModulePrerequisites' is the original name of this method.

        Args:
            module_code (str)

        Returns:
            Iterable[str]
        """

        module_code = str(module_code)
        return conversion.pn_to_mp_objects_in_iterable(LicenceServer.TYPE.GetModulePrerequisites(module_code if module_code else ''), str)

    @staticmethod
    def get_requested_module_codes() -> 'Iterable[str]':
        """ 'GetRequestedModuleCodes' is the original name of this method.

        Returns:
            Iterable[str]
        """

        return conversion.pn_to_mp_objects_in_iterable(LicenceServer.TYPE.GetRequestedModuleCodes(), str)

    @staticmethod
    def remove_module(module_code: 'str'):
        """ 'RemoveModule' is the original name of this method.

        Args:
            module_code (str)
        """

        module_code = str(module_code)
        LicenceServer.TYPE.RemoveModule(module_code if module_code else '')

    @staticmethod
    def remove_modules(module_codes: 'List[str]'):
        """ 'RemoveModules' is the original name of this method.

        Args:
            module_codes (List[str])
        """

        module_codes = conversion.to_list_any(module_codes)
        LicenceServer.TYPE.RemoveModules(module_codes)

    @staticmethod
    def get_licensed_module_details() -> 'Iterable[_7503.ModuleDetails]':
        """ 'GetLicensedModuleDetails' is the original name of this method.

        Returns:
            Iterable[mastapy.licensing.ModuleDetails]
        """

        return conversion.pn_to_mp_objects_in_iterable(LicenceServer.TYPE.GetLicensedModuleDetails())

    @staticmethod
    def get_available_module_details() -> 'Iterable[_7503.ModuleDetails]':
        """ 'GetAvailableModuleDetails' is the original name of this method.

        Returns:
            Iterable[mastapy.licensing.ModuleDetails]
        """

        return conversion.pn_to_mp_objects_in_iterable(LicenceServer.TYPE.GetAvailableModuleDetails())

    @staticmethod
    def get_requested_module_statuses() -> 'Iterable[_7504.ModuleLicenceStatus]':
        """ 'GetRequestedModuleStatuses' is the original name of this method.

        Returns:
            Iterable[mastapy.licensing.ModuleLicenceStatus]
        """

        return conversion.pn_to_mp_objects_in_iterable(LicenceServer.TYPE.GetRequestedModuleStatuses())
