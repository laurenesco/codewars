# 8 kyu
# https://www.codewars.com/kata/55e8aba23d399a59500000ce

class Hero:
    def __init__(self, name: str = "Hero") -> None:
        self.name = name
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0

    def check_alive(health: int) -> bool:
        if health > 0:
            return True
        else:
            return False
