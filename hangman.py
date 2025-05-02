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
        self.lives = 0

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
        guess = input("Please enter your guess. > ")
        try:
            guess = guess.lower()
        except Exception as e:
            print(f"{e}")
        if len(guess) == 1:
            self.one = True
            print(guess)
            return guess
        elif len(guess) > 1:
            self.one = False
            print(f"you are guessing the entire word: {guess}")
            # immediately tries the word for simplicity
            if guess == self.word:
                print("You guessed correctly! You win!")
            return guess
        else:
            print("empty input, try again.")
            return False

    def validate_guess(self, guess):

        if guess in self.letters:
            self.correct.append(guess)
            return self.correct
        else:
            print("incorrect! you lost a life")
            self.lives -= 1
            return False

    def print_corrent_letters(self):
        i = 0
        for letter in self.letters:

            if letter in self.correct:
                print(f"{letter}", end=' ')
            else:
                print("_", end=' ')
        print('\n')

    def track_lives(self):
        if self.lives == 0:
            return False
        else:
            return True

    def has_won(self):
        x = 0
        for letter in self.letters:
            if letter in self.correct:
                x += 1
        if x >= len(self.letters):
            print('Game over! you have won!!')
            return False
        else:

            return True


'''
TODO: display the hangman/correct number of spaces
input validation and decapitalization
allow for guesses
validate guesses
count number of guesses
check victory

'''

hangman = Hangman(secret_word)

print(hangman.letters)
print(hangman.word)
hangman.display_game_empty()
hangman.display_blanks()
runner = True
while runner:
    console.print(Rule("[bold red] New turn [/bold red]"))
    guess = hangman.get_guess()
    hangman.validate_guess(guess)
    hangman.print_corrent_letters()
    hangman.track_lives()
    runner = hangman.has_won()
