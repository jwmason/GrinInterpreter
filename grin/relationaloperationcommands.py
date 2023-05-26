"""This module is in charge of handling relational operations"""


def relational_operation(var1, var2, relational_op) -> bool:
    """This performs a relational operation"""
    result = False
    if relational_op == "<":
        result = var1 < var2
    elif relational_op == ">":
        result = var1 > var2
    elif relational_op == "<=":
        result = var1 <= var2
    elif relational_op == ">=":
        result = var1 >= var2
    elif relational_op == "=":
        result = var1 == var2
    elif relational_op == "<>":
        result = var1 != var2
    return result


__all__ = [
    relational_operation.__name__
]