﻿"""_5677.py

ElectricMachineRotorYForcePeriodicExcitationDetail
"""


from mastapy.system_model.analyses_and_results.harmonic_analyses import _5674
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineRotorYForcePeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineRotorYForcePeriodicExcitationDetail',)


class ElectricMachineRotorYForcePeriodicExcitationDetail(_5674.ElectricMachinePeriodicExcitationDetail):
    """ElectricMachineRotorYForcePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL

    def __init__(self, instance_to_wrap: 'ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
