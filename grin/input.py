"""This module is in charge of reading input and storing it into a list"""

import grin


# This function cannot be tested because it requires input, so it will not be included in coverage
def get_input() -> list:
    """This function asks for input until it receives a '.' and converts all input to
    grin tokens and adds all tokens to a list"""
    grin_token_list = []
    while cmd := input() != '.':
        grin_token = grin.parse(cmd)
        grin_token_list.append(grin_token)
    return grin_token_list

__all__ = [
    get_input.__name__
]