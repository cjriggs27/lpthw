from sys import argv
#this line assigns arguments to be used for the argv
script, user_name, dog_name = argv
#this line assigns the variable prompt a value of '> ' so we can set the variable to whatever input we want
prompt = '* '

#these following strings greet the user and refference the argv values given in the command line
print(f"\nHi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
#this line assigns the user input to the variable likes
likes = input(prompt)
#this line was added as part of a study drill. I had to add an additional argument and therefore use an additional string and variable to tie our extra user input to the final string
print(f"Is it true that you have a dog named {dog_name}?")
dog = input(prompt)

#this string refferences the argv values given in the command line
print(f"Where do you live {user_name}?")
#this line assigns the user input to the variable lives
lives = input(prompt)

#this line is a string asking the user what kind of computer they have
print("What kind of computer do you have?")
#this line assigns the user input to the variable computer
computer = input(prompt)

#This multiple line string uses the """ and refferences the variables based on the user inputs from the previous lines of code in order to sum up all the the information given to the program
print(f"""
Alright, so you said {likes} about liking me. You said {dog} when asked if you have a dog named {dog_name}.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
