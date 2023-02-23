class Crafts(object):
    def __init__(self, crafts: list = []) -> None:
        self.crafts = crafts

    def have(self, craft: str, inventory: object, base: object = None) -> bool:  # craft - name craft
        pass

    def get(self) -> list:
        return self.crafts
