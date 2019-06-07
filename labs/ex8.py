#sets formatter to {} {} {} {}
formatter = "{} {} {} {}"
# its just telling the console to print 1234 in a different way
print(formatter.format(1, 2, 3, 4))
#this is also just another way of making the console speak
print(formatter.format("one", "two", "three", "four"))
#
print(formatter.format(True, False, False, True))
#
print(formatter.format(formatter, formatter, formatter, formatter))
#tells the console to say whats in the quotes starting from ( ending at )) in line 18
print(formatter.format(

     "gamer time",
     "game time ending",
     "this is a poem",
     "or a song gamers"
 ))