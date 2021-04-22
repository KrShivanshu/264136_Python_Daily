"""
Write a python program to check the user input abbreviation.
If the user enters "lol", print "laughing out loud".
If the user enters "rofl", print "rolling on the floor laughing".
If the user enters "lmk", print "let me know".
If the user enters "smh", print "shaking my head".
"""

word = input("Enter a word: ")
if word == "lol":
    print("laughing out loud")
elif word == "rofl":
    print("rolling on the floor laughing")
elif word == "lmk":
    print("let me know")
elif word == "smh":
    print("shaking my head")
else:
    print("Wrong word entered, abbreviatin not found!")

