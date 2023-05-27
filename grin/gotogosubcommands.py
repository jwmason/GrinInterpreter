"""This module is in charge of handling the GOTO and GOSUB commands"""

from grin.relationaloperationcommands import relational_operation

def target_conditional(line, variable_dict, line_dict, list_len, current_line):
    """This function is in charge of deciding whether or not to execute GOTO or GOSUB command"""
    # Holds the result of the IF statement
    result = False
    # If it includes an IF command
    if len(line[0]) == 6:
        var1 = line[0][3]
        var2 = line[0][5]
        # Accounting for variables and values
        if var1.text() in variable_dict:
            var1 = variable_dict[var1.text()]
        else:
            var1 = var1.value()
        if var2.text() in variable_dict:
            var2 = variable_dict[var2.text()]
        else:
            var2 = var2.value()
        relational_op = line[0][4].text()
        # Checks if the relational operation is True or False
        result = relational_operation(var1, var2, relational_op)
    if (result is True) or (len(line[0]) == 2):
        target = line[0][1].value()
        target_line = find_target_line(target, line, line_dict)
        if (target_line+current_line) > 0 and (target_line+current_line) <= list_len:
            if target_line < 0:
                return current_line-target_line
            else:
                return current_line+target_line
        else:
            return None


def find_target_line(target, line, line_dict):
    """This function finds target line"""
    # Finding line to go to
    if isinstance(target, int):
        target = target
    elif isinstance(target, str):
        if target in line_dict:
            target = line_dict[target]
        else:
            raise Exception('TypeError: Not a valid parameter')
    else:
        raise Exception('TypeError: Not a valid parameter')
    return target


__all__ = [
    target_conditional.__name__,
]