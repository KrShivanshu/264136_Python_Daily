"""
Write a python program to check if the input number is
- real number
- float numner
- string
- complex number
- Zero (0)
"""

user_input = 0.0
input_type = type(user_input)
if input_type==type(9) and not user_input == 0:
    print("Integer")
elif input_type == type(9.0):
    print("Float")
elif input_type==type(2+2j):
    print("Complex Number")
elif input_type==type("String"):
    print("String")
elif user_input == 0:
    print("Zero")