from ..__class_init__ import *


class ProfileGeneric(ic.COSEMInterfaceClasses):
    """dummy class"""
    CLASS_ID = ClassID.PROFILE_GENERIC

    def __new__(cls, *args, **kwargs):
        raise ValueError(F"version: {__name__[-1]} of {cls.__class__.__name__} not support framework")

    def characteristics_init(self):
        """ initiate all attributes and methods of class """

    def NAME(self) -> str:
        return "not support version"
