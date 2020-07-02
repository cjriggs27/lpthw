#this line assigns a value to a variable and tabs in that value with the \t escape sequence
tabby_cat = "\tI'm tabbed in."
#this line assigns a value to a variable and starts the rest of the written string to a new line
persian_cat = "I'm split\non a line."
#this line assigns a value to a variable and uses a \\ escape sequence to insert a backslash
backslash_cat = "I'm \\ a \\ cat."
#this line assigns a value to a variable and uses the \t* escape sequence to tab-in and place asterisks next to list items and \n to adjust the rest of the string to the next line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#these next 4 lines are printing the values assigned to each variable
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
