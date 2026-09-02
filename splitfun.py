# Input Function Where We Enter Our Argument.

name = input("What's Your Name?? : ")

# Say Hello To User

print ( "hello,"end="") # we have used end= function here cz python print function our argument in new line(\n) by default now it'll print the output in a single line
print(name)

# The quotes can be used inside and can be printed if "" dble quotes are outside you can use single quotes inside same for single one can use outside and double inside... 
# Moreover can use backslash for escape character "\"
name = name.split(" ")
print('Hello, name', name) 
