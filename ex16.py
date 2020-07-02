from sys import argv

script, filename = argv
#the following three lines are tiny strings that refference the argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#input variable tied to what seems like nothing. I think this is more for effect to stop the program asking if you wish to continue
input("?")
#simple little string
print("Opening the file...")
#this line opens the file "filename" and creates a file object with the perameter "w" and assigned it to the variable target
target = open(filename, 'w')
#simple string
print("Truncating the file. Goodbye!")
#using the function truncate to delete the contents of the file object assigned to target
target.truncate()
#simple string
print("Now I'm going to ask you for three lines.")
#strings with inputs assigned to variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#simple string
print("I'm going to write these to the file.")
#using the function write to write new text with the user input assigned to the new line variables using refferences
formatter = "{}\n{}\n{}"

target.write(formatter.format(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#simple string
print("And finally, we close it.")
#using close function to close the file object
target.close()

#all of the lines below were added as part of a study drill to read the newly edited file

#printing a simple string on a new line
print("\nNow let's see our new file!")
#simple string
print("Just type in the file name again: ")
#assigning a user input to the variable file_again
file_again = input("> ")
#using the open function on the variable file_again and creating a file object and assining it to the variable newtarget
newtarget = open(file_again)
#simple string to create space because I wasn't sure how to include the escape sequence \n
print(" ")
#using the read function on the newtarget variable with no parameters and printing the newly edited file
print(newtarget.read())
