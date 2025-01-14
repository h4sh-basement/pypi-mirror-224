﻿"""_794.py

PinionBevelGeneratingModifiedRollMachineSettings
"""


from mastapy.gears.manufacturing.bevel import _799
from mastapy._internal.python_net import python_net_import

_PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionBevelGeneratingModifiedRollMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionBevelGeneratingModifiedRollMachineSettings',)


class PinionBevelGeneratingModifiedRollMachineSettings(_799.PinionFinishMachineSettings):
    """PinionBevelGeneratingModifiedRollMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_BEVEL_GENERATING_MODIFIED_ROLL_MACHINE_SETTINGS

    def __init__(self, instance_to_wrap: 'PinionBevelGeneratingModifiedRollMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
