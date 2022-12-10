# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:55:56 2022
"""

# import datetime
# from models.playermodel import PlayerModel
# from models.roundmodel import RoundModel
from operator import itemgetter
from tinydb import TinyDB



class RoundController:
    """Round controller"""

    def __init__(self):
        """Constructor"""


    @staticmethod
    def add_rounds():
        """
        Swiss Method

        First Round : The players are ranked by best ranking.
        index = number of matchs by round = 4
        The matchs are :
            player[0] vs players[4]
            player[1] vs players[5]
            player[2] vs players[6]
            player[3] vs players[7]

        """
        db = TinyDB('db.json')
        players = db.table('players').all()
        # print(players)
        players.sort(key=itemgetter("elo_points"))

        print('\nPlayers of the Tournament : \n')
        print('\nS1 Group :\n')
        for index in range(4):
            print(players[index])
        print('\nS2 Group :\n')
        for index in range(4, 8):
            print(players[index])
        print('\nRound 1 : matches / players : \n')

        round_1 = []  # Round 1 list of match

        for index in range(4):
            match = (
                (
                    players[index]['last_name'],
                    players[index]['elo_points'],
                ),
                (
                    players[index + 4]['last_name'],
                    players[index + 4]['elo_points'],
                ),
            )
            round_1.append(match)

        player1 = players[0]
        player2 = players[1]
        player3 = players[2]
        player4 = players[3]
        player5 = players[4]
        player6 = players[5]
        player7 = players[6]
        player8 = players[7]

        print('match1 :', player1['first_name']+' '+player1['last_name'],
              'vs', player5['first_name']+' '+player5['last_name'],
              '\nmatch2 :', player2['first_name']+' '+player2['last_name'],
              ' vs ', player6['first_name']+' '+player6['last_name'],
              '\nmatch3 :', player3['first_name']+' '+player3['last_name'],
              ' vs ', player7['first_name']+' '+player7['last_name'],
              '\nmatch4 :', player4['first_name']+' '+player4['last_name'],
              ' vs ', player8['first_name']+' '+player8['last_name'])

        # score premier round

        print('\nRound 1 results : \n')
        print('match1 :', player1['first_name']+' '+player1['last_name'],
              ' vs ', player5['first_name']+' '+player5['last_name'])
        player1_score1 = int(input('Enter score player 1 ? :'))
        player5_score2 = int(input('Enter score player 2 ? :'))
        match1 = [player1, player5, player1_score1, player5_score2]

        print('match2 :', player2['first_name']+' '+player2['last_name'],
              ' vs ', player6['first_name']+' '+player6['last_name'])
        player2_score1 = int(input('Enter score player 1 ? :'))
        player6_score2 = int(input('Enter score player 2 ? :'))
        match2 = [player2, player6, player2_score1, player6_score2]

        print('\nmatch3 :', player3['first_name']+' '+player3['last_name'],
              ' vs ', player7['first_name']+' '+player7['last_name'])
        player3_score1 = int(input('Enter score player 1 ? :'))
        player7_score2 = int(input('Enter score player 2 ? :'))
        match3 = [player3, player7, player3_score1, player7_score2]

        print('\nmatch4 :', player4['first_name']+' '+player4['last_name'],
              ' vs ', player8['first_name']+' '+player8['last_name'])
        player4_score1 = int(input('Enter score player 1 ? :'))
        player8_score2 = int(input('Enter score player 2 ? :'))
        match4 = [player4, player8, player4_score1, player8_score2]

        winners1 = []  # winners 1st round

        print('\n Round 2 qualified players :\n')

        if match1[2] > match1[3]:
            print(match1[0], ' qualified ! ')
            winners1.append(match1[0])
        else:
            print(match1[1], ' qualified ')
            winners1.append(match1[1])
        if match2[2] > match2[3]:
            print(match2[0], ' qualified ! ')
            winners1.append(match2[0])
        else:
            print(match2[1], ' qualified ')
            winners1.append(match2[1])
        if match3[2] > match3[3]:
            print(match3[0], ' qualified ! ')
            winners1.append(match3[0])
        else:
            print(match3[1], ' qualified ')
            winners1.append(match3[1])

        if match4[2] > match4[3]:
            print(match4[0], ' qualified ! ')
            winners1.append(match4[0])
        else:
            print(match4[1], ' qualified ')
            winners1.append(match4[1])

        # 2nd Round : matches

        print('\nRound 2 : matches / players : \n')

        # winners 1st round ranked by elo
        winners1.sort(key=itemgetter("elo_points"))

        print(winners1)

        print('\nRound 2 matches : \n')

        player1 = winners1[0]
        player2 = winners1[1]
        player3 = winners1[2]
        player4 = winners1[3]

        print('match1 :', player1['first_name']+' '+player1['last_name'],
              ' vs', player3['first_name']+' '+player3['last_name'],
              '\nmatch2 :', player2['first_name']+' '+player2['last_name'],
              ' vs ', player4['first_name']+' '+player4['last_name'])

        # winners of second round

        print('\nRound 2 results : \n')

        print('\nmatch1 :', player1['first_name']+' '+player1['last_name'],
              ' vs ', player3['first_name']+' '+player3['last_name'])

        player1_score1 = int(input('Enter score player 1 ? :'))
        player3_score2 = int(input('Enter score player 2 ? :'))
        match1 = [player1, player3, player1_score1, player3_score2]

        print('match2 :', player2['first_name']+' '+player2['last_name'],
              ' vs ', player4['first_name']+' '+player4['last_name'])
        player2_score1 = int(input('Enter score player 1 ? :'))
        player4_score2 = int(input('Enter score player 2 ? :'))
        match2 = [player2, player4, player2_score1, player4_score2]

        print('\nRound 3 qualified players : \n')

        # winners of second round

        winners2 = []  # winners 2nd round

        print('\n Round 2 qualified players :\n')

        if match2[2] > match2[3]:
            print(match1[0], ' qualified ! ')
            winners2.append(match1[0])
        else:
            print(match1[1], ' qualified ')
            winners2.append(match1[1])
        if match2[2] > match2[3]:
            print(match2[0], ' qualified ! ')
            winners2.append(match2[0])
        else:
            print(match2[1], ' qualified ')
            winners2.append(match2[1])

        # 3rd Round : matches

        print('\nRound 3 : matches / players : \n')

        # winners3 = []

        winners2.sort(key=itemgetter("elo_points"))

        player1 = winners2[0]
        player2 = winners2[1]

        print('match1 :', player1['first_name'] + ' ' + player1['last_name'],
              ' vs ' + player2['first_name']+' '+player2['last_name'])

        player1_score1 = int(input('Enter score player 1 ? :'))
        player2_score2 = int(input('Enter score player 2 ? :'))

        match3 = [player1, player2, player1_score1, player2_score2]

        print('\nRound 3 results : \n')

        if match3[2] > match2[3]:
            print(match3[0], ' is the winner !  ')
        else:
            print(match3[1], ' is the winner !')
