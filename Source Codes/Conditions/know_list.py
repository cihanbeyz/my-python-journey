Fruits = []

f1 = input("enter fruit number : ")
Fruits.append(f1)
f2 = input("enter fruit number : ")
Fruits.append(f2)
f3 = input("enter fruit number : ")
Fruits.append(f3)
f5 = input("enter fruit number : ")
Fruits.append(f5)
f5 = input("enter fruit number : ")
Fruits.append(f5)
f6 = input("enter fruit number : ")
Fruits.append(f6)
print(Fruits)


Marks = []

f1 = int(input("enter number of student: "))
Marks.append(f1)
f2 =int( input("enter number Of student: "))
Marks.append(f2)
f3 = int(input("enter number Of student: "))
Marks.append(f3)
f5 = int(input("enter number Of student: "))
Marks.append(f5)
f5 = int(input("enter number Of student: "))
Marks.append(f5)
f6 = int(input("enter number Of student: "))
Marks.append(f6)
Marks.sort()                            #sort the list
print(Marks)

#Tuple can't be changed see how...
a = (34,3.14,"Fanchise","Ramin",None)
# a(3) = "Rin"  #here we try to replace/modify the Fanchise with Rin
print(a)

L = [123,23,45,23,45]
print(sum(L))

a = [0,0,0,1,2,2,2,2,2,55,5]
n = a.count(2)
print(n)
