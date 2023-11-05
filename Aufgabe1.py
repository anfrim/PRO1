# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:20:35 2023

@author: anast
"""

def histogram_characters_ger(input_sentence):
    pairs_list = list()
    sent = input_sentence.lower()
    sent = sent.replace(" ", "")
    for char in sent:
        number = sent.count(char)
        pairs_list.append((char, number))
    
    dictionary = {}
    
    for key, val in pairs_list:
        dictionary.setdefault(key, val)
    
    print(dictionary)
        
histogram_characters_ger("Die Studierenden klönen")
        
        