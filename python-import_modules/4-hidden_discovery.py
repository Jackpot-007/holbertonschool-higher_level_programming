#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    count = len(content)
    for n in range(count):
        if "__" in content[n]:
            continue
        print(content[n])
