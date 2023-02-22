import random

class Lottery(object):
    def __init__(self, chance: int, min: int = 0, max: int = 100):
        self.min = min
        self.max = max
        self.chance = chance

    def play(self):
        var = random.randint(self.min, self.max)
        if self.chance <= var:
            return True
        else:
            return False


if __name__ == '__main__':
    lottery = Lottery(chance=5, min=0, max=100)  # min - min number
                                                 # max - max number
                                                 # chance - chance return True of 100%
