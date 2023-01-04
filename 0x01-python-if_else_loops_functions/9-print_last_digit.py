#!/usr/bin/python3
def print_last_digit(number):
        rem = number % 10
        if number < 0:
                rem = number % -10
        if rem < 0:
                rem = -rem
        print("{}".format(rem), end="")

        return 