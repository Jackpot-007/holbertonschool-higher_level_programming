#!/usr/bin/python3
"""Define a function that prints a text with 2 new lines \
    after each of these characters: ., ? and :"""

def text_indentation(text):
    """Prints a text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for t in ".:?":
        text = (t + "\n\n").join(
            [line.strip(" ") for line in text.split(t)])

    print(text, end="")
