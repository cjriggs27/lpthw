name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height_centimeters = height_inches * 2.54
weight_lbs = 180 # lbs
weight_kgs = weight_lbs * 0.4535924
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"He's {height_centimeters} centimeters tall.")
print(f"He's {weight_lbs} pounds heavy.")
print(f"He's {round(weight_kgs)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_inches + weight_lbs
print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")
