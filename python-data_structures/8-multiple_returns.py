#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    m = None

    if length > 0:
        m = sentence[0]

    return (length, m)
