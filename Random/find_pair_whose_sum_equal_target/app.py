#!/usr/bin/env python3

def find_pair(array_a, array_b, target):
    result = None # holds final result
    temp = set(array_b)  # transform the 2nd array into a set

    for el in array_a:
        if (target - el) in temp:
            result = [el, (target - el)]
            break
    return result
