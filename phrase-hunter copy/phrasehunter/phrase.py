from .character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = []
        self.char_list = list(phrase)

        for i in phrase:
            self.phrase.append(Character(i))

    def guess(self, guess):
        for i in self.phrase:
            i.player_guess(guess)

    def show_phrase(self):
        guesses = []
        for i in self.phrase:
            guesses.append(i.show_char())
        return guesses




