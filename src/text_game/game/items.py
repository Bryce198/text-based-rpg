class Item:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def use_item(self, user, target):
        raise NotImplementedError(f'Must be implemented by child classes')

    def show_description(self):
        print(f'{self.description}')


class DamageItem(Item):
    def __init__(self, name: str, description: str, damage: int) -> None:
        super().__init__(name, description)
        self.damage = damage

    def use_item(self, user, target):
        if self not in user.inventory:
            return f'{user.name} does not have this item'
        print(f'{user.name} uses {self.name} on {target.name}')
        print(f'It causes {self.damage - target.defense} damage!')
        
        return target.take_damage(self.damage - target.defense)


class HealingItem(Item):
    def __init__(self, name: str, description: str, healing_amount: int) -> None:
        super().__init__(name, description)
        self.healing_amount = healing_amount

    def use_item(self, user, target):
        if self not in user.inventory:
            return f'{user.name} does not have this item'
        print(f'{user.name} uses {self.name} on {target.name}')
        print(f'{target.name} heals for {self.healing_amount} hp')

        return target.heal(self.healing_amount)