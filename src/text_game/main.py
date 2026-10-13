from text_game.models.player import PlayerHero
from text_game.models.companion import Companion
from text_game.game.party import Party
from text_game.utils.display_menu import display_title_menu


def main():
    #display_title_menu()
    bryce = PlayerHero('Bryce', 100, 30, 10, 1, 10, 'Warrior')
    party = Party(bryce)
    niel = Companion('Niel', 0, 40, 20, 1, 10, 'Rogue')
    gedra = Companion('Gedra', 120, 25, 10, 1, 11, 'Wizard')
    mike = Companion('Mike', 120, 10, 10, 1, 20, 'Paladin')
    print(party)
    party.remove_member('Bryce')
    party.add_member(niel)
    print(party)
    party.get_party_members_state()

if __name__ == "__main__":
    main()