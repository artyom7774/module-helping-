class Place(object):
    def __init__(self, inventory: object, size: int, text: str = '*NONE*', speed: int or float = 1, frame: str = '|', type: str = '█', get: list = []) -> None:       
        self.inventory = inventory
        self.size = size
        self.text = text
        self.speed = speed
        self.frame = frame
        self.type = type
        self.get = get
        
    def run(self) -> list:
        from helping.progress import Bar 

        bar = Bar(size=self.size, text=self.text, speed=self.speed, frame=self.frame, type=self.type)
        bar.full_run(delete=True)

        for element in self.get:
            self.inventory.add(element)

        return self.inventory
