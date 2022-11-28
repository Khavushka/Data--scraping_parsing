# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:24:44 2022

@author: khavu
"""

import text

txt = text.get_dictionary('players-parsing-to_csv.py')

season = []

def get_dictionary(url):
    for i in range(1,51):
        filename = "data/season-" +str(i)+".csv"
        c_dict = text.get_dictionary(filename)
        season.append(c_dict)