"""This module is in charge of handing input commands from Grin"""


# Cannot test this function because it requires input, so it will not be included in test cases
def innum():
    """This function is used to read an integer or float"""
    num = input().strip()
    try:
        num = float(num)
        if num.is_integer():
            return int(num)
        else:
            return num
    except ValueError as e:
        print(e)
        exit()


# Cannot test this function because it requires input, so it will not be included in test cases
def instr():
    """This function is used to read a string"""
    return str(input())


__all__ = [
    innum.__name__,
    instr.__name__
]