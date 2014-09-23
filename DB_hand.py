#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import re


class DATA_BASE(object):

    def __init__(self):   
        self.db = sqlite3.connect('profile.db')


    def create_TBL(self):
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE if not exists profiles (id INTEGER PRIMARY KEY, 
                                       name TEXT UNIQUE,
                                       phone TEXT UNIQUE,
                                       cv TEXT,
                                       date DATETIME)''')
        self.db.commit()


    def update_DB(self, name, phone, cv):
        self.name, self.phone, self.cv = name, phone, cv 

        self.cursor.execute("INSERT INTO profiles VALUES (NULL, ?, ?, ?, datetime(CURRENT_TIMESTAMP, 'localtime'))", (self.name, self.phone, self.cv))
        self.db.commit()


    def print_out(self):
        for row in self.cursor.execute('SELECT cv FROM profiles ORDER BY id'):
            print row
           







if __name__ == "__main__":

    name = "Taras Dmytrus Andriyovych"
    phone = "+080638079433"
    cv = '''Django, pythondeveloper\
            was working for a three years at ERICPOL '''

    DB =  DATA_BASE()

    # create a table if not exists
    DB.create_TBL()
    # update row
    DB.update_DB(name, phone, cv)
    DB.print_out()