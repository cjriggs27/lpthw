#variable assigned string of stuff
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#printing a simple string
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# this is a conditional statement saying "While the length of the variable stuff is not equal to 10 the following will happen"
while len(stuff) != 10:
    # assigning the last variable from "more_stuff", using .pop(), to variable "next_one"
    next_one = more_stuff.pop()
    # printing simple string and the variable next_one
    print("Adding: ", next_one)
    #appending the variable "next_one" to the variable "stuff"
    stuff.append(next_one)
    # printing a simple string with the len function specifying the length of the variable "stuff"
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!
