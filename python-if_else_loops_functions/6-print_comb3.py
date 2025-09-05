#!/usr/bin/python3
for n in range(10):
    for c in range(n + 1, 10):
        if n == 8 and c == 9:
            print("{:02d}, {:02d}".format(n, c))
        else:
            print("{:02d}, {:02d}".format(n, c), end=', ')
