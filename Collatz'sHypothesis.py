""" Write a program which reads one natural number and executes 
the above steps as long as c0 remains different from 1. 
We also want you to count the steps needed to achieve the goal. 
Your code should output all the intermediate values of c0, too.
"""
c0 = int(input("Enter a number: "))
step = 0
while c0!=1:
    if c0%2==1:
        c0=3*c0+1
    else:
        c0=c0/2
    print(int(c0))
    step=step+1

print(step)