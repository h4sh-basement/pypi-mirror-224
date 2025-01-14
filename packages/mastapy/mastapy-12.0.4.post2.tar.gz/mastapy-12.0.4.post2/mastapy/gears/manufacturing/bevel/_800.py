﻿"""_800.py

PinionHypoidFormateTiltMachineSettings
"""


from mastapy.gears.manufacturing.bevel import _799
from mastapy._internal.python_net import python_net_import

_PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionHypoidFormateTiltMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionHypoidFormateTiltMachineSettings',)


class PinionHypoidFormateTiltMachineSettings(_799.PinionFinishMachineSettings):
    """PinionHypoidFormateTiltMachineSettings

    This is a mastapy class.
    """

    TYPE = _PINION_HYPOID_FORMATE_TILT_MACHINE_SETTINGS

    def __init__(self, instance_to_wrap: 'PinionHypoidFormateTiltMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
