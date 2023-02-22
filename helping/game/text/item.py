class Item(object):
    def __init__(self, name: str, display_name: str, rare: int, count: int = 1) -> None:
        self.name = name
        self.display_name = display_name
        self.rare = rare
        self.count = count

    def get(self) -> dict:
        return {"name": self.name, 
                "display_name": self.display_name, 
                "rare": self.rare, 
                "count": self.count
                }
