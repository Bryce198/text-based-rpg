from text_game.models.character import Character
from text_game.models.enemies import Enemy
import random
import questionary
from ..game.skills import DamageSkill, HealingSkill

class Hero(Character):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, role: str, move_list: list[HealingSkill | DamageSkill]) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, move_list)
        self.exp = 0
        self.to_next_level = 25
        self.role = role
        self.equipment = {}
        self.move_list = move_list

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
            print(f'{self.name} grew to level {self.level}!')
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

    def get_battle_command(self):
        return questionary.select(f'{self.name}\'s turn, what will you do?', 
                                  choices=['Attack', 'Defend', 'Use Skill', 'Inventory', 'Run Away']).ask()

    def select_skill(self):
        move_name_list = []
        for move in self.move_list:
            move_name_list.append(move.name)

        return questionary.select(f'What skill would you like to use?', 
                                  choices=move_name_list).ask()

    def use_skill(self, target):
        skill = self.select_skill()
        for move in self.move_list:
            if move.name == skill:
                move.use_skill(self, target)
                if not target.is_alive():
                    self.gain_exp(target.exp_drop)

    def execute_command(self, target):
        command = self.get_battle_command()
        if command == 'Attack':
            self.attack(target)
            return
        elif command == 'Defend':
            self.defense += 10
            print(f'{self.name} is defending!')
            return
        elif command == 'Use Skill':
            self.use_skill(target)
            return 
    
    def is_alive(self):
        return super().is_alive()

    def __repr__(self) -> str:
        return f'Name: {self.name}\nRole({self.role})\nLevel: {self.level}'
        

class PlayerHero(Hero):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, role, move_list=[])
        self.gold = 0
        self.inventory = []
        




