"""
Write a Python program to find the second smallest number in a list
"""


n = int(input())
arr = map(int, input().split())

min  = 9999999
min2 = 9999999
for i in arr:
    if(i<min):
        min2=min
        min=i
    elif i<min2 and min<i:
        min2=i

print(min2)