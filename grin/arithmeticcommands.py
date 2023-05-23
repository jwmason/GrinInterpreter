"""This module is in charge of defining what eoch Grin command does in Python"""

def add(a: float, b: float):
    """This function adds two parameters"""
    result = a + b
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


def subtract(a: float, b: float):
    """This function subtracts two parameters"""
    result = a - b
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


def multiply(a: float, b: float):
    """This function multiplies two parameters"""
    result = a * b
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


def divide(a: float, b: float):
    """This function divides two parameters"""
    result = a / b
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


__all__ = [
    add.__name__,
    subtract.__name__,
    multiply.__name__,
    divide.__name__
]