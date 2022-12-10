# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:07:08 2022

@author: m
"""

from tinydb.table import Document

class TournamentView:
    """ Display informations about tournaments """

    def __init__(self):
        pass


    def show_tournament(self,tournament:Document) ->None:
        """ Tournament by id """
        print('\n')
        print(f"Id: : { tournament['id'] }")
        print(f"Name : {tournament['name']}")
        print(f"location: {tournament['location']}")
        print(f"Description: {tournament['description']}")
        print(f"Time Control : {tournament['time_control']}")
        print(f"Opponents : {tournament['players']}")
        print('\n\n')

    def list_tournaments(self, tournaments):
        """list of tournaments """
        for tournament in tournaments:
            print(f"ID : { tournament['id'] }")
            print(f"Name : { tournament['name'] }")
            print(f"Location : {tournament['location'] }")
            print(f"Description : { tournament['description'] }")
            