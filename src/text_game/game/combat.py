from text_game.models.enemies import EnemyParty, Enemy
from text_game.game.party import Party
from text_game.models.player import PlayerHero
from text_game.models.companion import Companion
from typing import TYPE_CHECKING
lazy import questionary
from questionary import Choice
import random



class CombatBattle():
    def __init__(self, player_party: Party, enemy_party: EnemyParty) -> None:
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.combined_parties = []

        self.combined_parties.extend(player_party.members)
        self.combined_parties.extend(enemy_party.ep)

        self.combined_parties = sorted(
            self.combined_parties,
            key=lambda character: character.speed,
            reverse=True
        )


    def battle(self):
        enemy_list = []
        party_list = []
        enemy_count = 0
        for char in self.combined_parties:
            if isinstance(char, Enemy):
                enemy_list.append(char)
                enemy_count += 1
            elif isinstance(char, PlayerHero) or isinstance(char, Companion):
                party_list.append(char)
        
        print(f'Battle has started! there are {enemy_count} enemies!')
        
        
        for char in self.combined_parties:
            if isinstance(char, PlayerHero) or isinstance(char, Companion):
                print(f'{char.name}\'s turn!')
                enemy_select = char.select_enemy(enemy_list)
                if enemy_select in enemy_list: 
                    char.execute_command(enemy_select)





    def __iter__(self):
        return iter(self.combined_parties)

    


