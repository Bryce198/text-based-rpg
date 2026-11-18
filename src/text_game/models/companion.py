from text_game.models.player import Hero

class Companion(Hero):
    def __init__(self, name: str, health: int, mp: int, attack_power: int, defense: int, level: int, speed: int, role: str,
                 move_list: list, inventory: list) -> None:
        super().__init__(name, health, mp, attack_power, defense, level, speed, role, move_list, inventory)
        self.control_mode = 'Manual'

    def switch_control_mode(self):
        if self.control_mode == 'Manual':
            self.control_mode = 'Auto'
        elif self.control_mode == 'Auto':
            self.control_mode = 'Manual'

    def use_ai_command(self, target):
        print(f'{self.name}\'s turn!')
        if target is None:
            print('No target selected')
            return
        if not target.is_alive():
            return
        if not self.is_alive():
            print(f'{self.name} is knocked out!')
            return
        self.attack(target)
        return

    def execute_turn(self, target):
        if self.control_mode == 'Manual':
            self.execute_command(target)
        elif self.control_mode == 'Auto':
            self.use_ai_command(target)
        
         
            