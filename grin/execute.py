"""This module executes the grin tokens with its equivalent Python statements"""

from grin.inputcommands import innum, instr
from grin.arithmeticcommands import add, subtract, multiply, divide


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def run(grin_token_list):
    """This function takes the token list and executes all commands"""
    variable_dict = {}
    grin_token_list = grin_token_list
    for line in grin_token_list:
        token = line[0][0]

        # Variable Setting

        if token.text() == 'LET':
            variable = line[0][1].text()
            value = line[0][2].value()
            variable_dict[variable] = value

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
                raise TypeError('Not a valid parameter')

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
                    return add(var_value, num)
                elif token.text() == 'SUB':
                    return subtract(var_value, num)
                elif token.text() == 'MULT':
                    return multiply(var_value, num)
                elif token.text() == 'DIV':
                    return divide(var_value, num)

__all__ = [
    run.__name__
]