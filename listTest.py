lists = [1,2,3,4,5]
print(lists[0:-1])
for v in enumerate(lists):
     print(v)
for v in range(2):
     lists.insert(-1,lists[v])

print(lists)

num =  lists
del num[:]
print(num)
print(lists)

def func(a=2,b=3):
     return b**a

print(func(b=2))

lists = [i for i in range(-1,-2)]
print(5 == 6)

#####

# Generators
def countdown():
     i=5
     while i>0:
          yield i
          i-=1

for i in countdown():
     print(i)

# decorator
def decor(func):
     def wrap():
          print("=====")
          func()
          print("=====")
     return wrap

@decor
def print_text():
     print("hello world!")

#print_text = decor(print_text)
print_text()

# recursion
def fib(x):
     if x == 0 or x == 1:
          return 1
     else: 
          return fib(x-1) + fib(x-2)
print(fib(4))

#itertools
from itertools import product, permutations

letters = ("a","b")
print(list(product(letters,range(2))))
print(list(permutations(letters)))