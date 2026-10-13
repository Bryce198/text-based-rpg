

# Character Model

# This is the base character model that all game 
# characters inherit from.
class Character:
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.speed = speed

        self.character_turn = False

    def take_damage(self, damage: int) -> int:
        true_damage = max(0, damage - self.defense)
        true_damage = min(self.health, true_damage)
        self.health -= true_damage
        return true_damage

    def attack(self, target) -> int:
        if not self.is_alive() or not target.is_alive():
            return 0
        return target.take_damage(self.attack_power)
        
    def is_turn(self) -> bool:
        return self.character_turn

    def start_turn(self) -> None:
        self.character_turn = True
    
    def end_turn(self) -> None:
        self.character_turn = False

    def is_alive(self) -> bool:
        return self.health > 0

    def heal(self, amount: int) -> None:
        self.health = min(self.max_health, self.health + max(0, amount))

    def __repr__(self) -> str:
        return f"name: {self.name}, health: {self.health}/{self.max_health}, level: {self.level}"

