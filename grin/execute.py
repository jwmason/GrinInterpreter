"""This module executes the grin tokens with its equivalent Python statements"""

from grin.inputcommands import innum, instr
from grin.arithmeticcommands import add, subtract, multiply, divide


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def run(grin_token_list):
    """This function takes the token list and executes all commands"""
    variable_dict = {}
    grin_token_list = grin_token_list
    try:
        for line in grin_token_list:
            token = line[0][0]

            # Variable Setting

            if token.text() == 'LET':
                variable = line[0][1].text()
                value = line[0][2].value()
                if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                    variable_dict[variable] = value
                elif isinstance(value, (int, float)):
                    variable_dict[variable] = value
                else:
                    print('TypeError: Not a valid parameter')
                    exit()

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
                    print('TypeError: Not a valid parameter')
                    exit()

            # Arithmetic Operations

            elif token.text() in ['ADD', 'SUB', 'MULT', 'DIV']:
                var = line[0][1].text()
                num = line[0][2].value()
                # If the num is a variable
                if num in variable_dict:
                    num = variable_dict[num]
                if var in variable_dict:
                    var_value = variable_dict[var]
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
                # If it includes an IF command
                if len(line) == 6 and line[0][2].text() == 'IF':
                    var1 = line[0][3]
                    var2 = line[0][5]
                    relational_op = line[0][4]
                    if relational_op.text() == '>' or relational_op.text() == '>=':
                        pass
                    elif relational_op.text() == '<' or relational_op.text() == '<=':
                        pass
                    elif relational_op.text() == '=':
                        pass
                    elif relational_op.text() == '<>':
                        pass
                    else:
                        print('TypeError: Relational Operator not a valid parameter')
                        exit()
    except RuntimeError as e:
        print(e)
        exit()


__all__ = [
    run.__name__
]