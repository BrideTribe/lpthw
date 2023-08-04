name = 'Victor A Akinnibosun'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
kg_weight = weight * 0.453592 # kilogram
cm_height = height * 2.54 # centimeter
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, this height is approximately {round(cm_height)} centimeters.")
print(f"He's {weight} pounds heavy, this weight is approximately {round(kg_weight)} kilogram.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")