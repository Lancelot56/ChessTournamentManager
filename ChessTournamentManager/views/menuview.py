# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:05:42 2022

@author: m
"""



class MenuView:
    """ Main Menu """
    def __init__(self):
        pass

    @staticmethod
    def show_menu():
        """ Display Menu """
        print('\n-- Welcome to Chess Tournaments Manager\n')
        print('\n1. Searching a player by ID')
        print('\n2. Searching a tournament by ID')
        print('\n3. Adding a player')
        print('\n4. Update Elo ranking')
        print('\n5. Adding a tournament')
        print('\n6. Completing results of an existing tournament ')
        print('\n7. Reports  ')
        print('\n    71: Players list')
        print('    72: Tournaments list')
        print('\n8. Exit program')
        print('\n Your choice (1-8) ? :')
