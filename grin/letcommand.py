"""This module handles the LET command"""

from grin.labels import label_execute

def let(line, variable_dict: dict, label_dict: dict, current_line) -> dict:
    """This function creates a variable in the given variable_dict"""
    variable = line[0][1].text()
    value = line[0][2].value()
    if value in variable_dict:
        value = variable_dict[value]
    if isinstance(value, str):
        if value in label_dict:
            variable_dict[variable] = label_dict[value]
            label_dict[variable] = current_line
            new_variable_dict = label_execute(variable_dict[variable], variable_dict, label_dict)
            variable_dict.update(new_variable_dict)
        else:
            variable_dict[variable] = value
    elif isinstance(value, (int, float)):
        variable_dict[variable] = value
    else:
        raise Exception('TypeError: Not a valid parameter')
    return variable_dict, label_dict


__all__ = [
    let.__name__
]