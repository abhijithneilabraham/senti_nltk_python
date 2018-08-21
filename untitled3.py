#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 01:17:35 2018

@author: abhijith
"""
from nltk.stem import WordNetLemmatizer
import nltk
from nltk import tokenize
import numpy as np
from textblob import TextBlob

file=open("nn.txt","r")
read_file=file.read()
print('total sentences    ', read_file.count('.'))
number_of_sentences=read_file.count('.')
sentences=tokenize.sent_tokenize(read_file)
total=0
for p in sentences:
    q=TextBlob(p)
    senti=q.sentiment
    total=total+senti.polarity
    

average=total/number_of_sentences
if average>0:
    print("positive")
else:
    print("negative")    



        
