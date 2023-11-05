# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:43:11 2023

@author: anast
"""

def histogram_characters_en(input_sentence):
    char_to_replace = ["ö", "ü", "ä", "ß"]
    replacement = ["oe", "ue", "ae", "ss"]
    pairs_list = list()
    sent = input_sentence.lower()
    for item in char_to_replace:
        i = char_to_replace.index(item)
        new_item = replacement[i]
        sent = sent.replace(item, new_item)
    for char in sent:
        number = sent.count(char)
        pairs_list.append((char, number))
    
    dictionary = {}
    
    for key, val in pairs_list:
        dictionary.setdefault(key, val)
    
    print(dictionary)
        
histogram_characters_en("Die Studierenden klönen")