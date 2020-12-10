#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n_arg = len(sys.argv) - 1

    if n_arg == 0:
        print(n_arg, "argument.")
    elif n_arg == 1:
        print(n_arg, "argument:")
    else:
        print(n_arg, "arguments:")
    for i in range(n_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
