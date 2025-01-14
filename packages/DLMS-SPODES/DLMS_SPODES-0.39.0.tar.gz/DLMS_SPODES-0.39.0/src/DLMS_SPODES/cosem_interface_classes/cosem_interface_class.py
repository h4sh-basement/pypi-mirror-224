from __future__ import annotations
import dataclasses
from abc import ABC, abstractmethod
from typing import Iterator, Type, TypeAlias, Callable, Any, Self
from .. import settings
from ..types import cdt, ut, cst
from ..relation_to_OBIS import get_name
import logging
from enum import IntEnum
from datetime import datetime, timedelta, timezone
from itertools import count
from . import collection as col
from ..types.implementations import enums

match settings.get_current_language():
    case settings.Language.ENGLISH: from ..Values.EN import attr_names as an
    case settings.Language.RUSSIAN: from ..Values.RU import attr_names as an

logger = logging.getLogger(__name__)
logger.level = logging.INFO

logger.info(F'Register start')

_n_class = count(0)


class Classifier(IntEnum):
    """ (dyn.) Classifies an attribute that carries a process value, which is updated by the meter itself.
    (static) Classifies an attribute, which is not updated by the meter itself (e.g. configuration data). """
    NOT_SPECIFIC = 0
    STATIC = 1
    DYNAMIC = 2

    def __str__(self):
        return self.name


SelectiveAccessDescriptor: TypeAlias = ut.SelectiveAccessDescriptor  # TODO: make with subclass


@dataclasses.dataclass(frozen=True)
class ICElement:
    NAME: str


@dataclasses.dataclass(frozen=True)
class ICAElement(ICElement):
    DATA_TYPE: Type[cdt.CommonDataType] | ut.CHOICE
    min: int = None
    max: int = None
    default: int = None
    classifier: Classifier = Classifier.STATIC
    selective_access: Type[SelectiveAccessDescriptor] | None = None

    def __str__(self):
        return F'{self.NAME} ({self.classifier.name.lower()}) {self.DATA_TYPE.NAME}'


@dataclasses.dataclass(frozen=True)
class ICMElement(ICElement):
    DATA_TYPE: Type[cdt.CommonDataType]

    def __str__(self):
        return F'{self.NAME} {self.DATA_TYPE.NAME}'


_LN_ELEMENT = ICAElement(an.LOGICAL_NAME, cst.LogicalName)
"""" first element for each COSEM Interface Class"""


