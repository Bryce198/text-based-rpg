from text_game.models.player import PlayerHero
from text_game.models.enemies import Enemy


def main():
    bjorn = PlayerHero("Bjorn", 100, 100, 10, 1, 10, 'mage')
    goblin = Enemy("Goblin", 100, 60, 0, 1, 2, 100)

    goblin.attack(bjorn)
    print(bjorn)
    bjorn.attack(goblin)
    print(goblin)
    print(bjorn)
    print(bjorn.attack_power)
    print(bjorn.speed)
    print(bjorn.defense)

if __name__ == "__main__":
    main()