"""
Write a Python program to find the repeated items of a tuple
"""

tup = (1,3,4,6,6,3,2,5,7,8,5,5,6,7,8)
my_list = []

for i in tup:
    if tup.count(i) > 1:
        if i not in my_list:
            my_list.append(i)

for j in my_list:
    print(j, "repeated", tup.count(j),"times in the given tuple")