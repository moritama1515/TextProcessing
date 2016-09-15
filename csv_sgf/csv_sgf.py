#!/usr/bin/env python
#coding:utf-8
import sys
import re
import string

f = open('001.txt','r')
Allf = f.read()

text = Allf.replace('\n','')
text = text.replace('\r','')

list = text.split(";")
play = list[2:-2]
count = 0
count += len(play)
jw = "\n".join(play)

maps = jw.replace("Black",'')
maps = maps.replace("White",'')
maps = maps.replace("[",'')
maps = maps.replace("]",'')

value =  maps.split("\n")
for i,v in enumerate(value):
	print str((i+1)) + "," + str(v)

#print count	
#print maps


f.close()
