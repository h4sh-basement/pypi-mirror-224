﻿"""_6921.py

BoostPressureLoadCaseInputOptions
"""


from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.gears import _2482
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility_gui import _1812
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'BoostPressureLoadCaseInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('BoostPressureLoadCaseInputOptions',)


class BoostPressureLoadCaseInputOptions(_1812.ColumnInputOptions):
    """BoostPressureLoadCaseInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS

    def __init__(self, instance_to_wrap: 'BoostPressureLoadCaseInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_set(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGearSet: 'RotorSet' is the original name of this property."""

        temp = self.wrapped.RotorSet

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_CylindricalGearSet)(temp) if temp is not None else None

    @rotor_set.setter
    def rotor_set(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.RotorSet = value
