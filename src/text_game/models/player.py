from text_game.models.character import Character
from text_game.models.enemies import Enemy
import random

class Hero(Character):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, role: str, move_list: list) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, move_list)
        self.exp = 0
        self.to_next_level = 25
        self.role = role
        self.equipment = {}

    def level_up(self):
        self.level += 1
        self.to_next_level *= 2

        self.max_health += 10
        self.health += 10
        self.attack_power += 6
        self.defense += 3
        self.speed += 4
        

    def gain_exp(self, exp):
        if exp < 0:
            raise ValueError('Experience cannot be negative')
        self.exp += exp
        while self.exp >= self.to_next_level:
            self.exp -= self.to_next_level
            self.level_up()
            print(f'{self.name} leveled up to {self.level}!')
            print(f'New stats:\n\nAttack: {self.attack_power}\nDefense: {self.defense}\nSpeed: {self.speed}\nHealth: {self.max_health}')
            print(f'To next level: {self.to_next_level}\n')


    def attack(self, target):
        if not target.is_alive():
            print(f"{target.name} has already been defeated")
            return 0

        
        damage = super().attack(target)
        if not target.is_alive():
            self.gain_exp(target.exp_drop)
            print(f'{target.name} has been defeated!')

        return damage

    def is_alive(self):
        return super().is_alive()

    def __repr__(self) -> str:
        return f'Name: {self.name}\nRole({self.role})\nLevel: {self.level}'
        

class PlayerHero(Hero):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, role, move_list=[])
        self.gold = 0
        self.inventory = []
        




