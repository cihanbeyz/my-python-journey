def main():
    n = input("what's Your Number?")

def countdown(n):       #parameters
    if n<=0:
        return "Blast OFf"

    print (n)
    
    return countdown(n - 1)

def waima(sadness,happiness,lessmoreless):
    sadness = input("Your mood? ")
    happiness = input("Your swings: ")
    return f"Are you sure... you okay? you are saying {sadness}. Just smile and avoid this short statment -> {happiness}"
meh = shit(2,4,3)       #positional arguments
print(meh)
main()

def custom_greet(name,greeting="Hello"):
    return f"{greeting}, {name}"


print(custom_greet("Alex!"))            #1

meoww = custom_greet("Alex","Heyaa")
print(meoww)                            #2

print(custom_greet("Alex!","Sup"))      #3


def math_machine(a,b,operation="add"):
    if operation== "add" :
        return a+b
    if operation=="substract" :
        return a-b
    if operation=="multipy" :
        return a*b
    if  operation=="divide" :
        if b == 0 :
            return "ERRORL Can't divide by Zero! "
        else: 
            return a/b
    else:
        return "invalid operation! "

print(math_machine(10,5,"add"))
print(math_machine(10,5,"substract"))
print(math_machine(10,5,"divide"))
print(math_machine(10,0,"divide"))
print(math_machine(10,34,"module"))



