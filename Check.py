a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e)

my_list = [[1,2,3,4] for i in range(2)]
print(my_list[1][0])

x =2
x = x==x
print(x)

my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)