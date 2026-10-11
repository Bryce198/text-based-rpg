from text_game.models.player import PlayerHero, Companion
from text_game.models.character import Character

class Party():
    def __init__(self, leader: PlayerHero) -> None:
        self.leader = leader
        self.members = []
        self.members.append(self.leader)

    def add_member(self, member: Companion):
        if len(self.members) < 4:
            self.members.append(member)

    def remove_member(self, member: Companion):
        if member is self.leader:
            return 'Party leader cannot be removed'

        if member in self.members:
            self.members.remove(member)
        else:
            return 'Party member does not exist'

        return f'{member} has been removed from the party'

    def get_party_members_state(self):
        status = None
        for member in self.members:
            if member.is_alive():
                status = 'Alive'
            else:
                status = 'Injured'
            print(f'Party member: {member.name}\n Status: {status}')

    def is_defeated(self):
        pass