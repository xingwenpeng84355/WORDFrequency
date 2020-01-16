#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:40:29 2020

@author: xingwenpeng
"""
import jieba
import pandas as pd
documents_path='/Users/xingwenpeng/Desktop/csvdata/docs.csv'

txt= open(documents_path, "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
wordFreq=[]
wordFreqN=[]
for i in range(3000):
    word, count = items[i]
    print("{0:<10}{1:<5}".format(word, count))
    wordFreq.append(word)
    wordFreqN.append(count)
df = pd.DataFrame(wordFreq, columns=['frequency'])
dh = pd.DataFrame(wordFreqN, columns=['frequency'])

excel_out_put_path="/Users/xingwenpeng/Desktop/csvdata/wordFrequency.xlsx"
df.to_excel(excel_out_put_path, index=False)
excel_out_put_path="/Users/xingwenpeng/Desktop/csvdata/wordFrequencyN.xlsx"
dh.to_excel(excel_out_put_path, index=False)


emotions_path='/Users/xingwenpeng/Desktop/csvdata/wordsinemotion.csv'
Etxt= open(emotions_path, "r", encoding="utf-8").read()
EtxtW = jieba.lcut(Etxt)
set_listone = set(EtxtW)
set_listtwo = set(wordFreq)
listone_listtwo = set_listone & set_listtwo

df = pd.DataFrame(listone_listtwo, columns=['same'])
excel_out_put_path="/Users/xingwenpeng/Desktop/listone_listtwo.xlsx"
     