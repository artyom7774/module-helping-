class Player(object):
    def __init__(self, health: int, max_health: int, damage: int, armor: int = 0, money: int = None) -> None:
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.armor = armor
        self.money = money
