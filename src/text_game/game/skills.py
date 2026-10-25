class Skill():
    def __init__(self, name: str, mp_cost: int, description: str):
        self.name = name
        self.mp_cost = mp_cost
        self.description = description


    def use_skill(self, user, target):
        raise NotImplementedError('Subclass must implement the use_skill() method.')

    def show_info(self):
        print(f'{self.description}')


class DamageSkill(Skill):
    def __init__(self, name: str, mp_cost: int, description: str, damage: int):
        super().__init__(name, mp_cost, description)
        self.damage = damage

    def use_skill(self, user, target):
        if user.mp < self.mp_cost:
            print(f'{user.name} does not have enough mp to use {self.name}.')
            return

        damage = max(1, self.damage + user.attack_power - target.defense)
        target.health -= damage
        print(f'{user.name} uses {self.name} on {target.name} for {damage} damage!')
        return


class HealingSkill(Skill):
    def __init__(self, name: str, mp_cost: int, description: str, healing_amount: int):
        super().__init__(name, mp_cost, description)
        self.healing_amount = healing_amount

    def use_skill(self, user, target):
        if user.mp < self.mp_cost:
            print(f'{user.name} does not have enough mp to use {self.name}.')
            return

        target.heal(self.healing_amount)
        print(f'{target.name} was healed for {self.healing_amount} hp!')
        return

cut = DamageSkill('cut', 5, 'The user cuts the target with a blade', 10)
