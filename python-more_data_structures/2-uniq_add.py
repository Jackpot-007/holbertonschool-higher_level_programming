#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_num = []
    total = 0
    for num in my_list:
        if num not in add_num:
            add_num.append(num)
            total += num
    return total
