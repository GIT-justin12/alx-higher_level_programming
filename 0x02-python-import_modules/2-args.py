#!/usr/bin/python3
import sys

if __name__ == '__main__':

    """Prints the argument list passed to the program.
    The program takes all the arguments starting from the second
    and prints the number of arguments and their value.
    """
    arg_array = sys.argv
    arg_array_len = len(arg_array) - 1

    if arg_array_len > 1:
        print(arg_array_len, 'arguments:')
        for i in range(1, arg_array_len + 1):
            print('{:d}: {}'.format(i, arg_array[i]))
    elif arg_array_len == 1:
        print(arg_array_len, 'argument:')
        for i in range(1, arg_array_len + 1):
            print('{:d}: {}'.format(i, arg_array[i]))
    elif arg_array_len == 0:
        print(arg_array_len, 'arguments.')
