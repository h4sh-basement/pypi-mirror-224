﻿"""_2512.py

InputPowerInputOptions
"""


from mastapy.utility_gui import _1812
from mastapy._internal.python_net import python_net_import

_INPUT_POWER_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'InputPowerInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('InputPowerInputOptions',)


class InputPowerInputOptions(_1812.ColumnInputOptions):
    """InputPowerInputOptions

    This is a mastapy class.
    """

    TYPE = _INPUT_POWER_INPUT_OPTIONS

    def __init__(self, instance_to_wrap: 'InputPowerInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
