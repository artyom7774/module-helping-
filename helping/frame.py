class Settings(object):
    def new(frame: object, alignment: int = 1, elements: list or tuple = None):
        for number in range(len(frame.list)):
            element = frame.list[number]
            if element != '%straight%' and element != '%none%':
                var = 0
                for selected in elements:
                    if selected != number:
                        var += 1
                    if var >= len(elements):
                        break
                else:
                    if frame.size > len(element) + 1:
                        if alignment == 1:
                            pass
                
                        elif alignment == 2:
                            have = frame.size - len(element) - 2
                            var = ''
                            for i in range(have // 2):
                                var = var + ' '
                            element = var + element + var
                            if len(element) > frame.size:
                                var = len(element)
                                element = element[:var-1]
                    
                        else:
                            var = len(element)
                            var1 = ''
                            for i in range(frame.size - var - 2):
                                var1 = var1 + ' '
                            element = var1 + element
                        frame.list[number] = element


class Frame(object):
    def __init__(self, size: int, list: list or tuple):
        self.size = size
        self.list = list
        self.list_size = len(self.list)
        self.out = []
        self.frame = ['╔', '═', '╗', '╠', '═', '╣', '║', ' ', '║', '╚', '═', '╝']

    def create(self):
        out = self.frame[0]
        for i in range(self.size - 2):
            out = out + self.frame[1]
        out = out + self.frame[2]
        self.out.append(out)
        for element in self.list:
            if element == '%straight%':
                out = self.frame[3]
                for i in range(self.size - 2):
                    out = out + self.frame[4]
                out = out + self.frame[5]
                self.out.append(out)

            elif element == '%none%':
                out = self.frame[7]
                for i in range(self.size - 2):
                    out = out + self.frame[8]
                out = out + self.frame[9]
                self.out.append(out)

            else:
                out = self.frame[6]
                out = out + element
                for i in range(self.size - len(element) - 2):
                    out = out + self.frame[7]
                out = out + self.frame[8]
                self.out.append(out)

        out = self.frame[9]
        for i in range(self.size - 2):
            out = out + self.frame[10]
        out = out + self.frame[11]
        self.out.append(out)

    def print(self):
        for element in self.out:
            print(element)

    def elem_print(self, number: int):
        try:
            print(self.out[number])
        except IndexError:
            print('Number is not defined')
            
    def get_list(self):
        return self.list

    def new(self, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12):
        self.frame = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

    def frame_print(self):
        var = 0
        for i in range(4):
            for k in range(3):
                print(self.frame[var] + ' ', end='')
                var += 1
            print()
        
        
if __name__ == '__main__':
    frame = Frame(30, ['1', '2', '3', '%straight%', '5']) # size list size horizontally
                                                          # list what will be inside the frame, list also accepts:
                                                          # %straight% - horizontal line
                                                          # %none% - empty line
                                                          
    Settings.new(frame, alignment=2, elements=[1, 2]) # Sets the settings for an object of class Frame
                                                      # frame - an object of class Frame
                                                      # alignment - arrangement of elements: 1 - left, 2 - center, 3 - right
                                                      # elements - the lines to which the change will be applied
                                              
    frame.create()   # Create a frame
    frame.new('|', '-', '|', '-', '-', '-', '|', ' ', '|', '-', '-', '-') # Change the components of the frame (after that, you need to call create())
    
    frame.print() # Frame drawing
                  # if the length of the element in the list is greater than the length of the frame, then this line will become larger
                  # since create() is not called again, the frame is drawn with the usual settings
                  
    frame.elem_print(0) # Drawing the 1st line, the first and last line will be: ╔═══╗
    frame.elem_print(1) #
    frame.elem_print(4) #                                                        ╚═══╝
                        # Will print "Number is not defined" if element does not exist


    
