from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the rile. Goodbye!")
target.truncate()

print("I'm now gonna to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1 + "\n" + line2 + "\n" + line3 "\n")


print("And finally, we close it.")
target.closed()