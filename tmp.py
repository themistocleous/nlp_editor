# Charalambos Themistocleous
# Part 1
# Automatic pos from lexicon

import nltk as nltk
import pandas as pd
from normalize import normalize
text1 = "η δύναμη μιλώ τηλέφωνο"
text1 = nltk.word_tokenize ( text1 )
df = pd.read_csv('dictionary.csv',sep=";",encoding="utf8" )
mstr = ""
for n in range(len(text1)):
    for l in df.index:
        if text1[n] == df.ix[ l,"lemma" ]:
            pos = ''.join ( [ str(text1[n])," [",str(df.ix[ l,"pos" ]),"]" ])
            mstr = ''.join ( [ mstr,pos ] )
print(mstr)


