students = ["Harry","Lisa","Jimmy"]

print(students[1])
for student in students:
    print(student)

# for i in range(12):
#     print(i)

for i in range(len(students)):
    print(i + 1, students[i])

lst= ["Lala",342,4.43,True]
lst.insert(3,False)         #we insert false at index 3

x = lst.pop(1)              #we deleted the value of index 1 that is 342
lst.remove(True)            #to use remove we have to give the value of index to remove
print(x)                   #here we printed that deleted index value by giving variable x 
print(lst)                  #here we wil have the remaining list that we modified