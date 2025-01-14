﻿"""_6806.py

ElectricMachineHarmonicLoadDataFromJMAG
"""


from mastapy.system_model.analyses_and_results.static_loads import _6809, _6813
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromJMAG')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromJMAG',)


class ElectricMachineHarmonicLoadDataFromJMAG(_6809.ElectricMachineHarmonicLoadDataFromMotorPackages['_6813.ElectricMachineHarmonicLoadJMAGImportOptions']):
    """ElectricMachineHarmonicLoadDataFromJMAG

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_JMAG

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromJMAG.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
