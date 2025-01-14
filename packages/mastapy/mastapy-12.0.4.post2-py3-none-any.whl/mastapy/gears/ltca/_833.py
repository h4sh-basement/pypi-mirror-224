﻿"""_833.py

GearLoadDistributionAnalysis
"""


from mastapy.gears.analysis import _1209
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearLoadDistributionAnalysis',)


class GearLoadDistributionAnalysis(_1209.GearImplementationAnalysis):
    """GearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_DISTRIBUTION_ANALYSIS

    def __init__(self, instance_to_wrap: 'GearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
