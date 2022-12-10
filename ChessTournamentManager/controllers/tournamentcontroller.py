# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:59:04 2022

@author: m
"""
from tinydb import TinyDB
from models.tournamentmodel import TournamentModel
from views.tournamentview import TournamentView


class TournamentController:
    """All about Tournaments : find/show/create"""

    def __init__(self):
        """Consructor"""

    @staticmethod
    def index() -> None:
        """index"""
        tournaments=TournamentModel.get_tournaments()
        TournamentView().list_tournaments(tournaments)

    @staticmethod
    def show(idt:int) -> None:
        """show"""
        tournament =  TournamentModel.get_tournament_by_id(idt)
        TournamentView().show_tournament(tournament)

    @staticmethod
    def add_tournament():
        """ add a tournament"""
        db = TinyDB('db.json')
        tournaments = db.table('tournaments')

        last_id = tournaments.all()[-1]["id"]
        idt = last_id + 1

        name = input("Please enter tournament's name : ")
        location = input("Please enter tournament's location ? :")
        description = input("Please enter tournament's description : ")
        time_control = int(input("Time control in sec ? :"))
        nb_rounds = int(input("How many Rounds ? :"))
        record = ({'id':idt, 'name': name,'location': location, 'description': description,
                 'time control': time_control,'nb_rounds': nb_rounds,'rounds':[1,2,3,4]})
        tournaments.insert(record)

        print('tournament saved ')

        input("Press Enter to continue...")
