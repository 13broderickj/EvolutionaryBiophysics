# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:44:00 2017

@author: jasebroderick
"""
import re
#FIND DNA PATTERNS THAT THE TWO CONSECUTIVES PATTERNS MATCH EACH OTHER
dnas=['aggagg','gattaggattaggatgat','agctgcagtaggttaggttagagaga','abcdefghijklmnop','aabcdef']
dnaAsNumber=[123456432341234,11,22222,334433,12345678,54321,654,34636,123123,1234512345]#I DON'T SMOKE CRACK MOTHERFUCKER I SELL IT 
lines = ['dogs','bood','fussss','darlussm','caaase','noathing','found','bud','bassbass']
for line in dnaAsNumber+dnas:
    line=str(line)
    searchObj = re.search( r'([A-Z0-9]{3,})\1', line, re.M|re.I)
    
    if searchObj:
       print "searchObj.group() : ", searchObj.group()
    else:
       print "Nothing found!!"
       
