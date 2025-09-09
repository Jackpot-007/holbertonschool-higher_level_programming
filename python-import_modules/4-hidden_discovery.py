#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    content = dir(hidden_4)
    count = len(content)
    for i in range(count):
        if "__" in content[i]:
            continue
        print(content[i])
