# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:01:19 2023

@author: anast
"""
import string

def histogramm(input_sentence, spaces = True, special_characters=False, count_all=True):
    pairs_list = list()
    sent = input_sentence.lower()
    char_to_replace = ["ö", "ü", "ä", "ß"]
    replacement = ["oe", "ue", "ae", "ss"]
    lowercase_alphabet = string.ascii_lowercase
    letters = []
    if spaces == False:
        sent = sent.replace(" ", "")
    else:
        lowercase_alphabet = lowercase_alphabet + " "
    if special_characters == True:
        for item in char_to_replace:
            i = char_to_replace.index(item)
            new_item = replacement[i]
            sent = sent.replace(item, new_item)
    else:
        lowercase_alphabet = lowercase_alphabet + "äöüß"
    if count_all == True:
        for letter in lowercase_alphabet:
            letters.append(letter)
    else:
        for letter in sent:
            letters.append(letter)
        
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
    
histogramm("Die Studierenden klönen", spaces = True, special_characters=True, count_all=False)