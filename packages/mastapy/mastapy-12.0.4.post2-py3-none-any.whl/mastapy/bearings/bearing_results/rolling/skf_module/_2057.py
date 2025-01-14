﻿"""_2057.py

RotationalFrequency
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ROTATIONAL_FREQUENCY = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'RotationalFrequency')


__docformat__ = 'restructuredtext en'
__all__ = ('RotationalFrequency',)


class RotationalFrequency(_0.APIBase):
    """RotationalFrequency

    This is a mastapy class.
    """

    TYPE = _ROTATIONAL_FREQUENCY

    def __init__(self, instance_to_wrap: 'RotationalFrequency.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_ring(self) -> 'float':
        """float: 'InnerRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_ring(self) -> 'float':
        """float: 'OuterRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_about_its_axis(self) -> 'float':
        """float: 'RollingElementAboutItsAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingElementAboutItsAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_set_cage(self) -> 'float':
        """float: 'RollingElementSetCage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingElementSetCage

        if temp is None:
            return 0.0

        return temp
