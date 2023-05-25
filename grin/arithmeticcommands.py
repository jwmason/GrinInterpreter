"""This module is in charge of defining what eoch Grin command does in Python"""

def add(a: float, b: float):
    """This function adds two parameters"""
    try:
        result = a + b
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result
    except TypeError as e:
        print(e)
        exit()


def subtract(a: float, b: float):
    """This function subtracts two parameters"""
    try:
        result = a - b
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result
    except TypeError as e:
        print(e)
        exit()

def multiply(a: float, b: float):
    """This function multiplies two parameters"""
    try:
        result = a * b
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result
    except TypeError as e:
        print(e)
        exit()

def divide(a: float, b: float):
    """This function divides two parameters"""
    try:
        result = a / b
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result
    except (TypeError, ZeroDivisionError) as e:
        print(e)
        exit()


__all__ = [
    add.__name__,
    subtract.__name__,
    multiply.__name__,
    divide.__name__
]