#!/usr/bin/python3
for n in range(10):
    for c in range(n + 1, 10):
        if n == 8 and c == 9:
            print("{}{}".format(n, c))
        else:
            print("{}{}".format(n, c), end=", ")
