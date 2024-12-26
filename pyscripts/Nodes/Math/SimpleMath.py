import math

from ...components.fields import Field
from ...components.tree import TREE_MATH


class MultiplyNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": Field.int(),
                "Multiplier": Field.float(),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "multiply"
    CATEGORY = TREE_MATH

    def multiply(self, Value, Multiplier):
        total = int(Value * Multiplier)
        return (total,)


class DivideNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": Field.int(),
                "Divisor": Field.float(),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "divide"
    CATEGORY = TREE_MATH

    def divide(self, Value, Divisor):
        total = int(Value / Divisor)
        return (total,)


class SumNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": Field.int(),
                "Value_B": Field.int(),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "sum"
    CATEGORY = TREE_MATH

    def sum(self, Value_A, Value_B):
        total = int(Value_A + Value_B)
        return (total,)


class SubtractNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value_A": Field.int(),
                "Value_B": Field.int(),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "sub"
    CATEGORY = TREE_MATH

    def sub(self, Value_A, Value_B):
        total = int(Value_A - Value_B)
        return (total,)

# changed to new node KeepRatio
class PowNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": Field.int(),
                "height": Field.int(),
                "max_length": Field.int(default=1024),
            },
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("WIDTH", "HEIGHT")
    FUNCTION = "max_side"
    CATEGORY = TREE_MATH

    def max_side(self, width, height, max_length):
        if width > height:
            ratio = height / width
            width = max_length
            height = int(ratio * width)
        else:
            ratio = width / height
            height = max_length
            width = int(ratio * height)
        return (width,height,)


class SquareRootNode:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Value": Field.float(),
            },
        }

    RETURN_TYPES = ("FLOAT", "FLOAT",)
    FUNCTION = "sqrt"
    CATEGORY = TREE_MATH

    def sqrt(self, Value):
        total = math.sqrt(Value)
        return (total, -total,)
