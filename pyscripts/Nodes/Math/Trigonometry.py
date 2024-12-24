import math

from ...components.fields import Field
from ...components.tree import TREE_TRIGONOMETRY


class SinNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "value_a": Field.int(),
                "value_b": Field.int()
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value_a, value_b):
        greater = 0
        if value_a > value_b:
            greater = value_a    
        else:
            greater = value_b
        return (greater,)


class CosNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "value": Field.float(),
                "type_": Field.combo(["RAD", "DEG"],),
                "arcCos": Field.combo([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value, type_="RAD", arcCos=False):
        if type_ == "DEG":
            value = math.radians(value)
        if arcCos == True:
            value = math.acos(value)
        else:
            value = math.cos(value)
        return (value,)


class tgNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "value": Field.float(),
                "type_": Field.combo(["RAD", "DEG"],),
                "arcTan": Field.combo([False, True],)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, value, type_="RAD", arcTan=False):
        if type_ == "DEG":
            value = math.radians(value)
        if arcTan == True:
            value = math.atan(value)
        else:
            value = math.tan(value)
        return (value,)
