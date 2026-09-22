students = {
    "Name":"Harry",
    "Lisa":"Jimmy",
}
print(students["Lisa"])

Fruits = {
    "Apple" : "Red",
    "Orange": None,
    "Banana": "Light Green",
    "Mashmellow": "Creamy"
}

for key in Fruits:
    print(Fruits[key])       #Here we use key to get the value of the dictionary. But we can't use key+1 because key is a string and we can't add an integer to a string. So we can just print the key and the value of the dictionary.
    print(key)               #Here we print the key of the dictionary. But we can't use key+1 because key is a string and we can't add an integer to a string. So we can just print the key and the value of the dictionary.

Students= [
    {"Name":"Harry","House":"Petrin","Loci":"New York"},
    {"Name":"Lisa","House":"Monjo","Loci":"None"} ,
    {"Name":"Jimmy","House":"Dead","Loci":"California"},
    {"Name":"Rockie","House":"Champi","Loci":"Texas"},
    
]
for m1 in Students:
    print(m1)           #This will print the whole dictionary inside the list. But we can't use m1+1 because m1 is a dictionary and we can't add an integer to a dictionary. So we can just print the whole dictionary inside the list.
    print(m1["House"])  #This will print the value of the key "House" in the dictionary inside the list. But we can't use m1+1 because m1 is a dictionary and we can't add an integer to a dictionary. So we can just print the value of the key "House" in the dictionary inside the list.

for RI in range(len(Students)): 
    print(RI+1 ,Students[RI]["Name"], Students[RI]["House"], Students[RI]['Loci']) #HERE! we have to use Students[RI] to access the dictionary inside the list and then use the key to get the value.
                                                                                    #Also we use RI+1 to start the ranking from 1 instead of 0. In Dict we call the key to get the value but in list we use index to get the value.
print("The length of the Students list is: ", len(Students)) #Here we use len() to get the length of the list. But we can't use len(Students)+1 because len() returns an integer and we can't add an integer to an integer. So we can just print the length of the list.

print(">"*4,end="") #Here we use ">"*4 to print 4 ">" in a row. But we can't use ">"*4+1 because ">"*4 returns a string and we can't add an integer to a string. So we can just print 4 ">" in a row. We have multiply string with integar to get the string so we can multiply string with integar to get the string.

            #Let's Define A Function To Get The # in Rows N Column

def main():
    kiu = int(input("Enter the height of column:"))
    siu = int(input("Enter the width of the row: "))
    (get_row(siu))
    (get_column(kiu))

def get_row(width):
    print( "?"*width)


def get_column(height):
    print("#"*height)

main()

def main ():
    blocks_row(4,4)
    
    user = int(input("What's should size be: "))
    blocks_column(user)

def blocks_row(width,height):
    for i in range(height):
        for j in range(width):
            print("#", end="")
        print()
def blocks_column(size):
    for i in range(size):
        clown(size)
def clown(width):
    print("#"*width)

main()