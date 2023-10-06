#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_arr = sys.argv
    len_arg_arr = len(arg_arr)
    sum = 0

    if len_arg_arr > 1:
        for i in range(1, len_arg_arr):
            sum += int(arg_arr[i])

    print("{}".format(sum))
