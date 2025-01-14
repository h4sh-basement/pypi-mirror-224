﻿"""_2250.py

RealignmentResult
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_REALIGNMENT_RESULT = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RealignmentResult')


__docformat__ = 'restructuredtext en'
__all__ = ('RealignmentResult',)


class RealignmentResult(_0.APIBase):
    """RealignmentResult

    This is a mastapy class.
    """

    TYPE = _REALIGNMENT_RESULT

    def __init__(self, instance_to_wrap: 'RealignmentResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def successful(self) -> 'bool':
        """bool: 'Successful' is the original name of this property."""

        temp = self.wrapped.Successful

        if temp is None:
            return False

        return temp

    @successful.setter
    def successful(self, value: 'bool'):
        self.wrapped.Successful = bool(value) if value is not None else False
