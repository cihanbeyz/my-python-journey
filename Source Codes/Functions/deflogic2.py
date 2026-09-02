def yo (a,b):       #function define
    waimo = a+b     #variable define
    print (waimo)   #print that varible but it'll show nothing here cz we did't assign any value to "a" and "b".
x = yo(5,3)         #1. Here we call the function and assign the value to "a,b" both at same time....         
                    #2. lemme tell you smth if we define a funtion we change the line of our code. like if we print a varible at 2 line and assign value in 3 line it won't show any error...
                    #3. that's the reason we use function cz at last we call the function and everting that is in funtion processed and output shows on screen

print(x)            #1. result would be NONE cz print don't return any value it shows the result and vanish lol
                    #2. i'm talking about above print that already showed the result "8" and vanish
         
        #BUT BUT IF WE USE RETURN FUNTION "IN SAME CODE LEMME SHOW YOU"

def yo (a,b):
    waimo = a+b
    return waimo    # Used return funtion
x= yo(5,7)
print(x)            #now here our output shows 12 cz return funtion don't vanish the output but somehow saves it so we can use them again in whole code... iT'S become a Value Producer!!

    #IMPORT SHEILD:
                    # when you run a file(like myfile.py) directly python gives it a secret internalname "__main__"
                    # when someone IMPORT this file (like ur frnd,checher or any bot) python gives it name of your file(as myfile.py)
def main():
    name = input("Name: ")                    
    print (hello(name) )         #here print our hello function

def hello(n):                   #here we def our own function 'hello' but we already has been use print above to print this function...
    return f"Hello, {n}"

if __name__ == "__main__":      #this is wot python take as our file name... 
    main()

# what happend when we run:
# __name__ is equals "__main__". the if condition is true. it calls main() and your program runs.
# what happened when bot test it??
# the bot wants to test your hello() function, it does an 'import yourfile' (not "__main__")
# this your input("Name: ") line never runs during the test so the bot doesn't get stuck wating for
# you to type something it'll quietly test your hello() and move on.
        ##  So this def function is so important for many purposes...
