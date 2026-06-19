import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''', '''
 +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''', '''
 +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''', '''
 +---+
  |   |
  0   |
  |   |
      |
      |
=========
''', '''
 +---+
  |   |
  0   |
      |
      |
      |
=========
''', '''
 +---+
  |   |
      |
      |
      |
      |
=========          
  ''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

correct_word = []
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(letter)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")
    print(stages[lives])