class Character:
    def __init__(self, char, was_guessed=False):
        if type(char) != str or len(char) != 1:
            raise ValueError("Only one letter/character, please.")
        self.char = char
        self.was_guessed = was_guessed

    def player_guess(self, guess):
        if not self.was_guessed and guess == self.char:
            self.was_guessed = True

    def show_char(self):
        if self.was_guessed:
            return self.char
        else:
            return "_"

    def __str__(self):
        return self.char
