from __future__ import annotations

from typing import TYPE_CHECKING

from text_game.models.character import Character

if TYPE_CHECKING:
    from text_game.game.party import Party

class Enemy(Character):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, exp_drop: int) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, move_list=[])
        self.exp_drop = exp_drop


class EnemyParty():
    def __init__(self, enemy_party: list[Enemy]):
        self.enemy_party = enemy_party

    def __add__(self, other: Party):
        return self.enemy_party + other.members

    
        