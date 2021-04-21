""" Your task is to write a program which reads the number of blocks the builders have, 
and outputs the height of the pyramid that can be built using these blocks. """

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height=0
i=1
while i <= blocks:
    if i<=blocks:
        height=height+1
        blocks=blocks-i
        i=i+1
    else:
        break
    

print("The height of the pyramid:", height)
