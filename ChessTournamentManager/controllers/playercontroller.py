# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 05:51:59 2022

@author: m
"""


from tinydb import TinyDB, where
from models.playermodel import PlayerModel
from views.playerview import PlayerView


class PlayerController:
    """All about players methods index,show,add"""

    def __init__(self):
        pass
        
    @staticmethod
    def index() -> None:
        """index"""
        players =  PlayerModel.get_players()
        PlayerView().list_players(players)

    @staticmethod
    def show(idp:int) -> None:
        """show"""
        player =  PlayerModel.get_player_by_id(idp)
        PlayerView().show_player(player)

    @staticmethod
    def add_player():
        """create a player """
        
        db = TinyDB('db.json')
        players = db.table('players')

        last_id = players.all()[-1]["id"]
        idp = last_id + 1
        first_name = input("Please enter player's first name: ")
        last_name = input("Please enter player's last name: ")
        elo_points = int(input("Please enter player's elo points : "))
        date_of_birth = input("Please enter player's birth date (format = DD/MM/YYYY): ")
        gender = input("Please enter player's gender ('m' / 'f'): ")

        record = ({'id': idp, 'first_name': first_name, 'last_name': last_name,
                 'elo_points': elo_points, 'date_of_birth': date_of_birth,'gender': gender})

        players.insert(record)

        print("\n Player saved .\n")

    @staticmethod
    def update_rank():
        """Update player's elo in the database and in the current tournament."""
        db = TinyDB("db.json")
        players = db.table('players')


        idp=int(input("Player Id to update elo ? "))
        new_elo =int( input("Please enter player's  new elo : "))


        players.update({"elo_points": new_elo}, where("id") == idp)

        select=players.search(where('id')==idp)

        print( 'Elo rank updated from the selected player:\n',select )
            
