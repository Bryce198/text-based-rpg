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
        self.reserves = []

    def add_member(self, member: Companion | PlayerHero):
        if len(self.members) <= 3:
            self.members.append(member)
            print(f'{member.name} was added to the party')
            return
        print(f'Party is Full!, {member.name} is being moved to reserves.')
        self.reserves.append(member)
        return
        

    def remove_member(self):
        party_list = []
        for party_member in self.members:
            party_list.append(party_member.name)
        member_name = input(f'Which party member do you want to remove:\n{party_list}\n>')
        if member_name == self.leader.name:
            print('Party leader cannot be removed')
            return
        for member in self.members:
            if member_name == member.name:
                self.members.remove(member)
                print(f'{member.name} has been removed from the party')
                return
        print('Party member does not exist')
        return

    def swap_from_reserves(self):
        member = input('Which member do you want to swap?')
        
        for party_member in self.members:
            if member not in party_member.name:
                print('Member not found in party')
            else:
                pass
            

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
        alive_list = []
        defeated = False
        for member in self.members:
            if member.is_alive():
                alive_list.append(member)

        if len(alive_list) == 0:
            defeated = True

        return defeated