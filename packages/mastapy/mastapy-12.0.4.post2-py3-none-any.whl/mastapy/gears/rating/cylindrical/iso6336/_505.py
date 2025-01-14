﻿"""_505.py

ISO63361996MeshSingleFlankRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _513
from mastapy._internal.python_net import python_net_import

_ISO63361996_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63361996MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63361996MeshSingleFlankRating',)


class ISO63361996MeshSingleFlankRating(_513.ISO6336AbstractMetalMeshSingleFlankRating):
    """ISO63361996MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_MESH_SINGLE_FLANK_RATING

    def __init__(self, instance_to_wrap: 'ISO63361996MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_factor_contact(self) -> 'float':
        """float: 'HelixAngleFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def transverse_load_factor_bending(self) -> 'float':
        """float: 'TransverseLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp
