a = (2,3,23,"A",True,23,43,53,43,64,3,3,5,3)

print(type(a))

i = a.index(3)      #here we have use index that is the methode of tuple it will tell where is the 
                    # word is like 3 is on index 1 and also on 11,12,14 index it will stop right there
                    # when it'll find the first 3 and will tell its index
x = a.count(43)     # It'll count all the 43 in whole index that are 2

print(i)
print(x)

y = a*3
print(y)        #it'll print your tuple 3 times 

print(3 in a)  # to check if there is 3 in your tuple

