"""
Write a Python program to convert a list into a nested dictionary of keys
"""

my_list = ['a','b','c','d','e']
my_dict = current = {}
for ele in my_list:
    current[ele] = {}
    current = current[ele]
print(my_dict)