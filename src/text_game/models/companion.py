from text_game.models.player import Hero

class Companion(Hero):
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int, role: str) -> None:
        super().__init__(name, health, attack_power, defense, level, speed, role)
        