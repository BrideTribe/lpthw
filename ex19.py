# define a function called 'cheese_and_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print number of cheese
    print(f"You have {cheese_count} cheeses!")

    # print number of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")

    # other output of the function
    print(f"Man that's enough for a party!")

    # the '\n' creates a new line
    print(f"Get a blanket.\n")

# indicate the beginning of the function
print("We can just give the function numbers directly:")

# calls the 'cheese and crackers' function by passing values directly to it
cheese_and_crackers(20, 30)

# alternatively, declare variables whose values can be passed into the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# the variables are passed into the function instead of direct values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# performs mathematical operation in the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# performs arithmetic operations with the function's variables.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
