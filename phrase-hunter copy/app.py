import re
from phrasehunter.game import Game

if __name__ == '__main__':
    # Learned how to open text files with the help of: https://docs.python.org/3/tutorial/inputoutput.html
    with open("phrases.txt") as phrases:
        phrase_list = re.findall(r"[\w?' ]+", phrases.read())
        game = Game(phrase_list)
        game.run_game()
