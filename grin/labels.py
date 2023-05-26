"""This module is in charge of executing the command given to the label"""

import grin


def label_check(token, line, label_dict) -> dict:
    """This function checks if the line has a label"""
    possible_colon = line[0][1].text()
    if possible_colon == ':':
        label_name = token.text()
        label_dict[label_name] = line[0][2:]
    return label_dict


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def label_execute(grin_token_list, variable_dict, label_dict) -> dict:
    """This function takes the label command and executes it"""
    line = grin_token_list
    token = line[0]

    # Labels - LET, GOTO, GOSUB
    possible_colon = line[1].text()
    if possible_colon == ':':
        label_name = token.text()
        label_dict[label_name] = line[0][2:]

    # Variable Setting
    elif token.text() == 'LET':
        variable = line[1].text()
        value = line[2].value()
        if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            variable_dict[variable] = value
        elif isinstance(value, str):
            # Check if the value is a label
            if value in label_dict:
                variable_dict[variable] = label_dict[value]
            else:
                print('TypeError: Not a valid parameter')
                exit()
        elif isinstance(value, (int, float)):
            variable_dict[variable] = value
        else:
            print('TypeError: Not a valid parameter')
            exit()

    elif token.text() in ['INNUM', 'INSTR']:
        variable_name = line[1].text()
        if token.text() == 'INNUM':
            value = grin.innum()
        if token.text() == 'INSTR':
            value = grin.instr()
        variable_dict[variable_name] = value

    # Basic Commands
    elif token.text() == 'END':
        exit()

    elif token.text() == 'PRINT':
        var = line[1].text()
        if var.startswith('"') and var.endswith('"'):
            print(var[1:-1])
        elif var in variable_dict:
            print(variable_dict[var])
        else:
            print('TypeError: Not a valid parameter')
            exit()

    # Arithmetic Operations
    elif token.text() in ['ADD', 'SUB', 'MULT', 'DIV']:
        var = line[1].text()
        num = line[2].value()
        # If the var or num is a variable
        if num in variable_dict:
            num = variable_dict[num]
        if var in variable_dict:
            var_value = variable_dict[var]
            # Checking operation
            if token.text() == 'ADD':
                new_value = grin.add(var_value, num)
                variable_dict[var] = new_value
            elif token.text() == 'SUB':
                new_value = grin.subtract(var_value, num)
                variable_dict[var] = new_value
            elif token.text() == 'MULT':
                new_value = grin.multiply(var_value, num)
                variable_dict[var] = new_value
            elif token.text() == 'DIV':
                new_value = grin.divide(var_value, num)
                variable_dict[var] = new_value

    # Control Flow and Subroutines
    elif token.text() in ['GOTO', 'GOSUB']:
        # Holds the result of the IF statement
        result = False
        # If it includes an IF command
        var1 = line[3]
        var2 = line[5]
        # Accounting for variables and values
        if var1 in variable_dict:
            var1 = variable_dict[var1]
        else:
            var1 =  var1.value()
        if var2 in variable_dict:
            var2 = variable_dict[var2]
        else:
            var2 = var2.value()
        relational_op = line[4].value()
        # Checks if the relational operation is True or False
        result = grin.relational_operation(var1, var2, relational_op)

        if result is True:
            if token.text() == 'GOTO':
                pass
            elif token.text() == 'GOSUB':
                pass
    return variable_dict


__all__ = [
    label_check.__name__,
    label_execute.__name__
]
