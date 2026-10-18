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
                self.reserves.append(member)
                self.members.remove(member)
                print([reserve.name for reserve in self.reserves])
                print(f'{member.name} has been removed from the party')
                return
        print('Party member does not exist')
        return

    def swap_from_reserves(self):
        player_party = [member.name for member in self.members]
        reserves_list = [reserve.name for reserve in self.reserves]
        

        member = input(f'Which member do you want to swap?\n{player_party}\n>')
        if member not in player_party:
            print(f'Member not found. pick a member from the list:\n{player_party}')
            return
        if member == self.leader.name:
            print('Party leader cannot be removed from the party.')
            return

        swapped = input(f'Which member do you want to swap for?\n{reserves_list}\n>')
        if swapped not in reserves_list:
            print(f'Reserve member not found. pick a member from the list:\n{reserves_list}')
            return

        member_index = player_party.index(member)
        reserve_index = reserves_list.index(swapped)

        self.swap_member(member_index, reserve_index)

        print(f'{self.members[member_index]} \n\nwas swapped with\n\n{self.reserves[reserve_index]}\n')
        print(self)
        return

    def swap_member(self, member_index: int, reserve_index: int):
        self.members[member_index], self.reserves[reserve_index] = (
            self.reserves[reserve_index], self.members[member_index]
        )

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