def main (n,c,t="Hello"):
    c= "Ma Boy"
    
    return f"{t} {n} {c}"

x = input ("Your Name? : ")
print ("Ohh ",x)

y = main(x,"lor")
print(y)

z= main(x,"Chipangi","Heyaa") 
print(z)


def magic(a,c,b="YES"):
    c= "NO"
    
    return a,b, c

yea= magic("HEllO",3)
a,b,c = yea

print(f"{a} {b} OR {c}")

