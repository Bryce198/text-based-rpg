from __future__ import annotations

from typing import TYPE_CHECKING

from text_game.models.character import Character

if TYPE_CHECKING:
    from text_game.game.party import Party

class Enemy(Character):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, exp_drop: int) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, move_list=[])
        self.exp_drop = exp_drop

    def use_ai_command(self, target):
            print(f'{self.name}\'s turn!')
            if target is None:
                print('No target selected')
                return
            if not target.is_alive():
                return
            if not self.is_alive():
                print(f'{self.name} is knocked out!')
                return
            self.attack(target)
            return


class EnemyParty():
    def __init__(self):
        self.ep = []

    def add_to_party(self, enemy: Enemy):
        pass

    def __iter__(self):
        return iter(self.ep)