print("Welcome to the Treasure Island")
direction = input("Where do you wanna go, right or left? R or L: ")

if direction == "L":
    next_step = input("Swim or Wait? S or W: ")
    if next_step == "W":
        door = input("Which door, red, blue or yellow? R, B, Y?")
        if door == "Y":
            print("You win!")
        else:
            print('Game Over')
    else:
        print('Game Over')  
else:
    print('Game Over')            
