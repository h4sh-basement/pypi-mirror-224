﻿"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1503 import IndividualContactPosition
    from ._1504 import SurfaceToSurfaceContact
