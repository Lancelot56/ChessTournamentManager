# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:34:08 2022

@author: m
"""


from operator import itemgetter
from tinydb import TinyDB


class ReportView:
    """All about reports : players/tournaments"""

    @staticmethod
    def report_players():
        """Display a list of all the players."""
        db = TinyDB('..db.json')
        players = db.table('players').all()
        players.sort(key=itemgetter("elo_points"))
        print(players)
        players_dict = []
        for player in players:
            players_dict.append(dict(player))
        print(players_dict)

        for player in players:
            print(
                    f"{player['last_name']} {player['first_name']} RANK: {player['rank']} "
                    f"TOTAL SCORE: {player['score']}"
                    )
    def report_tournaments(self):
        """Display a list of all the tournaments."""
        db = TinyDB('../db.json')
        tournaments = db.table('tournaments').all()

        for tournament in tournaments:

            print(
                    f"{tournament['name']} DATE : {tournament['date']} LOCATION : "
                    f"{tournament['location']} MODE : {tournament['mode']}"
                    )
