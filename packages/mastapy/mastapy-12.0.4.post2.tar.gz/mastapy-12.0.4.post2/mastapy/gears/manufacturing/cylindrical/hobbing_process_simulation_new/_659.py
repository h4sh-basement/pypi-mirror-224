﻿"""_659.py

HobbingProcessCalculation
"""


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _673
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessCalculation',)


class HobbingProcessCalculation(_673.ProcessCalculation):
    """HobbingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_CALCULATION

    def __init__(self, instance_to_wrap: 'HobbingProcessCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
