#To avoid deep nesting , you must need to Guard Clauses (clean)


def check (x):
    if x <= 0 :
        return "Negitive Or Zero not allowed."

    if x % 2 == 0 :                         
        return "Number is Even positive."
    return "Number is Odd positive."

n = int(input("What's x??"))
print(check(n))

#For String And Int

def super_condition(x):
    if x == " ":
        return "Empty"
    elif x == "secret":
        return "Access granted"
    else:
        try :
            num = int(x)
        except ValueError:
            return "Normal"
    
    if num < 0 :
        return "Negitive"
    elif num % 2==0 and num % 5==0:
        return "Devisible by 10"
    elif num % 2==0 or num % 5==0:
        return "Divisible by 2,5"
    else:
        return "Normal"

x = input ("What's x??").lower().strip()
print(super_condition(x))

