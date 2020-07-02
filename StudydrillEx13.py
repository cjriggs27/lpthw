from sys import argv
#This code was written to create a script with more arguments than the example in the 13th exercise of the book
script, name, sister, gf, dog, gfdog, like = argv
#these lines are what prompt the user to input a value to assign to each variable pertaining to the written string
script = input("What is the script name? ")
name = input("What is your name? ")
sister = input("What is your sister's name? ")
gf = input("What is your gf's name? ")
dog = input("What is your dog's name? ")
gfdog = input("What is your gf's dog's name? ")
like = input("What do you like to do? ")

#these lines print the string followed by the varialbe value assigned by the user input
print("\nThis is the name of this script:", script)
print("\nThis is my name:", name)
print("\nThis is my sister's name:", sister)
print("\nThis is my girlfriend's name:", gf)
print("\nThis is my dog's name:", dog)
print("\nThis is my girlfriend's dog's name:", gfdog)
print("\nThis is what I like to do:", like)
