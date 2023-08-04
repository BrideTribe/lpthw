# number of available cars
car = 100 

# space available in each of the cars
space_in_a_car = 4

# number of drivers available
drivers = 30

# passengers available
passengers = 90

# calculate cars that are not driven
cars_not_driven = car - drivers

# number of cars driven
cars_driven = drivers

# the total passenger the available cars can carry
carpool_capacity = cars_driven * space_in_a_car

# total passenger a car can carry
average_passengers_per_car = passengers / cars_driven


print("There are", car, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")
