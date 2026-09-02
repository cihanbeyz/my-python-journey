#DEFINE FUNCTION: 
# This is use to create your own function to save time and from headache
        # like if you want something again n again in your output you can define a function and call that function
        # whenever you need that
        #why we use def funtion??
        #we use def function bcz if we have random data like a huge messy data we can 
        #just split that data or set a boundry for example if we want specific data we will define main() function
        #and then where in the botton you wrap your data just call that funtion for example main()
        #


def Yobibi(to="Meow Meoww" ):  #RN "Meow Meoww" is defaulf value of "to" variable it will work when don't input #empty parentheses means this function has nothin yet.... we can add here our arguments... in quotes to print like "hello Momo" or anything we want in our output but have to use default parameters as we use to as variable...
        print("Ya Habibi" ,to)        #"to" is here our default parameter that will print here user input like he will type his name...   #now here we described our funtion here. as now i wanna print "Ya habibi"
                                 
name = input("is something bothering you?: ")  

Yobibi(name)             #here we can't put two positional argument like in quotes until you define them above you should define parameters then you call them and than comma one it will give try it ()"Hello!!", name)
  


def bkup(to="Input Something Plz "):     # So i wrote code twice cz i wanna tell you this if you ain't input anything then there should be some caution like " input somethin.. " so you can check the code
        print("Heloo",to)


name = input("Wht's Your input: ")
print(name)
bkup()


def guess():
    lol = int(input("what's your number?"))    #here we define a varible in our function name "guess" & we change variable type into integar cz in "IF & ELSE condition" won't work when user put real "50" that will still show correct not incorrect cz it was "50" string "50" not= 50
    return lol

def main():
    lol = guess()                    #here should be confusion like we are using guess variable multiple times so we should get error> but we don't it is bcz those variables are in different function so can't be refer as same variables...
    if lol == 50:               #so so!! same varible (Like "guess" variable here) in different function are taken as different variables so we can use same variables in diff function                                                                                                                                                                
        print("Incorrect")            

    else:
        print("correct")

main()
















