


#-*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:16:24 2022

"""


from router.console import Console
from controllers.menucontroller import MenuController
from db.seeders.databaseseeder import DatabaseSeeder

def main():
    """Program Entry"""
    DatabaseSeeder().seed()
    Console.routing(MenuController().menu())
    DatabaseSeeder().clear()

main()

