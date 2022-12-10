# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:31:23 2022

@author: m
"""

from tinydb import TinyDB


class PlayerSeeder:
    """class PlayerSeeeder to seed Database with players"""
    def __init__(self):
        pass

    def seed(self) -> None:
        """Seed method """

        db = TinyDB('db.json')
        players = db.table('players')

        players.insert({'id': 1, 'first_name': 'John', 'last_name': 'Die',
                        'elo_points': 1016, 'date_of_birth ': '12/12/1987',
                        'gender': 'm'})
        players.insert({'id': 2, 'first_name': 'Jane', 'last_name': 'Doll',
                        'elo_points': 894, 'date_of_birth ': '12/12/1987',
                        'gender': 'm'})
        players.insert({'id': 3, 'first_name': 'Jill', 'last_name': 'Sullivan',
                        'elo_points': 898, 'date_of_birth ': '12/12/1987',
                        'gender': 'm'})
        players.insert({'id': 4, 'first_name': 'William', 'last_name': 'Smith',
                        'elo_points': 996, 'date_of_birth ': '12/12/1987',
                        ' gender ': 'm'})
        players.insert({'id': 5, 'first_name': 'Cloé', 'last_name': 'Beaulieu',
                        'elo_points': 990, 'date_of_birth ': '12/12/1987',
                        ' gender ': 'f'})
        players.insert({'id': 6, 'first_name': 'Manon', 'last_name': 'Lavie',
                        'elo_points': 999, 'date_of_birth': '12/12/1987',
                        'gender ': 'f'})
        players.insert({'id': 7, 'first_name': 'Bobby', 'last_name': 'Larsson',
                        'elo_points': 1234, 'date_of_birth ': '12/12/1987',
                        'gender': 'm'})
        players.insert({'id': 8, 'first_name': 'Julie', 'last_name': 'Vini',
                        'elo_points': 1100, 'date_of_birth ': '12/12/1987',
                        'gender ': 'f'})

    def clear(self) -> None:
        """Method to reset players in db.json"""

        db = TinyDB('db.json')
        db.drop_table('players')
        