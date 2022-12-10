# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:33:07 2022

@author: m
"""

from tinydb import TinyDB


class TournamentSeeder:
    """Class TournamentSeeder to seed Database with tournaments"""

    def __init__(self):
        """Constructeur"""
        pass

    def seed(self) -> None:
        """Seed method"""
        db = TinyDB('db.json')
        tournaments = db.table('tournaments')
        tournaments.insert({
            'id': 1,
            'name': 'Blitz Chess Arena',
            'description': 'Come n\' prove them wrong about your chess skills!',
            'location': 'Online',
            'time_control': 360,
            'players': [
                {
                    'id': 1,
                    'firstname': 'John',
                    'lastname': 'Doe',
                    'elo_points': 1080
                },
                {
                    'id': 1,
                    'firstname': 'Jane',
                    'lastname': 'Doe',
                    'elo_points': 1014
                }
            ],
            'rounds': [
                {
                    'winner': {
                        'id': 2,
                        'firstname': 'John',
                        'lastname': 'Doe',
                        'elo_points': 1080
                    },
                    'looser': {
                        'id': 2,
                        'firstname': 'Jane',
                        'lastname': 'Doe',
                        'elo_points': 1014
                    }
                }
            ]
        })
        tournaments.insert({
            'id': 2,
            'name': 'Bullet from Paris',
            'description': 'World Championship',
            'location': 'Paris',
            'time_control': 560,
            'players': [
                {
                    'id': 1,
                    'firstname': 'John',
                    'lastname': 'Doe',
                    'elo_points': 1080
                },
                {
                    'id': 2,
                    'firstname': 'Jane',
                    'lastname': 'Doe',
                    'elo_points': 1014
                }
            ],
            'rounds': [
                {
                    'winner': {
                        'id': 1,
                        'firstname': 'John',
                        'lastname': 'Doe',
                        'elo_points': 1080
                    },
                    'looser': {
                        'id': 2,
                        'firstname': 'Jane',
                        'lastname': 'Doe',
                        'elo_points': 1014
                    }
                }
            ]
        })
        tournaments.insert({
            'id': 3,
            'name': 'Fast from Boston',
            'description': 'US Championship',
            'location': 'Boston',
            'time_control': 160,
            'players': [
                {
                    'id': 4,
                    'firstname': 'Gerard',
                    'lastname': 'Delobel',
                    'elo_points': 1080
                },
                {
                    'id': 2,
                    'firstname': 'Jane',
                    'lastname': 'Doe',
                    'elo_points': 1014
                }
            ],
            'rounds': [
                {
                    'winner': {
                        'id': 4,
                        'firstname': 'Gérard',
                        'lastname': 'Delobel',
                        'elo_points': 1080
                    },
                    'looser': {
                        'id': 2,
                        'firstname': 'Jane',
                        'lastname': 'Doe',
                        'elo_points': 1014
                    }
                }
            ]
        })

    def clear(self) -> None:
        """Method to reset tournaments in db.json"""
        db = TinyDB('db.json')
        db.drop_table('tournaments')
