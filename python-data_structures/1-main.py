#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

list = [1, 2, 3]
idx = 0
print("Element at index {:d} is {:d}".format(idx, element_at(list, idx)))