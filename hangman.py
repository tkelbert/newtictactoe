import random
import time
from rich import print
from rich.console import Console
from rich.rule import Rule

console = Console()

word_list = ["python", "javascript", "programming", "computer", "science"]
secret_word = random.choice(word_list)


class Hangman:
    def __init__(self, word):
        self.word = word
        letters = []
        for char in self.word:
            letters.append(char)

        self.letters = letters

        self.one = False
        self.correct = []
        self.lives = 6

    def display_game_empty(self):
        print("=============")
        print("---HANGMAN---")
        print("=============")
        print("   _____   ")
        print("   |   |   ")
        print("   |       ")
        print("   |       ")
        print("___|___    ")

    def display_blanks(self):
        for char in self.word:
            print(f"_", end=' ')
        print('\n')

    def get_guess(self):
        guess = input("Please enter your guess. > ").lower()
        if len(guess) == 1:
            self.one = True
            return guess
        elif len(guess) > 1:
            self.one = False
            return guess
        else:
            print("empty input, try again.")
            return False

    def validate_guess(self, guess):
        if guess in self.letters:
            self.correct.append(guess)
            return True
        else:
            print("incorrect! you lost a life")
            self.lives -= 1
            return False

    def print_correct_letters(self):
        for letter in self.letters:
            if letter in self.correct:
                print(f"{letter}", end=' ')
            else:
                print("_", end=' ')
        print('\n')

    def track_lives(self):
        return self.lives > 0
    def has_won(self):
        return len(self.correct) == len(self.letters)
    def print_man(self):
        head = 'O'
        neck = '|'
        left = '-'
        right = '-'
        ll = '/'
        rl = '\\\\'
        body = []
        if self.lives == 6:
            self.display_game_empty()
            return
         # Calculate the number of errors (parts to show)
        errors = 6 - self.lives

        # Determine what character to display for each part
        # If the number of errors is high enough, show the part, otherwise show a space.
        display_head = head if errors >= 1 else ' '
        display_torso = neck if errors >= 2 else ' '  # Using neck as torso center
        display_left_arm = left if errors >= 3 else ' '
        display_right_arm = right if errors >= 4 else ' '
        display_left_leg = ll if errors >= 5 else ' '
        display_right_leg = rl if errors >= 6 else ' '
 # Print the hangman structure using the display characters
        print("   _____   ")
        print("   |   |   ")
        # Print the head row
        print(f"   |   {display_head}   ")
        # Print the arms/torso row - note alignment
        print(f"   |  {display_left_arm}{display_torso}{display_right_arm}   ")
        # Print the legs row - added a space between legs for clarity when only one is shown
        print(f"   |  {display_left_leg} {display_right_leg}   ")
        print("___|___   ")
        print("   |   [ ]   ")
        print("___|___   ")
        
cTODO: None
'''

hangman = Hangman(secret_word)

print(hangman.letters)
print(hangman.word)
hangman.display_game_empty()
hangman.display_blanks()

while hangman.track_lives():
    console.print(Rule("[bold red] New turn [/bold red]"))
    guess = hangman.get_guess()
    if not guess:
        continue
    hangman.validate_guess(guess)
    hangman.print_correct_letters()
    if hangman.has_won():
        print("Game over! You have won!")
        break

    hangman.print_man()
    console.print(f"Lives: {hangman.lives}")

while hangman.track_lives():
    console.print(Rule("[bold red] New turn [/bold red]"))
    guess = hangman.get_guess()
    hangman.validate_guess(guess)
    hangman.print_corrent_letters()
    hangman.track_lives()
    runner = hangman.has_won()
    hangman.print_correct_letters()
    if hangman.has_won():
        print("Game over! You have won!")
        break

    hangman.print_man()
    print(hangman.lives)
    console.print(f"Lives: {hangman.lives}")
