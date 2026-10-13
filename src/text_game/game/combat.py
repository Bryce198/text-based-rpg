from text_game.models.enemies import EnemyParty
from text_game.game.party import Party
from typing import TYPE_CHECKING



class CombatBattle():
    def __init__(self, player_party: Party, enemy_party: EnemyParty) -> None:
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.combined_parties = (*self.player_party, *self.enemy_party)
        self.turn_order = []

    def battle(self):
        self.turn_order = 

    def __iter__(self):
        return iter(self.combined_parties)

    def __add__(self, player_class: Party, enemy_party: EnemyParty):
        return player_class + enemy_party


