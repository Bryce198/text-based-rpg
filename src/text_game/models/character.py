

# Character Model

# This is the base character model that all game 
# characters inherit from.
class Character:
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int) -> None:
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.speed = speed

    def take_damage(self, damage) -> None:
        self.health -= (damage - self.defense)

    def attack(self, target) -> int | dict | None:
        target.take_damage(self.attack_power)
        
        

    def is_alive(self):
        alive = True
        if self.health <= 0:
            alive = False
        return alive

    def __repr__(self) -> str:
        return f"name: {self.name}, health: {self.health}, level: {self.level}"