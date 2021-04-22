numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


###

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Enter a word: "))
print("Step 3:", beatles)

# step 4
del(beatles[-1])
del(beatles[-1])
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))


###