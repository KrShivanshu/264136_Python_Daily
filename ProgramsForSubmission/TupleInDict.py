"""
Write a Python program to convert a list of tuples into a dictionary
"""

def ConvertTupIntoDic(tup, dic):
    for a, b in tup:
        dic.setdefault(a, []).append(b)
    return dic

tup = [("Monday", 1), ("Tuesday", 2), ("Thursday", 3),("Wednesday", 4),
        ("Friday", 5), ("Saturday", 6), ("Sunday", 27)]
dic = {}
print(ConvertTupIntoDic(tup, dic))