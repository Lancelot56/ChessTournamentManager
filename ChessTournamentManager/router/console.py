# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:04:56 2022

@author: m
"""
import sys
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from controllers.menucontroller import MenuController
from controllers.roundcontroller import RoundController
from db.seeders.databaseseeder import DatabaseSeeder

class Console:
    """ Console for routing requests to the right controller"""
    def __init__(self) -> None:
        pass

    @staticmethod
    def routing(menu_input:int):
        """ routinf requests of the menu to the right controller"""
        if menu_input == 1:
            player_id = int(input('Enter the id\'s player to see details : '))
            PlayerController.show(player_id)
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 2:
            tournament_id = int(input('Enter the id\'s tournament to see details : '))
            TournamentController.show(tournament_id)
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 3:
            PlayerController.add_player()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 4:
            print('update ranking')
            PlayerController.update_rank()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 5:
            TournamentController.add_tournament()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 6:
            RoundController.add_rounds()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 71:
            print('listing all players:sorted player list')
            PlayerController.index()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 72:
            TournamentController.index()
            input("Press Enter to continue...")
            Console.routing(MenuController().menu())

        if menu_input == 8:
            DatabaseSeeder().clear()
            # program that stops execution for option 6
            try:
                DatabaseSeeder().clear()
                sys.exit('Chess Tournaments Manager - End')
            except:
                print('Chess Tournaments Manager - End')
    