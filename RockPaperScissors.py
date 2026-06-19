import random
print("Let's play rock paper scissors!")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

user_choice = int(input("What do you choose? type 0 for rock,\n 1 for paper, and 2 for scissors\n"))
print(f"User chose: {user_choice}")
# printing of user's choice
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("  ")
print("  ")
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
# printing of computer's choice
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("  ")
# selection of choices
if computer_choice == 0 and user_choice == 1:
    print("You win!")
elif computer_choice == 1 and user_choice == 2:
    print("You win!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!")
elif computer_choice == user_choice:
    print("The match is draw!")
elif user_choice != 0 and user_choice != 1 and user_choice != 2:
    print("You chose an invalid no. You lose!")
else:
    print("You lose!")