class COSEMInterfaceClasses(ABC):
    CLASS_ID: ut.CosemClassId
    VERSION: cdt.Unsigned | None = None
    """ Identification code of the version of the class. The version of each object is retrieved together with the logical name and the class_id by reading the object_list 
    attribute of an “Association LN” / ”Association SN” object. Within one logical device, all instances of a certain class must be of the same version."""
    A_ELEMENTS: tuple[ICAElement, ...]
    M_ELEMENTS: tuple[ICMElement, ...] = None
    cardinality: tuple[int, int | None]
    __attributes: list[cdt.CommonDataType | None]
    __specific_methods: tuple[cdt.CommonDataType, ...] = None
    _cbs_attr_post_init: dict[int, Callable]
    __record_time: list[cdt.DateTime | None]  # TODO: make to int
    collection: col.Collection | None

    def __init__(self, logical_name: cst.LogicalName | bytes | str):
        self.collection = None
        # """ TODO: """
        self.cardinality = (0, None)
        """ (min, max). default is (0, None) from 0 to infinity. If min == max then they are value.   
        Specifies the number of instances of the class within a logical device. value The class shall be 
        instantiated exactly “value” times. min...max. The class shall be instantiated at least “min.” times 
        and at most “max.” times. If min. is zero (0) then the class is optional, otherwise (min. > 0) "min." 
        instantiations of the class are mandatory. """

        self.__attributes = [_LN_ELEMENT.DATA_TYPE(logical_name), *[None] * len(self.A_ELEMENTS)]
        """ Attributes container """

        if self.M_ELEMENTS is not None:
            self.__specific_methods = tuple(el.DATA_TYPE() for el in self.M_ELEMENTS)
            """Specific methods container"""

        self._cbs_attr_post_init = dict()
        """container with callbacks for post initial attribute by index"""

        self._cbs_attr_before_init = dict()
        """container with callbacks for before initial attribute by index"""

        self.__record_time = [None] * len(self.A_ELEMENTS)

        # init all attributes with default value
        for i in range(2, len(self.A_ELEMENTS)+2):
            default = self.get_attr_element(i).default
            if default is not None:
                self.set_attr(i, default)

        self.characteristics_init()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.hash_ = next(_n_class)

    def copy(self, source: Self, association_id: int = 3):
        """copy object according by association"""
        for i, a in source.get_index_with_attributes():
            if i == 1 or a is None or self.get_attr_element(i).classifier == Classifier.DYNAMIC:
                continue
            else:
                if source.collection is not None and self.get_attr_element(i).classifier == Classifier.STATIC and not source.collection.is_writable(ln=self.logical_name,
                                                                                                                                                    index=i,
                                                                                                                                                    association_id=association_id):
                    self.__attributes[i-1] = a
                else:
                    if isinstance(arr := self.__attributes[i-1], cdt.Array):
                        arr.set_type(a.TYPE)
                    self.set_attr(i, a.encoding)

    @classmethod
    def get_attr_element(cls, i: int) -> ICAElement:
        """return element by order index. Override in each new class"""
        match i:
            case 1: return _LN_ELEMENT
            case _: return cls.A_ELEMENTS[i - 2]

    @classmethod
    def get_meth_element(cls, i: int) -> ICElement:
        """ implement in subclasses with methods """
        return cls.M_ELEMENTS[i - 1]

    @abstractmethod
    def characteristics_init(self):
        """ initiate all attributes and methods of class """

    def get_attr(self, index: int) -> Any | None:
        if index >= 1:
            return self.__attributes[index-1]
        else:
            raise IndexError(F'not support {index=} as attribute')

    def set_attr(self, index: int, value, with_time: bool | datetime = False) -> timedelta:
        if self.__attributes[index-1] is None:
            new_value = self.get_attr_element(index).DATA_TYPE(value if value is not None else self.get_attr_element(index).default)
            if cb_func := self._cbs_attr_before_init.get(index, None):
                cb_func(new_value)
                self._cbs_attr_before_init.pop(index)
            self.__attributes[index-1] = new_value
            if cb_func := self._cbs_attr_post_init.get(index, None):
                cb_func()
                self._cbs_attr_post_init.pop(index)
            else:
                """without callback post init"""
        else:
            self.__attributes[index-1].set(value)
        # todo: make better all below
        TZ = timezone(datetime.now() - datetime.utcnow())
        """ os time zone """
        time_now = datetime.now(TZ)
        if isinstance(with_time, bool) and with_time:
            self.set_record_time(index, cdt.DateTime(time_now))
            return timedelta()
        elif isinstance(with_time, datetime):
            delta = (time_now-with_time)/2
            self.set_record_time(index, cdt.DateTime(time_now - delta))
            return delta

    def set_attr_link(self, index: int, link: cdt.CommonDataType):
        # self.__attributes[index - 1] = link  # TODO: without validate now for pass load_objects
        if isinstance(link, self.get_attr_element(index).DATA_TYPE):
            self.__attributes[index-1] = link
        else:
            raise ValueError(F'get wrong link: {link} for {self} attr: {index}')

    def get_attr_data_type(self, index: int) -> Type[cdt.CommonDataType] | ut.CHOICE:
        """search data_type attribute value"""
        value: cdt.CommonDataType = self.get_attr(index)
        if value is not None:
            return value.__class__
        else:
            return self.get_attr_element(index).DATA_TYPE

    def clear_attr(self, i: int):
        """use in template"""
        if i > 1:
            self.__attributes[i-1] = None
        else:
            raise ValueError(F'not support clear {self} attr: {i}')

    def get_meth(self, index: int) -> Any:
        if index >= 1:
            return self.__specific_methods[index-1]
        else:
            raise IndexError(F'not support {index=} as attribute')

    def get_record_time(self, index: int) -> cdt.DateTime | None:
        return self.__record_time[index-2]

    def set_record_time(self, index: int, value: str | bytes | cdt.DateTime):
        self.__record_time[index-2] = cdt.DateTime(value)

    def get_index_with_attributes(self) -> Iterator[tuple[int, cdt.CommonDataType | None]]:
        """ if by initiation order is True then need override method for concrete class"""
        return iter(zip(range(1, self.get_attr_length()+1), self.__attributes))

    def get_attr_length(self) -> int:
        """common attributes amount"""
        return len(self.A_ELEMENTS)+1

    @property
    def it_index_with_meth(self) -> Iterator[tuple[int, cdt.CommonDataType]]:
        return iter(zip(range(1, 20), self.__specific_methods))

    @property
    @abstractmethod
    def NAME(self) -> str:
        """ class name according to current language """

    @property
    def logical_name(self) -> cst.LogicalName:
        """ The logical name is always the first attribute of a class. It identifies the instantiation (COSEM object) of this class.
        The value of the logical_name conforms to OBIS (see IEC 62056-61)"""
        return self.get_attr(1)

    def __setattr__(self, key, value):
        match key:
            case 'VERSION' | 'CLASS_ID' | 'A_ELEMENTS' | 'M_ELEMENTS' as prop: raise ValueError(F"Don't support set {prop}")
            case _:                                                            super().__setattr__(key, value)

    def __getitem__(self, item) -> cdt.CommonDataType:
        """ get attribute value by index, start with 1 """
        if isinstance(item, str):
            return self.__getattr__(item)
        return self.get_attr(item)

    def __iter__(self) -> Iterator[cdt.CommonDataType]:
        """ return attributes iterator"""
        return iter(self.__attributes)

    def __str__(self):
        return F'{self.logical_name} {get_name(self.logical_name)}'

    def get_obis(self) -> bytes:
        """ return obis as bytes[6] """
        return self.logical_name.contents

    @property
    def instance_id(self) -> cdt.OctetString:
        return self.logical_name

    # TODO: rewrite this
    def get_attribute_descriptor(self, index: int) -> bytes:
        """ Cosem-Attribute-Descriptor IS/IEC 62056-53 : 2006, 8.3 Useful types """
        return self.CLASS_ID.contents + self.instance_id.contents + ut.CosemObjectAttributeId(index).contents

    @property
    def string_type_cardinality(self) -> str:
        min_cardinality, max_cardinality = self.cardinality
        if min_cardinality == max_cardinality:
            return str(min_cardinality)
        else:
            max_cardinality = str(max_cardinality) if max_cardinality else 'n'
            return F'{str(min_cardinality)}...{max_cardinality}'

    def reset_attribute(self, index: int):
        """ try set default to value """
        self.set_attr(index, self.get_attr_element(index).default)

    def get_attr_descriptor(self, value: int, SAP: enums.ClientSAP = enums.configurator_client) -> ut.CosemAttributeDescriptor:
        """ TODO """
        return ut.CosemAttributeDescriptor((self.CLASS_ID,
                                            ut.CosemObjectInstanceId(self.logical_name.contents),
                                            ut.CosemObjectAttributeId(value)))

    def get_meth_descriptor(self, value: str | int) -> ut.CosemMethodDescriptor:
        """ TODO """
        match value:
            case int() as index:
                return ut.CosemMethodDescriptor((ut.CosemClassId(self.CLASS_ID.contents),
                                                 ut.CosemObjectInstanceId(self.logical_name.contents),
                                                 ut.CosemObjectMethodId(index)))

    def __hash__(self):
        return hash(self.logical_name)
