"""This module executes the grin tokens with its equivalent Python statements"""

from grin.inputcommands import innum, instr
from grin.arithmeticcommands import add, subtract, multiply, divide
from grin.relationaloperationcommands import relational_operation
from grin.labels import label_check, label_execute
from grin.gotogosubcommands import find_target_line


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def run(grin_token_list, start = None, stop = None):
    """This function takes the token list and executes all commands"""
    variable_dict = {}
    label_dict = {}
    line_dict = {}
    list_len = len(grin_token_list)
    grin_token_list = grin_token_list[start:stop]
    for line in grin_token_list:
        # Setting current line
        current_line = 0
        # Setting Identifier Token
        token = line[0][0]

        # Labels - LET, GOTO, GOSUB
        new_label_dict = label_check(token, line, label_dict)
        for key, value in new_label_dict.items():
            if not key in label_dict:
                label_dict[key] = value

        # Variable Setting
        if token.text() == 'LET':
            variable = line[0][1].text()
            value = line[0][2].value()
            if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                variable_dict[variable] = value
            elif isinstance(value, str):
                # Check if the value is a label
                if value in label_dict:
                    variable_dict[variable] = label_dict[value]
                    label_dict[variable] = current_line
                    new_variable = label_execute(variable_dict[variable], variable_dict, label_dict)
                    for key, value in new_variable.items():
                        if key in variable_dict:
                            variable_dict[key] = value
                        else:
                            variable_dict[key] = value
                else:
                    raise Exception('TypeError: Not a valid parameter')
            elif isinstance(value, (int, float)):
                variable_dict[variable] = value
            else:
                raise Exception('TypeError: Not a valid parameter')

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
            # Holds the result of the IF statement
            result = False
            # If it includes an IF command
            if len(line) == 6:
                var1 = line[0][3]
                var2 = line[0][5]
                # Accounting for variables and values
                if var1 in variable_dict:
                    var1 = variable_dict[var1]
                else:
                    var1 =  var1.value()
                if var2 in variable_dict:
                    var2 = variable_dict[var2]
                else:
                    var2 = var2.value()
                relational_op = line[0][4].value()
                # Checks if the relational operation is True or False
                result = relational_operation(var1, var2, relational_op)
            if (result is True) or (len(line) == 1):
                target = line[0][1].value()
                target_line = find_target_line(target, line, line_dict)
                if token.text() == 'GOTO':
                    pass
                elif token.text() == 'GOSUB':
                    pass

        # Next line
        current_line += 1


__all__ = [
    run.__name__
]