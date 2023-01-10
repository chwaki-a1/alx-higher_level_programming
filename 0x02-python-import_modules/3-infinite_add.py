#!/usr/bin/python3

if __name__ == "__main__":
    """Print additon of all args."""
    import sys

    n = 0
    for i in range(len(sys.argv) - 1):
        n += int(sys.argv[i + 1])
    print("{}".format(n))
