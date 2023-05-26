"""This module is in charge of handling the GOTO and GOSUB commands"""


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


def goto():
    """This function is in charge of performing the goto command"""
    pass


def gosub():
    """This function is in charge of performing the gosub command"""
    pass


__all__ = [
    find_target_line.__name__,
    goto.__name__,
    gosub.__name__
]