def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def days_in_month(year, month):
#
# Write your new code here.
#
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [2,4,6,9,11]:
        return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


####

def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def days_in_month(year, month):
#
# Write your new code here.
#
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [2,4,6,9,11]:
        return 30

def day_of_year(year, month, day):
#
# Write your new code here.
#
    if days_in_month(year,month) >= day:
        return year,month,day
    else:
        return None

print(day_of_year(2001, 2, 31))


###################

def is_prime(num):
#
# Write your code here.
#
    count=0
    for i in range(1,(num//2)+1):
        if num%i == 0:
            count+=1
    if count>=2:
        return True
    else:
        return False
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

###############
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
