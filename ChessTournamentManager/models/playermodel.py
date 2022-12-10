# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:00:18 2022

@author: m


"""


from tinydb import TinyDB
from tinydb.table import Document


class PlayerModel:
    """Player class and all his attributes"""

    def __init__(self, idp: str, first_name: str, last_name: str,
                 elo_points: int, date_of_birth: str, gender: str,
                 rank: str) -> None:
        """Constructor"""

        self.idp = idp
        self.first_name = first_name
        self.last_name = last_name
        self.elo_points = elo_points
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank

    @staticmethod
    def get_players():
        """Return all the players of the table players"""
        db = TinyDB('db.json')
        return db.table('players').all()

    @staticmethod
    def get_player_by_id(idp: int) -> Document:
        """Return player details for a precise id"""
        db = TinyDB('db.json')

        print('\nDetails of player :', idp)
        return db.table('players').get(doc_id=idp)
