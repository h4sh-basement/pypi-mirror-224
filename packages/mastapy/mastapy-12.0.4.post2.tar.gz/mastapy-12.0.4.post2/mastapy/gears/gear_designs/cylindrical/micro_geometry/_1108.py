﻿"""_1108.py

LeadSlopeReliefWithDeviation
"""


from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107
from mastapy._internal.python_net import python_net_import

_LEAD_SLOPE_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'LeadSlopeReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadSlopeReliefWithDeviation',)


class LeadSlopeReliefWithDeviation(_1107.LeadReliefWithDeviation):
    """LeadSlopeReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _LEAD_SLOPE_RELIEF_WITH_DEVIATION

    def __init__(self, instance_to_wrap: 'LeadSlopeReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
