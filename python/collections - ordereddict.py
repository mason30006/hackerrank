# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 18:59:32 2017

@author: Mason
"""

from sys import stdin
from collections import OrderedDict

ordered_dictionary = OrderedDict()
n = stdin.readline()

for i in range(int(n)):
    string = stdin.readline()
    string_parts = string.split(' ')
    price = int(string_parts[-1])
    item_name = ' '.join(string_parts[0:-1])
    if item_name in ordered_dictionary.keys():
        ordered_dictionary[item_name] = price + ordered_dictionary[item_name]
    else:
        ordered_dictionary[item_name] = price
        
for key in ordered_dictionary.keys():
    print key + ' ' + str(ordered_dictionary[key])
        
        