types_of_people = 10 # types of people
x = f"There are {types_of_people} types of people." # create an f-string variable

binary = "binary" # declare a sring variable
do_not = "don't" # create a string variable
y = f"Those who know {binary} and those who {do_not}." # f-string variable

print(x) # this print a f-string variable
print(y) # print f-string variable

print(f"I said: {x}") # print an f-string x in another f-string
print(f"I also said: '{y}'") # print an f-string y in another f-string

hilarious = True # create a binary variable
joke_evaluation = "Isn't that joke so funny?! {}" # a variable with an empty f-string locator

print(joke_evaluation.format(hilarious)) # add format to an already created string and print

w = "This is the left side of..." # create a string variable w
e = "a string with a right side." # create a string variable e

print(w + e) # this is string concatenation