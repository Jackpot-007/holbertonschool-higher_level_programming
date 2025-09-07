#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    i = 0
    while i < strlen:
        char = ord(str[i])
        if 97 <= char <= 122:
            char -= 32
        print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        i += 1
