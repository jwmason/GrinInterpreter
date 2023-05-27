"""This module executes the grin tokens with its equivalent Python statements"""

from grin.inputcommands import innum, instr
from grin.arithmeticcommands import add, subtract, multiply, divide
from grin.labels import label_check
from grin.gotogosubcommands import target_conditional
from grin.letcommand import let


def set_labels(grin_token_list, label_dict = {}):
    for line in grin_token_list:
        # Setting Identifier Token
        current_line = 0
        current_line += 1
        token = line[0][0]

        # Labels - LET, GOTO, GOSUB
        new_label_dict = label_check(token, line, label_dict)
        label_dict.update(new_label_dict)

        # Variable Setting
        if token.text() == 'LET':
            new_variable_dict, new_label_dict = let(line, {}, label_dict, current_line)
            label_dict.update(new_label_dict)
    return label_dict


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def run(grin_token_list, variable_dict = {}, label_dict = {}, line_dict = {}, start=None, stop=None):
    """This function takes the token list and executes all commands"""
    # Setting variables
    list_len = len(grin_token_list)
    label_dict = set_labels(grin_token_list)
    grin_token_list = grin_token_list[start:stop]
    current_line = 0
    # return_list = get_return(grin_token_list)
    # Running through each Grin line
    for line in grin_token_list:
        # Setting current line and Identifier Token
        current_line += 1
        token = line[0][0]

        # Labels - LET, GOTO, GOSUB
        new_label_dict = label_check(token, line, label_dict)
        label_dict.update(new_label_dict)

        # Variable Setting
        if token.text() == 'LET':
            new_variable_dict, new_label_dict = let(line, variable_dict, label_dict, current_line)
            variable_dict.update(new_variable_dict)
            label_dict.update(new_label_dict)

        elif token.text() in ['INNUM', 'INSTR']:
            variable_name = line[0][1].text()
            if token.text() == 'INNUM':
                value = innum()
            if token.text() == 'INSTR':
                value = instr()
            variable_dict[variable_name] = value

        # Basic Commands
        elif token.text() == 'END':
            exit()

        elif token.text() == 'PRINT':
            var = line[0][1].text()
            if var.startswith('"') and var.endswith('"'):
                print(var[1:-1])
            elif var in variable_dict:
                print(variable_dict[var])
            else:
                raise Exception('TypeError: Not a valid parameter')

        # Arithmetic Operations
        elif token.text() in ['ADD', 'SUB', 'MULT', 'DIV']:
            var = line[0][1].text()
            num = line[0][2].value()
            # If the var or num is a variable
            if num in variable_dict:
                num = variable_dict[num]
            if var in variable_dict:
                var_value = variable_dict[var]
                # Checking operation
                if token.text() == 'ADD':
                    new_value = add(var_value, num)
                    variable_dict[var] = new_value
                elif token.text() == 'SUB':
                    new_value = subtract(var_value, num)
                    variable_dict[var] = new_value
                elif token.text() == 'MULT':
                    new_value = multiply(var_value, num)
                    variable_dict[var] = new_value
                elif token.text() == 'DIV':
                    new_value = divide(var_value, num)
                    variable_dict[var] = new_value

        # Control Flow and Subroutines
        elif token.text() in ['GOTO', 'GOSUB']:
            target_line = None
            target_line = target_conditional(line, variable_dict, line_dict, list_len, current_line)
            if target_line is not None:
                if token.text() == 'GOTO':
                    run(grin_token_list, variable_dict, label_dict, line_dict, target_line-1)
                    break
                elif token.text() == 'GOSUB':
                    run(grin_token_list, variable_dict, label_dict, line_dict, target_line-1)
                    break
            else:
                raise Exception('Target does not meet requirements')

        elif token.text() == 'RETURN':
            run(grin_token_list, variable_dict, label_dict, line_dict, target_line)

__all__ = [
    run.__name__
]