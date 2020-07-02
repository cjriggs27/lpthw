#using a function to turn the formatter variable into other strings
formatter = "{} {} {} {}"
#this line assigns the .format values to the formatter variable
print(formatter.format(1,2,3,4))
#this line assigns the .format values to the formatter variable
print (formatter.format( "one", "two", "three", "four"))
#this line assigns the .format values to the formatter variable
print(formatter.format(True, False, False, True))
#this line assigns the .format values to the formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))
#this line assigns the .format values to the formatter variable
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or song about fear"
))
