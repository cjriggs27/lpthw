from sys import argv
#setting the structure for the argument value
script, input_file = argv
#this line is creating the function print_all with the argument f
def print_all(f):
    #this line returns a specified number of bytes from the file (in this case the default -1 meaning the whole file)
    print(f.read())
#this line is creating the function rewind with the argument f
def rewind(f):
    #this line uses the seek function with the parameter '0' to move to the start of the file
    f.seek(0)
#this line is creating the function print_a_line with the arguments line_count and f
def print_a_line(line_count, f):
    #this line structures the function to print the line_count followed by using f.readline to read a line from the file f
    print(line_count, f.readline())
#this line creates a file object and assigns it to the variable current_file
current_file = open(input_file)
#simple string followed by the escape sequence \n to space the next line
print("First let's print the whole file:\n")
#using the function print_all with the variable current_file
print_all(current_file)
#simple string
print("Now let's rewind, kind of like a tape.")
#using the function rewind with the variable current_file
rewind(current_file)
#simple string
print("Let's print three lines:")
#assigning the value of 1 to the variable current_line
current_line = 1
#using the function print_a_line with the arguments being the variable current_line and the variable current_file
print_a_line(current_line, current_file)
#this line reassigns the value of the variable current_line to the current value + 1
current_line += 1
print_a_line(current_line, current_file)
#this line reassigns the value of the variable current_line to the current value + 1
current_line += 1
print_a_line(current_line, current_file)
