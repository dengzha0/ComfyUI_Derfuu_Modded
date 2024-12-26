import math

from ...components.fields import Field
from ...components.tree import TREE_TRIGONOMETRY

# changed to new node Greater
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

# changed to new node "FilterSize"
class CosNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "width": Field.int(),
                "height": Field.int(),
                "small_size": Field.int(),
                "big_size": Field.int()
            }
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("WIDTH", "HEIGHT")
    FUNCTION = "get_value"
    CATEGORY = TREE_TRIGONOMETRY

    def get_value(self, width, height, small_size, big_size):
        larger_side = ""
        if width > height:
            larger_side = "width"
        else:
            larger_side = "height"

        new_width = 0
        new_height = 0
        ratio = 0
        if larger_side == "width":
            ratio = height / width
            if width < small_size:
                new_width = small_size
                new_height = int(new_width * ratio / 8) * 8
            else:
                new_width = big_size
                new_height = int(new_width * ratio / 8) * 8
        elif larger_side == "height":
            ratio = width / height
            if height < small_size:
                new_height = small_size
                new_width = int(new_height * ratio / 8) * 8
            else:
                new_height = big_size
                new_width = int(new_height * ratio / 8) * 8
        else:
            new_width = width
            new_height = height
        return (new_width,new_height,)


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
