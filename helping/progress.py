import time
import os


class Bar(object):
    def __init__(self, size: int, text: str = 'Installing', speed: int or float = 1, frame: str = '|', type: str = '█'):
        self.size = size
        self.text = text
        self.speed = speed
        self.frame = frame
        self.type = type
        self.out = ''
        self.now = 0

    def full_run(self, delete=False):
        self.now = 0
        for k in range(self.size + 1):
            self.out = str(self.text) + str(self.frame)
            for i in range(self.now):
                self.out = self.out + self.type

            for i in range(self.size - self.now):
                self.out = self.out + ' '

            self.out = self.out + self.frame
            self.now += 1

            print(self.out)
            time.sleep(self.speed)
            if delete:
                os.system('cls')
        self.now = 0

    def run(self):
        if self.size > self.now:
            self.out = str(self.text) + str(self.frame)
            for i in range(self.now):
                self.out = self.out + self.type

            for i in range(self.size - self.now):
                self.out = self.out + ' '

            self.out = self.out + self.frame
            self.now += 1

        print(self.out)
        time.sleep(self.speed)

    def part_reset(self):
        self.now = 0


if __name__ == '__main__':
    bar = Bar(size=30, speed=1)  # size - bar size
                                 # text - text before the bar, set "" if you want nothing before the bar
                                 # speed - bar speed, in how many seconds 1 element from size will be filled
                                 # frame - will be before and after elements
                                 # type - element that will fill the bar

    bar.full_run(delete=False) # Prints all stages of the bar
                               # if delete = True, then after each addition of an element, cmd will be cleared

    bar.run() # Print 1 element in turn, to reset use the part_reset() method
    