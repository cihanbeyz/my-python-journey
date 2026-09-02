#interactive mode:
#In this mode you just type python in terminal and then use it...
#as instant outputer just put input and you get your outpuy instantly
#like is say print("Hi Meoww"), enter you get the result there...
#and you can do math calculotar from it ...

age = int(input("What's Your Age: "))
height = int(input("What's Your Height: "))

def can_ride(height,age):
    if height >= 7 :
        return "You are giant for this ride"
    elif height < 4 or age < 5 :
        return "Sorry, You'r too small for this ride kido."
    elif height <= 5 or age <= 12:
        return "You can ride with an adult." 
    elif height > 5 or age > 12 :
        return "You can ride alone!"
    else: 
        return "Input User Detail, Please." 
sea = can_ride(height,age)
print(sea)

#Fizz Buzz

def fizzBuzz_ultra(n):
    if n==0:
        return "Zero is not allowed"
    elif n <0 :
        return "Negitive are not allowed"
    elif n%3==0 or n%5==0 :
        return "FizzBuzz"
    elif n%3 == 0 :
        return "Fizz"
    elif n%5 == 0 :
        return  "Buzz"
    elif n%7 == 0 :
        return "Bazz"
    else:
        return "7"

ei = int(input("What's Your Number? "))
xei = fizzBuzz_ultra(ei)
print(xei)

# The calculator with match

def calculate(a,b,operation):
    
    match operation:

        case "add":
            return a+b
    
        case "substract":
            return a-b
    
        case "multiply":
            return a*b
        case  "divide":
            if  b==0 :
                return "ERROR!!!"
            else:
               return a/b
        case  "modulo":
            return a%b 
        case _ :
            return "invalid operation"
a = int(input("What's The Value Of a: "))
b = int(input("What's The Value Of : "))
operation = input("What's The Operation You Wanna Perform: ")

xim = calculate(a,b,operation)
print(xim)



    
