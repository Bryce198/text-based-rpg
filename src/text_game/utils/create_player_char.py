from text_game.models.player import PlayerHero, PLAYER_CLASSES

def create_player_char():
    name = input('Enter the name for your character:\n')
    char_class = input('Choose your character class (Warrior/Mage/Ranger):').strip().title()

    while char_class not in PLAYER_CLASSES:
        char_class = input('Invalid class. Choose again:').strip().title()

    stats = PLAYER_CLASSES[char_class]

    
