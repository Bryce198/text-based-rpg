from __future__ import annotations

from typing import TYPE_CHECKING

from text_game.models.companion import Companion
from text_game.models.player import PlayerHero

if TYPE_CHECKING:
    from text_game.models.enemies import EnemyParty


class Party():
    def __init__(self, leader: PlayerHero) -> None:
        self.leader = leader
        self.members: list[Companion | PlayerHero] = []
        self.members.append(self.leader)

    def add_member(self, member: Companion | PlayerHero):
        if len(self.members) <= 3:
            self.members.append(member)
            return f'{member.name} was added to the party'
        
        return 'The party is full!'

    def remove_member(self, member_name: str):
        if member_name == self.leader.name:
            return 'Party leader cannot be removed'

        for member in self.members:
            if member_name == member.name:
                self.members.remove(member)
                return f'{member.name} has been removed from the party'
        return 'Party member does not exist'

    def get_party_members_state(self):
        status = ''
        for member in self.members:
            if member.is_alive():
                status = 'Alive'
            else:
                status = 'Injured'
            print(f'Name: {member.name}\nStatus: {status}')

    def __add__(self, other:EnemyParty):
        return self.members + other.enemy_party

    def __iter__(self):
        return iter(self.members)

    def __repr__(self) -> str:
        party_list = []
        for member in self.members:
            party_list.append(member.name)
        return f'Party:\n{party_list}'

    def is_defeated(self):
        pass