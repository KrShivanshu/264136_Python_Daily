my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


###
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

###
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

###
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here to print Unique elements
#
temp_list = []
for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list
print("The list with unique elements only:")
print(my_list)
