﻿"""_2511.py

BoostPressureInputOptions
"""


from mastapy.utility_gui import _1812
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'BoostPressureInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('BoostPressureInputOptions',)


class BoostPressureInputOptions(_1812.ColumnInputOptions):
    """BoostPressureInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_INPUT_OPTIONS

    def __init__(self, instance_to_wrap: 'BoostPressureInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
