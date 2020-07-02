#lines 2-4 use argv to get a filename from the user
from sys import argv

script, filename = argv
#this line uses the command open to open the specific file and that open file object is assigned to the variable txt
txt = open(filename)
#this line prints a little string using a refference
print(f"Here's your file {filename}:")
#this line prints a read command for the variable txt without parameters
print(txt.read())
#this line prints a string
print("Type the filename again:")
#this line assigns the user input to the variable file_again
file_again = input("> ")
#this line assigns the open commanded variable file_again to the variable txt_again
txt_again = open(file_again)
#this line prints a read command for the variable txt_again without parameters
print(txt_again.read())
