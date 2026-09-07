# Problem 01

def main():
    
    ct = float(input("Enter the temperature you wanna know abt: ")) 
    print(check_temp(ct))

def check_temp(temp):
    if temp <= 0 :
        return "Given temperature is freezing point"

    elif temp <= 15:
        return "Given Temperature is cold"
    elif temp <= 30:
        return "Given temperature is warm"
    else:
        return "Hot af" 
main()

# Problem 02 (Discount Calculator)

def main ():
    price = int(input("What's The Price Of Your Product? "))
    discount = calculate_discount(price)
    priceaftrdiscount = price_afterdis(discount,price)
    print(f" Your price after discount is: {priceaftrdiscount}, Your discount is: {discount}")
    
    
def calculate_discount(price):
    
    if price >= 1000:
        return price * 0.20
    elif 500 <= price < 1000:
        return price * 0.10
    else:
        return 0
def price_afterdis(price,discount):
    price_after = price - discount
    return price_after

main()

#Problem 3 Password strenght checker.

def main():
    cs = input("What's The Password? : ")
    print(check_strenght( cs))
    
def check_strenght(password):
    password = len(password)

    if password >= 12:
        return "Strong"
    elif 8 < password < 11:
        return "Medium"
    else:
        return "Weak"

main()



