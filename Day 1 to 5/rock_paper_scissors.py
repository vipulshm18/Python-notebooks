import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]

choice = random.randint(0, 2)
pc_choice = choices[choice]

user_choice = int(input("0 for Rock, 1 for Paper or 2 for Scissors?"))

if user_choice >= 0 and user_choice < 2:
    print(f"You chose: {choices[user_choice]}")
else: 
    print("Wrong input")
print(f"Computer chose: {pc_choice}")


if user_choice >= 3 or user_choice < 0:
    print('Wrong input, you lose!')
elif user_choice == 0 and pc_choice == 2:
    print('You win!')
elif user_choice == 2 and pc_choice == 0:
    print('You lose!')
elif choice > user_choice:
    print("You lose!")
elif user_choice > choice:
    print('You win!')
elif user_choice == choice:
    print("It's a draw!")
