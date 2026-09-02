# To print a quote to specify the word like "Meoww Meoww Meoww" as it is in quotes...
# but but if we use double quotes two times or single quotes two times it will give error...
# cz computer realize it's real quotes if we use quotes two times of same type...
# it will think it's start and end of argument... that is wrong for double quotes two times

name = input( "What's your Name?? ")

print("'Maula Mery Maula Mery'")
print('"Meoww Meoww"')

# As we know we use the quotes to print the argument same as it is in output...
# But If Use F'string means f before the string f"I love {Name}" like computer will take it as special sting..

print(f"Hello {name} ",name)

# follwing function Remove wide space from str of When use enter his name with sapces like "     david" he put alot space in interface...
name = name.strip()      # We can have argument in this parentheses{}...

print("Hello!!",name)

# following function Captialize first letter of user name
name = name.capitalize()

print("Hello!!",name)

# following function capitalize first letter of all words
name = name.title()
print(f"Hi Lol {name}")
#OR 
# We can combile them all like following...
# in this the name which user enter, stores in name of these combine function, computer stripe the space...stripe(), then capitalize each word...title()
name= name.strip().title()  

#You know we can add so many function like this i'm talking abt strip and capitalize one 
#but don't put too much function on a single line... just put them on multiple lines for better looking

# Split a string into substrings like... Splite user's name into first name and last name...
name = name.split(" ")    #we put space into doubles quotes that is an argument cz we wanna split joint name into first and last name
print("Hi Lol,",name)

