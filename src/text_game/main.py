from text_game.models.player import PlayerHero
from text_game.models.companion import Companion
from text_game.game.party import Party
from text_game.utils.display_menu import display_title_menu
from text_game.models.enemies import Enemy, EnemyParty
from text_game.game.skills import cut
from text_game.game.combat import CombatBattle


def main():
    #display_title_menu()
    bryce = PlayerHero('Bryce', 100, 15, 15, 10, 1, 10, 'Warrior', move_list=[cut], inventory=[])
    party = Party(bryce)
    # niel = Companion('Niel', 100, 12, 12, 40, 20, 1, 'Mage')
    gedra = Companion('Gedra', 120, 30, 25, 10, 1, 11, 'Wizard', move_list=[cut], inventory=[])
    # mike = Companion('Mike', 120, 15, 10, 10, 1, 20, 'Paladin')
    gorm = Enemy('Gobbie', 10, 10, 5, 0, 1, 5, 200)
    # lisire = Companion('Lisire', 100, 40, 20, 30, 1, 20, 'Mage')
    party = Party(bryce)
    razz = Enemy('Gorb', 60, 30, 18, 10, 3, 20, 35)
    #bryce.move_list.append(cut)
    #bryce.execute_command(gorm)
    #print(gorm)
    #niel.use_ai_command(gorm)
    #print(gorm.is_alive())
    enemy_party = EnemyParty()
    enemy_party.ep.append(gorm)
    enemy_party.ep.append(razz)
    party.add_member(gedra)
    battle = CombatBattle(party, enemy_party)
    #print(battle.combined_parties)
    battle.battle()





    
    
    


if __name__ == "__main__":
    main()