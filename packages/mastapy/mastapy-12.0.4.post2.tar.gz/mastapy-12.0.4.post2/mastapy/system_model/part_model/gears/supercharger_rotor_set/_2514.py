﻿"""_2514.py

RotorSetDataInputFileOptions
"""


from mastapy.utility_gui import _1813
from mastapy._internal.python_net import python_net_import

_ROTOR_SET_DATA_INPUT_FILE_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'RotorSetDataInputFileOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorSetDataInputFileOptions',)


class RotorSetDataInputFileOptions(_1813.DataInputFileOptions):
    """RotorSetDataInputFileOptions

    This is a mastapy class.
    """

    TYPE = _ROTOR_SET_DATA_INPUT_FILE_OPTIONS

    def __init__(self, instance_to_wrap: 'RotorSetDataInputFileOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
