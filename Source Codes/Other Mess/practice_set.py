# name = input("What's Your Name ??:  ")

# print("Good Afternoon,",name+"!!")
# print(f"Good Afternoon {name}!!")

Letter = '''Dear <Name> \n \t You'r selected \n <Date> '''

xi = Letter.replace("<Name>","Mubi").replace("<Date>","24 Sep 2001")

print(Letter.find("selected"))

print(xi)       #Here we catch the value that we have changed but one thing that needs to be rembember that string are immutable.
print(Letter)
