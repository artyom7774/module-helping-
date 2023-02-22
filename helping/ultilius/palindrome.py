class Palindrome(object):
    def __init__(self, text) -> None:
        self.text = text.lower()
        self.size = len(self.text)

    def get(self) -> bool:
        result = True

        for i in range(self.size // 2):
            var1 = self.text[i]
            var2 = self.text[self.size - 1 - i]

            if var1 == var2:
                pass
            else:
                result = False
            
        return result

if __name__ == '__main__':
    var = input('Enter a word: ')
    pal = Palindrome(text=var)

    print(f'{var}: {pal.get()}')
