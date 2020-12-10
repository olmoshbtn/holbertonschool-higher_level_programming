#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print(len(sys.argv) - 1, "arguments:")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, arg))
