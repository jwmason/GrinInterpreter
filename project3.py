# project3.py
#
# ICS 33 Spring 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin


def main() -> None:
    # test = ['LET A 1']
    # test = grin.parse(test)
    # for test in test:
    #     print(test)
    test = grin.get_input()
    print(test)
if __name__ == '__main__':
    main()
