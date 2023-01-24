#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    co = 0
    length = []
    while co < list_length:
        try:
            res = my_list_1[co] / my_list_2[co]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            co += 1
            length.append(res)
    return length
