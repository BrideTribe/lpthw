people = int(input("How many people are going? \n ->> "))
cars = int(input("How many cars are available? \n ->> "))
trucks = int(input("How many trucks are ready? \n ->> "))

# test if cars are more than people
if cars > people:
    print("We should take the cars.") # print this if the condition is true
elif cars < people: # test if there are more people than cars
    print("We should not take the cars.") 
else: # what to do when the conditions above are not true.
    print("We can't decide.")

# test for condition between trucks and cars.
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")

# compares people and trucks and take decision based on which is true.
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")