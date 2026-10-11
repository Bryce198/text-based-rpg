from text_game.models.player import PlayerHero, Companion
from text_game.models.enemies import Enemy
from text_game.game.party import Party


class Combat():
    def __init__(self, player_party: Party, enemy_party: list[Enemy]) -> None:
        self.player_party = player_party
        self.enemy_party = enemy_party

    def battle(self):
        pass

