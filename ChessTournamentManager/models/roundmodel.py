# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:53:47 2022

@author: m
"""

import datetime


class RoundModel:
    """
    Define a round
    Attrs :
        Name (str)
        Start date and time (int):  AUTOMATIC
        End date and time (int) : AUTOMATIC
        list of matchs (list) : 4 by round.
    """

    def __init__(self, idr, matchs, name="round 1",  end=0):
        """Init."""
        self.idr = idr
        self.name = name
        self.start = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.matchs = matchs
        self.end = end

    def __repr__(self):
        """Display : ROUND[], START : [date/time] END : [date/time]."""
        return (
            f"{self.name} START : {self.start} END : {self.end} \n "
            f"MATCHS : {self.matchs} "
        )
