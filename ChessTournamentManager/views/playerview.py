# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:34:08 2022

"""


from tinydb.table import Document

class PlayerView:
    """ Display informations about players"""
    def __init__(self):
        pass

    def show_player(self,player:Document) -> None:
        """ Player by id """

        print(f"Id : { player['id'] }")
        print(f"First name : { player['first_name'] }")
        print(f"Last name : { player['last_name'] }")
        print(f"Elo's points : { player['elo_points'] }")

    def list_players(self, players):
        """ List of all the players """
        for player in players:
            player = dict(player)
            print(f"Id : { player['id'] }")
            print(f"First name : { player['first_name'] }")
            print(f"Last name : { player['last_name'] }")
            print(f"Elo's points : { player['elo_points'] }")
