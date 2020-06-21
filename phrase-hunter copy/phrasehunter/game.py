import random
from .phrase import Phrase


def get_guess():
    while True:
        try:
            guess = input("Please guess a letter: ").lower()
            if guess.lower() == "quit":
                return guess
            elif not guess.isalpha() or len(guess) != 1:
                raise ValueError
            return guess
        except ValueError:
            print("Please enter only 1 letter.")


class Game:
    def __init__(self, phrases):
        self.lives = 5
        self.play = True
        self.phrases = [Phrase(i) for i in phrases]
        self.current_phrase = random.choice(self.phrases)

    # Guess getter

    # Remaining phrase that hasn't been guessed yet
    def remaining_phrase(self):
        remaining_phrase = []
        for i in self.current_phrase.char_list:
            if i == " ":
                remaining_phrase.append(" ")
            else:
                remaining_phrase.append("_")
        return " ".join(remaining_phrase)

    # Guess setter
    def set_guess(self, guess):
        self.current_phrase.guess(guess)
        return self.current_phrase.show_phrase()

    def run_game(self):
        already_guessed = []
        phrase = self.current_phrase.char_list
        show_guess = self.remaining_phrase()
        print("Welcome to Phrase Hunters! Guess the phrase! \nType \"quit\" to quit.\n {}".format(show_guess))
        self.set_guess(" ")
        while '_' in show_guess and self.lives > 0:
            guess = get_guess()
            # guess.upper() gets the first letters in the phrases because they're capitalized
            if guess.upper() == self.current_phrase.char_list[0]:
                show_guess = self.set_guess(guess.upper())
            if guess.lower() == self.current_phrase.char_list[0]:
                show_guess = self.set_guess(guess.lower())
            if guess.upper():
                show_guess = self.set_guess(guess.lower())
            if guess == "quit":
                print("Thanks for playing!")
                break
            if guess in already_guessed:
                print("\nPlease try a letter that hasn't been guess yet. \"{}\" has already been guessed".format(guess))
            if guess.lower() not in phrase and guess not in already_guessed:
                self.lives -= 1
                print("\"{}\" is not in this phrase. You have {} tries left. Please try again.".format(guess, self.lives))
            if guess not in already_guessed:
                already_guessed.append(guess.lower())
                already_guessed.append(guess.upper())
            print(" ".join(show_guess))

            if "_" not in show_guess and self.lives > 0:
                again = input("\nGood job! You guessed the phrase! Would you like to play again? (y/n): ").lower()
                if again[0] == "y":
                    self.lives = 5
                    self.current_phrase = random.choice(self.phrases)
                    already_guessed = []
                    phrase = self.current_phrase.char_list
                    show_guess = self.remaining_phrase()
                    print("\nType \"quit\" to quit.\n {}".format(show_guess))
                    self.set_guess(" ")
                    continue
                elif again[0] == "n":
                    print("Thanks for playing!")
                    break
                else:
                    print("Please type a y or n.")
                    pass
            elif "_" in show_guess and self.lives == 0:
                again = input("\nAw man! You lost! Would you like to play again? (y/n): ").lower()
                if again[0] == "y":
                    self.lives = 5
                    self.current_phrase = random.choice(self.phrases)
                    already_guessed = []
                    phrase = self.current_phrase.char_list
                    show_guess = self.remaining_phrase()
                    print("\nType \"quit\" to quit.\n {}".format(show_guess))
                    self.set_guess(" ")
                    continue
                elif again[0] == "n":
                    print("Thanks for playing!")
                    break
                else:
                    print("Please type a y or n.")
                    pass
