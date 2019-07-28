# -*- coding: utf-8 -*-
# Use Class with tinker
# Charalambos Themistocleous
# Normalization Function
# 2016

#the a string with the text and then using the replace
#adds space between the before and after a symbol as:

def normalize(myString):
       aString = myString
       #aString = aString.replace("\n", " ")
       aString = aString.replace("\r", " ")
       aString = aString.replace("\t", " ")
       aString = aString.replace("\\", "")
       aString = aString.replace("\"", " || ")
       aString = aString.replace("/", "")
       aString = aString.replace("(", " || ")
       aString = aString.replace(")", " || ")
       aString = aString.replace("{", " || ")
       aString = aString.replace("}", " || ")
       aString = aString.replace("[", " || ")
       aString = aString.replace("]", " || ")
       aString = aString.replace("*", "")
       aString = aString.replace("#", "")
       aString = aString.replace("&", "")
       aString = aString.replace("-", "")
       aString = aString.replace("_", "")
       aString = aString.replace("«", " || ")
       aString = aString.replace("»", " || ")
       aString = aString.replace(",", " | ")
       aString = aString.replace(":", " || ")
       aString = aString.replace("...", " || ")
       return aString
