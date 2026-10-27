# try:
#     x = int(input("Enter the number: "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

while True:
    try:
        z = int(input("Enter the x : "))
    except ValueError:
        print("X can't be integer ")
    else:
        print(f"x is {z}")
        break
