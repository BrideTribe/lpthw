from sys import argv

# read the WYSS section for how to run this
#name, first, second, third = argv

#print("The script is called:", name)
#print("Your first vairable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)
#print(argv)

script, name, age, location, gender = argv

print("This is the script name:", script)
print("Your name is:", name)
print("You are ", age, " years old")
print("You are from:", location)
print("You are a:", gender)

sibling = int(input("Number of siblings? "))
food = input("What is your best food? ")
print("-" * 10)
print(f"I have {sibling} siblings, and my best food is {food}")