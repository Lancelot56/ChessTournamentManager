# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:34:38 2022

@author: m
"""

from tinydb import TinyDB
from tinydb.table import Document


class MatchModel:
    """MatchModel class"""

    def __init__(self, idm, player_1, player_2, score_1, score_2):
        """Match Constructor"""
        self.match = []
        self.idm = idm
        self.player_1 = player_1
        self.player_2 = player_2
        self.score1 = score_1
        self.score2 = score_2

    @staticmethod
    def get_matchs():
        """Function get a match in detail"""
        db = TinyDB('../db.json')
        return db.table('matchs').all()

    @staticmethod
    def get_match_by_idm(idm: int) -> Document:
        """Function listing match in detail"""
        db = TinyDB('../db.json')
        return db.table('matchs').get(doc_id=idm)
