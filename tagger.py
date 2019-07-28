# -*- coding: utf-8 -*-
# Charalambos Themistocleous
# Convertions Standard Modern Greek
# 2017
import pandas as pd
import nltk as nltk
from normalize import normalize


def tagger(text1):
    text1 = nltk.word_tokenize ( text1 )
    df = pd.read_csv ('dictionary.csv',sep=";",encoding="utf8")
    mstr = ""
    for n in range ( len ( text1 ) ):
        for l in df.index:
            if text1[ n ] == df.ix[ l,"lemma" ]:
                pos = ''.join ( [ str ( text1[ n ] )," [",str ( df.ix[ l,"pos" ] ),"]" ] )
                mstr = ''.join ( [ mstr,pos ] )
    return mstr
