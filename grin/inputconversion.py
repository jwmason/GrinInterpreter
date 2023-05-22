"""This module is in charge of reading input and converting it into a token list of lists"""

import grin


# This function cannot be tested because it requires input, so it will not be included in coverage
def get_input() -> list:
    """This function asks for input until it receives a '.' and adds all converted input to a list"""
    grin_token_list = []
    # Terminal accepts input until user input is '.'
    while True:
        cmd = input()
        if cmd == '.':
            break
        grin_token_list.append(generator_to_token([cmd]))
    return grin_token_list


def generator_to_token(cmd) -> list:
    """This function turns a generator into a list of tokens"""
    grin_token_list = []
    # parse the command
    grin_generator_list = grin.parse(cmd)
    for token in grin_generator_list:
        grin_token_list.append(token)
    return grin_token_list


__all__ = [
    get_input.__name__,
]