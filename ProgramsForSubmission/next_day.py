# Write a Python program to get next d of a given date using if-elif-else
d = int(input("Enter d: "))
m = int(input("Enter m: "))
y = int(input("Enter y: "))

leap_year = False
if y%4==0 or y%100!=0 and y%4==0:
    leap_year = True

if m in (4,6,9,11):
    month_size = 30
elif m == 2:
    if leap_year:
        month_size = 29
    else:
        month_size = 28
else:
    month_size = 31

if d < month_size:
    d += 1
else:
    d = 1
    if m == 12:
        m = 1
        y += 1
    else:
        m += 1

print("Next date is [dd-mm-yyyy] %d-%d-%d" % (d, m, y))
