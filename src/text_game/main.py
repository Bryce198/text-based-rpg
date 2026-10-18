from text_game.models.player import PlayerHero
from text_game.models.companion import Companion
from text_game.game.party import Party
from text_game.utils.display_menu import display_title_menu
from text_game.models.enemies import Enemy


def main():
    #display_title_menu()
    bryce = PlayerHero('Bryce', 100, 15, 15, 10, 1, 10, 'Warrior')
    party = Party(bryce)
    niel = Companion('Niel', 100, 12, 12, 40, 20, 1, 'Mage')
    gedra = Companion('Gedra', 120, 30, 25, 10, 1, 11, 'Wizard')
    mike = Companion('Mike', 120, 15, 10, 10, 1, 20, 'Paladin')
    gorm = Enemy('Gobbie', 10, 10, 5, 0, 1, 5, 200)
    lisire = Companion('Lisire', 100, 40, 20, 30, 1, 20, 'Mage')
    print(bryce)
    


if __name__ == "__main__":
    main()