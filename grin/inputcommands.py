"""This module is in charge of handing input commands from Grin"""


# Cannot test this function because it requires input, so it will not be included in test cases
def innum():
    """This function is used to read an integer or float"""
    num = float(input())
    if isinstance(type(num), float) and num.is_integer():
        return int(num)
    else:
        return float(num)


# Cannot test this function because it requires input, so it will not be included in test cases
def instr():
    """This function is used to read a string"""
    return str(input())


__all__ = [
    innum.__name__,
    instr.__name__
]