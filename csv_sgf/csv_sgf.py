#!/usr/bin/env python
#coding:utf-8
import sys
import re
import string

f = open('001.txt','r')
Allf = f.read()

#a-zのリストを作成
charList = [chr(k) for k in range(97,97+26)]

text = Allf.replace('\n','')
text = text.replace('\r','')

textList = text.split(";")
#座標関連データ部分を取り出す
play = textList[2:-2]
#座標関連データをlistからstrに変換
jw = "\n".join(play)

#座標関連データの座標部分のみを取り出す
maps = jw.replace("Black",'')
maps = maps.replace("White",'')
maps = maps.replace("[",'')
maps = maps.replace("]",'')

#listに格納
value =  maps.split("\n")

#csv形式に変換(手数,x座標,y座標)
for i,v in enumerate(value):
	map_list = list(v)
	map_list = ','.join(map_list)
	print str((i+1)) + "," + map_list

f.close()
