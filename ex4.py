#all the code below this comment is setting a value to a number like car and drivers
#also its setting what value cars_not_driven and driven and such afterwards.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
#the error that he made is that he misspelt passengers in line right below this
average_passenger_per_car = passengers / cars_driven
# this is making the console say whats available and whats not
# along with what they have to do today how many people they have to drive and so
print("There are", cars, "available.")
print("There are only", drivers, "drivers available.")
print("There will be ", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")