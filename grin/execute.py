"""This module executes the grin tokens with its equivalent Python statements"""

from grin.arithmeticcommands import add, subtract, multiply, divide
from grin.parsing import GrinParseError

def run(grin_token_list):
    """This function takes the token list and executes all commands"""
    variable_dict = {}
    grin_token_list = grin_token_list
    for line in grin_token_list:
        token = line[0][0]
        if token.text() == 'LET':
            variable = line[0][1].text()
            value = line[0][2].value()
            variable_dict[variable] = value
        elif token.text() in ['ADD', 'SUB', 'MULT', 'DIV']:
            var = line[0][1].text()
            num = line[0][2].value()
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