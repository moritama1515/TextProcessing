#!/usr/bin/env python
#coding:utf-8
import sys
import re
import string

#コマンドラインくら引数を受け取りファイルを開く
argvs = sys.argv
fr = open(argvs[1],'r')
Allfr = fr.read()

#19路盤の座標(a-s)の検索文字列を作成
char_list = [chr(k) for k in range(97,97+19)]
search_list = ''.join(char_list)

text = Allfr.replace('\n','')
text = text.replace('\r','')
text_list = text.split(";")

#座標関連データ部分を取り出す
play = text_list[2:]

#座標関連データをlistからstrに変換
str_play = "\n".join(play)

#座標関連データの座標部分のみを取り出す
maps = str_play.replace("Black",'')
maps = maps.replace("White",'')
maps = maps.replace("[",'')
maps = maps.replace("]",'')
maps = maps.replace(")",'')

#listに格納
value =  maps.split("\n")

#書き込み用ファイルを開く
wfile = argvs[1].split(".")
fw = open(wfile[0]+".csv",'w') 

#csv形式に変換(手数,x座標,y座標)
for i,v in enumerate(value):
	map_list = list(v)
	map_list[0] = str(search_list.find(map_list[0])+1)
	map_list[1] = str(search_list.find(map_list[1])+1)
	map_list = ','.join(map_list)
	fw.write(str((i+1)) + "," + map_list +"\n")
	
fw.close()
fr.close()
