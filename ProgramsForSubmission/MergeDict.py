""""
Write a Python script to merge two Python dictionaries.
"""
dict1 = {  'Rahul': 4, 'Ram': 9, 'Jayant' : 10 }
dict2 = {  'Jonas': 4, 'Niel': 9, 'Patel' : 10 }
dict3 = {  'John': 8, 'Naveen': 11, 'Ravi' : 15 }

print("Before merging")
print("dictionary 1:", dict1)
print("dictionary 2:", dict2)
print("dictionary 3:", dict3)

dict3 = {**dict1, **dict2, **dict3}
print("after updating :")
print(dict3)