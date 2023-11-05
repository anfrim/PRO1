# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:57:28 2023

@author: anast
"""

import string

def histogramm_all_en(input_sentence):
    lowercase_alphabet = string.ascii_lowercase
    letters = []
    char_to_replace = ["ö", "ü", "ä", "ß"]
    replacement = ["oe", "ue", "ae", "ss"]
    pairs_list = list()
    sent = input_sentence.lower()
    for letter in lowercase_alphabet:
        letters.append(letter)
    for item in char_to_replace:
        i = char_to_replace.index(item)
        new_item = replacement[i]
        sent = sent.replace(item, new_item)
    for letter in letters:
        if letter in sent:
            number = sent.count(letter)
            pairs_list.append((letter, number))
        else:
            number = 0
            pairs_list.append((letter, number))
    
    dictionary = {}
    
    for key, val in pairs_list:
        dictionary.setdefault(key, val)
    
    print(dictionary)
        
histogramm_all_en("Die Studierenden klönen")
