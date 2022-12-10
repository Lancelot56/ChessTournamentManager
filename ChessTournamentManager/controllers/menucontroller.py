# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:56:58 2022

@author: m
"""

from views.menuview import MenuView


class MenuController:
    """Menu Controller """
    def __init__(self):
        pass

    def menu(self):
        """Manage menu input"""
        MenuView().show_menu()
        return int(input())
