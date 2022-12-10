# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:30:49 2022

@author: m
"""

from db.seeders.playerseeder import PlayerSeeder
from db.seeders.tournamentseeder import TournamentSeeder


class DatabaseSeeder:
    """ Database class."""

    def __init__(self):
        """database constructor."""

    def seed(self):
        """ Subclasses Playerseeder and Tournament seeder."""
        PlayerSeeder().seed()
        TournamentSeeder().seed()

    def clear(self):
        """ For clearing seeders."""
        PlayerSeeder().clear()
        TournamentSeeder().clear()
