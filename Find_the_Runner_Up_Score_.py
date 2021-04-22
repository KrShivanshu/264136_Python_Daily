if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

max  = -9999999
max2 = -9999999
for i in arr:
    if(i>max):
        max2=max
        max=i
    elif i>max2 and max>i:
        max2=i

print(max2)