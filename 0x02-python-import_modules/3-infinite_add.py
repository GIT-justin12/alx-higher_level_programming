#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_array = sys.argv
    arg_array_len = len(arg_array)
    sum = 0

    if arg_array_len > 1:
        for i in range(1, arg_array_len):
            sum += int(arg_array[i])

    print(sum)
