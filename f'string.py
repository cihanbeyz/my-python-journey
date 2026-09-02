#one thing to remember that in parentheses ((())) computer process first inner parentheses data then outer one...so on
# like:
# int(input("Enter the value of X: "))    #first the inner parentheses then the outer one

# x = input("Enter the value of X: ")
# y = input("Enter the value of Y: ")

# z = int(x) + int(y)

# print("Substraction of digits: ")

#print(int(input("What's the value of X: ")) + int(input("What's the value of X: ")))

x= float(input("What's the first number:"))
y= float(input("What's the second number:"))
z= int(x/y)   #want result in integar

 print(z)
"""For flout values as we know we use float and if you input in decimal
 but you don't want answer in decimal their is function called round..."""
#  FORMULA OF ROUND: round(number[, ndigits])

# z = round(x/y)    
z = round(x*y,2) #why 2 after x*y?? to move decimal to the left side of output as see the formula of function gotcha...
print(z)       

# SO SO..actually f'string called as formate string is good for numbers...
# like we can formate messy numbers in proper formate like seprate by commas etc Let's see how..

 print(f"{z:,}")     #here we use colon to describe what to put(it's "","" so its gonna be shown in numbers) and f'sting for formating...now result will be in formating
print(f"{z:2f}")     #weird?? yeah but it's also the alternate of round function, By formate sting(or f'sting) we can do multiple task...
                    #in this we use 2f to move decimal two digits left side as round function...

#  CONCLUSION: We can slove problems by multiple ways...
# ONE IMPORTANT NOTE: we use f'string to inject variables or calculations without breaking the string apart...
# then we put our calculation or variable in curly brackets{}... ONE MORE BENIFIT: f'string convert numbers,lists
# booleans, everthing into text for you... 
# we are not limited to just variables can do calculations {age*2} or {name.upper(age)} or {score-50}
# f'string also use in return function like  :  return f"welcome back, {user}!"

