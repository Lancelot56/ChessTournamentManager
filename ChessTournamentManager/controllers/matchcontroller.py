# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:36:00 2022

@author: m
"""
from tinydb import TinyDB
from models.matchmodel import MatchModel
from views.matchview import MatchView




class MatchController:
    """ Matchcontroller to run all about matchs"""

    def __init__(self):
        pass

    @staticmethod
    def index() -> None:
        """index method to research a match by id """
        matchs =  MatchModel.get_matchs()
        MatchView().list_matchs(matchs)

    @staticmethod
    def show(idm:int) -> None:
        """show method to display a matchs list """
        match =  MatchModel.get_matchs_by_id(idm)
        MatchView().show_match(match)

    @staticmethod
    def add_match():
        """create a match """

        db = TinyDB('../db.json')
        matchs= db.table('matchs')

        print('Matchs input')


        idt=int(input('Tournament id ? :'))
        idr=int(input('Round id ? :'))
        idm=int(input('Match id ? :'))

        player_1=input('Player 1 id ?')
        player_2=input('Player 2 id ?')
        score_1=int(input(' Player 1 score ? :'))
        score_2=int(input(' Player 2 score ? :'))
        record=({'tournament_id':idt,'round_id':idr,'match_id':idm,
                 'player_1 id':player_1,'player_2 id':player_2,'score_1':score_1,'score_2':score_2})
        matchs.insert(record)
        print('\n match saved\n')
