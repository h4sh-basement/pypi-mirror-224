﻿"""_2566.py

TorqueConverterTurbine
"""


from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbine',)


class TorqueConverterTurbine(_2540.CouplingHalf):
    """TorqueConverterTurbine

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
