"""This module executes the grin tokens with its equivalent Python statements"""

from grin.inputcommands import innum, instr
from grin.arithmeticcommands import add, subtract, multiply, divide
from grin.relationaloperationcommands import relational_operation


# Function cannot be tested as it tests the functionality of grin tokens that are unique every time
# the program is run, however each sub part inside the run function is tested.
def run(grin_token_list):
    """This function takes the token list and executes all commands"""
    variable_dict = {}
    grin_token_list = grin_token_list
    try:
        for line in grin_token_list:
            # Setting current line
            current_line = 0
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

                if result is True:
                    if token.text() == 'GOTO':
                        pass
                    elif token.text() == 'GOSUB':
                        pass

    except RuntimeError as e:
        print(e)
        exit()

    # Next line
    current_line += 1


__all__ = [
    run.__name__
]