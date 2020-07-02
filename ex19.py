#this line creates the function "cheese_and_crackers" with the arguments "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #this line is a simple string with a reference of cheese_count
    print(f"You have {cheese_count} cheeses!")
    #this line is a simple string with a reference of boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #simple string
    print("Man that's enough for a party!")
    #simple string followed by the escape sequence \n to ensure the line following the end of the function is blank
    print("Get a blanket.\n")

#simple string
print("We can just give the function numbers directly:")
#the function cheese_and_crackers with the arguments defined as "20" and "30"
cheese_and_crackers(20, 30)

#simple string
print("OR, we can use variables from our script:")
#variables assinged to the values 10 and 50
amount_of_cheese = 10
amount_of_crackers = 50
#the function "cheese_and_crackers" with the above variables "amount_of_cheese" and "amount_of_crackers" as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#simple string
print("We can even do math inside too:")
#the function "cheese_and_crackers" with the arguments defined as the summation of two given numbers
cheese_and_crackers(10 + 20, 5 + 6)

#simple string
print("And we can combine the two, variables and math:")
#the function "cheese_and_crackers" with the arguments defined as the summation of the previously defined variables (found on lines 20 and 21) and given numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
