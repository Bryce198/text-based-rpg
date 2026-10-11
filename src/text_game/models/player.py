from text_game.models.character import Character
from text_game.models.enemies import Enemy
import random

PLAYER_CLASSES = {
    'Warrior': {
        "health": 150,
        "attack": 25,
        "defense": 15,
        "speed": 12
    },
    "Mage": {
        "health": 80,
        "attack": 20,
        "defense": 5,
        "speed": 9
    },
    "Ranger": {
        "health": 100,
        "attack": 18,
        "defense": 12,
        "speed": 10
    }
}

class Hero(Character):
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, attack_power, defense, level, speed)  # Assuming a default defense value for human class
        self.exp = 0
        self.to_next_level = 25
        self.role = role

    def level_up(self):
        self.level += 1
        self.to_next_level *= 2
        self.health *= (self.level // 2)
        self.attack_power *= (self.level // 2)
        self.defense *= (self.level // 2)
        self.speed *= (self.level // 2)
        

    def gain_exp(self, exp):
        self.exp += exp

    def attack(self, target):
        if not target.is_alive():
            print(f"{target.name} has already been defeated")
            return None
        
        damage = super().attack(target)
        super().attack(target)
        if not target.is_alive():
            self.gain_exp(target.exp_drop)
            print(f'{target.name} has been defeated')
            while self.exp >= self.to_next_level:
                self.level_up()
                print(f"{self.name} has leveled up!")
                print(f'Exp needed for next levelup: {self.to_next_level}')

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": damage
        }

    def is_alive(self):
        return super().is_alive()

    def __repr__(self) -> str:
        return super().__repr__()


class Companion(Hero):
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, attack_power, defense, level, speed, role)
        self.equipment = {}
        self.exp = 0
        self.to_next_level = 25
        

class PlayerHero(Hero):
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, attack_power, defense, level, speed, role)
        self.exp = 0
        self.to_next_level = 25
        self.gold = 0
        self.inventory = []
        self.equipment = {}
        




