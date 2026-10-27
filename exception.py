# try:
#     x = int(input("Enter the number: "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():

    while True:
        try:
            z = int(input("Enter the x : "))
        except ValueError:
            print("X can't be integer ")
        else:
            print(f"x is {z}")
            break
    return z
main()