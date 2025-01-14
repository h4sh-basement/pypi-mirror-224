﻿"""_855.py

FaceGearSetLoadDistributionAnalysis
"""


from mastapy.gears.ltca.cylindrical import _853
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'FaceGearSetLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetLoadDistributionAnalysis',)


class FaceGearSetLoadDistributionAnalysis(_853.CylindricalGearSetLoadDistributionAnalysis):
    """FaceGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
