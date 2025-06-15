print("Welcome to the rollercoster")

height = int(input("What is your height?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")
    photos = input("Do you want photo?")
    if photos == "Y":
        bill += 3
    print(bill)
else:
    print("Sorry you have to grow taller before you can ride.")


