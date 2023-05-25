"""This module is in charge of handling relational operations"""

def relational_operation(var1, var2, relational_op) -> bool:
    """This performs a relational operation"""
    result = False
    try:
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
    # Except statement cannot be tested because the exit()
    # function prevents testing from catching specified errors
    except (TypeError, RuntimeError) as e:
        print(e)
        exit()

__all__ = [
    relational_operation.__name__
]