
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:05:24 2019

@author: Maxga
"""

import pythainlp 
import pythainlp.corpus 

with open("food.txt","r",encoding="utf-8-sig") as f:
    data1=f.read() 
#print(data1)
with open("sco.txt","r",encoding="utf-8-sig") as f:
    data2=f.read() 
#print(data2)
with open("spt.txt","r",encoding="utf-8-sig") as f:
    data3=f.read() 
#print(data3)
with open("game.txt","r",encoding="utf-8-sig") as f:
    data4=f.read() 
#print(data4)
with open("cuse.txt","r",encoding="utf-8-sig") as f:
    data5=f.read()
#print(data5)

from collections import Counter
list_word1=pythainlp.word_tokenize(data1)
list_word2=pythainlp.word_tokenize(data2)
list_word3=pythainlp.word_tokenize(data3)
list_word4=pythainlp.word_tokenize(data4)
list_word5=pythainlp.word_tokenize(data5)

stop = set(pythainlp.corpus.stopwords.words('thai')) 
etcstop = [' ','\r\n','\n','1','2','3','4','5','6','7','8','9','0',':','!',
           '@','#','$','%','^','&','*','&','(',')','_','+',',','\t']
list_word1=[i for i in pythainlp.word_tokenize(data1) if i not in stop and i not in etcstop]
list_word2=[i for i in pythainlp.word_tokenize(data2) if i not in stop and i not in etcstop]
list_word3=[i for i in pythainlp.word_tokenize(data3) if i not in stop and i not in etcstop]
list_word4=[i for i in pythainlp.word_tokenize(data4) if i not in stop and i not in etcstop]
list_word5=[i for i in pythainlp.word_tokenize(data5) if i not in stop and i not in etcstop]

wordcont1=Counter(list_word1)
wordcont2=Counter(list_word2)
wordcont3=Counter(list_word3)
wordcont4=Counter(list_word4)
wordcont5=Counter(list_word5)

with open("wordfood.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(wordcont1)))
    
with open("wordsco.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(wordcont2)))
    
with open("wordspt.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(wordcont3)))
    
with open("wordgame.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(wordcont4)))
            
with open("wordcuse.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(wordcont5)))

allwordcont=Counter(list_word1+list_word2+list_word3+list_word4+list_word5)
with open("wordall.txt","w+",encoding="utf-8") as f:
    f.write(str(dict(allwordcont)))

word1list=list(dict(wordcont1))
word2list=list(dict(wordcont2))
word3list=list(dict(wordcont3))
word4list=list(dict(wordcont4))
word5list=list(dict(wordcont5))
allwordlist=list(dict(allwordcont))

inverted_list={}

for i in allwordlist:
    inverted_list[i]=[]
    if i in word1list:
        inverted_list[i].append(str("อาหาร"))
    if i in word2list:
        inverted_list[i].append(str("การเมือง"))
    if i in word3list:
        inverted_list[i].append(str("การออกกำลังกาย"))
    if i in word4list:
        inverted_list[i].append(str("เกมส์"))
    if i in word5list:
        inverted_list[i].append(str("มลพิษ"))    

file = ""
for d,index in inverted_list.items():
      file+=d+" : " +str(",".join(index))+"\r\n"

with open("index.txt","w",encoding="utf-8") as f:
     f.write(file)        
#print(allwordlist)
"""
data1 = [] 

for i in allwordlist:
    data1[i]=allwordlist[i]
    
    if i in word1list :
        data1[i] = data1[i]+"1"
    if i not in word1list :
        data1[i] = data1[i]+"0"    
    if i in word2list :
         data1[i] = data1[i]+"1"
    if i not in word2list :
        data1[i] = data1[i]+"0"      
    if i in word3list :
         data1[i] = data1[i]+"1"
    if i not in word3list :
        data1[i] = data1[i]+"0" 
    if i in word4list :
         data1[i] = data1[i]+"1"
    if i not in word4list :
        data1[i] = data1[i]+"0"        
    if i in word5list :
         data1[i] = data1[i]+"1"  
    if i not in word5list :
        data1[i] = data1[i]+"0"      
   """








