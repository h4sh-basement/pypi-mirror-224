from enum import Enum, auto
import random as rnd
from typing import Tuple
from warnings import warn

class CoopEnum(Enum):

    @classmethod
    def has_name(cls, name):
        return name in cls._member_names_

    @classmethod
    def has_value(cls, value):
        return value in set([item.value for item in cls])

    @classmethod
    def as_list(cls):
        warn('CoopEnum as_list() method has been depricated, use value_list() or name_list()', DeprecationWarning,
             stacklevel=2)
        return cls.name_list()

    @classmethod
    def value_list(cls):
        return [e.value for e in cls]

    @classmethod
    def name_list(cls):
        return [e.name for e in cls]

    @classmethod
    def by_str(cls, str_name):

        # TODO: Not the best lookup strategy for large lists. Should better use the functions of Enum
        try:
            ret = cls[str_name]
        except:
            ret = next((item for item in cls if str(item) == str_name), None)

        if ret is None:
            raise ValueError(f"{str_name} is not a valid value for [{cls}]")

        return ret

    @classmethod
    def by_val(cls, val):
        ret = next((item for item in cls if item.value == val), None)
        if ret is None:
            raise ValueError(f"{val} is not a valid value for [{cls}]")
        return ret

    @classmethod
    def random(cls):
        return rnd.choice(list(cls))

class CardinalPosition(CoopEnum):
    TOP_LEFT = (0, 1)
    TOP_RIGHT = (1, 1)
    TOP_CENTER = (0.5, 1)
    BOTTOM_LEFT = (0, 0)
    BOTTOM_RIGHT = (1, 0)
    RIGHT_CENTER = (1, 0.5)
    BOTTOM_CENTER = (0.5, 0)
    LEFT_CENTER = (0, 0.5)
    CENTER = (0.5, 0.5)

    @classmethod
    def bottom_left_from_alignment(cls,
                                dims: Tuple[float, float],
                                anchor: Tuple[float, float],
                                cardinality,
                                inverted_y: bool = False) -> Tuple[float, float]:
        y_modifier = 1
        if inverted_y:
            y_modifier = -1

        bl_x = anchor[0] - cardinality.value[0] * dims[0]
        bl_y = anchor[1] - cardinality.value[1] * dims[1] * y_modifier

        return bl_x, bl_y

    @classmethod
    def alignment_from_bottom_left(cls,
                                dims: Tuple[float, float],
                                bottom_left: Tuple[float, float],
                                cardinality,
                                inverted_y: bool = False) -> Tuple[float, float]:

        y_modifier = 1
        if inverted_y:
            y_modifier = -1

        x = bottom_left[0] + cardinality.value[0] * dims[0]
        y = bottom_left[1] + cardinality.value[1] * dims[1] * y_modifier

        return x, y


    @classmethod
    def alignment_conversion(cls,
                             dims: Tuple[float, float],
                             anchor: Tuple[float, float],
                             from_cardinality,
                             to_cardinality,
                             inverted_y: bool = False) -> Tuple[float, float]:
        if from_cardinality == to_cardinality:
            return anchor

        bl = CardinalPosition.bottom_left_from_alignment(dims=dims,
                                                      anchor=anchor,
                                                      cardinality=from_cardinality,
                                                      inverted_y=inverted_y)
        ret = CardinalPosition.alignment_from_bottom_left(dims, bl, to_cardinality, inverted_y)
        return ret



if __name__=="__main__":
    class Dummy(CoopEnum):
        A = auto()
        B = auto()
        C = auto()

    print(Dummy.random())