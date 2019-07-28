# -*- coding: utf-8 -*-
# Charalambos Themistocleous
# Measuring Characters
# 2017
def character_freq(string):
    frequencies = {}
    for i in string:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies
