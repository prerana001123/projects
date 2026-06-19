import art
print(art.logo6)
import random
answer = random.randint(1,100)
print("Welcome to the number guessing Game!")
print("I'm thinking of a number between 1 to 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
chance = 0
if choice == "easy":
    chance += 10
    print(f"You have {chance} attempts remaining to guess the number.")
else:
    chance += 5
    print(f"You have {chance} attempts remaining to guess the number.")
keep_guessing = True
while keep_guessing:
    guess = int(input("Make a guess: "))
    if guess != answer:
        if guess < answer:
            print("Too low.")
        if guess > answer:
            print("Too high.")
        chance -= 1
        if chance != 0:
            print("Guess again.")
            print(f"You have {chance} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose!")
            keep_guessing = False
    else:
        print(f"You got it! The answer was {answer}. ")
        keep_guessing = False