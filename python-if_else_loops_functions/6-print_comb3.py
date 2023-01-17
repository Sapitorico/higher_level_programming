#!/usr/bin/python3
for i in range(1,10):
    for x in range(1, 10):
        if (i < x):
            print('{:02d},'.format(i), end=' ')