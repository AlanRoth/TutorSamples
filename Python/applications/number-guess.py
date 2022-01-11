import random
from enum import Enum

class NumberGuess():
    class HighLow(Enum):
        HIGH = 1
        WIN = 0
        LOW = -1
        LOST = -2

    def __init__(self):
        self.number = random.randrange(0, 100)
        self.guesses = 10
        self.string_values = {
            self.HighLow.HIGH : "Too High!",
            self.HighLow.WIN : "You win! The number was {number}".format(number=self.number),
            self.HighLow.LOW : "Too Low!",
            self.HighLow.LOST : "You loose! The number was {number}".format(number=self.number)
        }

    def parse_guess(self, guess: int) -> int:
        if guess > self.number:
            return self.HighLow.HIGH
        elif guess < self.number:
            return self.HighLow.LOW

        return self.HighLow.WIN

    def make_guess(self, guess):
        self.guesses -= 1
        if self.guesses == 0:
            return self.HighLow.LOST
        return self.parse_guess(guess)

    def game_loop(self):
        while self.guesses != 0:
            guess = int(input("Make your guess, you have {guesses} left: ".format(guesses=self.guesses)))
            result = self.make_guess(guess)
            if result == self.HighLow.WIN or result == self.HighLow.LOST:
                return self.string_values[result]
            print(self.string_values[result])

if __name__ == '__main__':
    game = NumberGuess()
    print(game.game_loop())