from text_game.models.character import Character

class Enemy(Character):
    def __init__(self, name: str, health: int, attack_power: int, defense: int, level: int, speed: int, exp_drop: int) -> None:
        super().__init__(name, health, attack_power, defense, level, speed)
        self.exp_drop = exp_drop
