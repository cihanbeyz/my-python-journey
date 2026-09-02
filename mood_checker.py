# Problem 01 (Mood Checher)

def mood_check(input):
    if "happy"  in input:
        return f"Keep smiling! ;)"
    elif ("sad") in input:
        return f"Don't Be Sad :("
    else:
        return f"Don't understand that mood ,but stay happy :)"

hey = input("How are you feeling today?").lower().strip()

x = mood_check(hey)
print(x)


# Problem 02 (Funtion OF Daily Reading Decider)

import math

def nova(a,b):
    c = int(a/b)
    if b == 0:
        return "You should at least one page a day"
    else:
        return math.ceil(c) 
    
    
    return f"it will take you {c} days to finish the book."

x = int(input("how many total pages? "))
y = int(input("how many pages you can read per day? "))
    
print(nova(x,y))


# Problem 03 (Random SHi)

name = input("Enter Your Full Name: ")
name = name.title().strip()

def main():
    z = (name).split()
    print(z)

main()
            



