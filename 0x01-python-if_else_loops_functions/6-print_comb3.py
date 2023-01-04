#!/usr/bin/python3
for firstNum in range(0, 10):
    for secondNum in range(firstNum + 1, 10):
        if firstNum == 8 and secondNum == 9:
            print("{}{}".format(firstNum, secondNum))
        else:

            print("{}{}".format(firstNum, secondNum), end=", ")
