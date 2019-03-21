#setting values to words to use later
name = 'Zed A. Shaw'
age = 35 # this isnt my age but its the authors so
height = 74 # inches
weight = 180 # pounds / Ibs
eyes = 'Blue'
teeth = 'white'
hair = 'brown'
# 10 - 15 using the words from eariler and using them in code to make the console to make a sentence
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky says author
# what this line is doing is adding everything up together but also
# its converting it to centimeters and kilograms >:)
total = age + height * 2.54 + weight / 2.205
#this line is just stating what everything adds up to in the console
print(f"If I add {age}, {height}, and {weight} I get {total}.")