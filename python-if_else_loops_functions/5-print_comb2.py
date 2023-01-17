#!/usr/bin/python3
print('{:02d},'.format(0), end=' ')
for i in range(1, 99):
    print('{:02d},'.format(i), end=' ')
print('{:02d}'.format(99))