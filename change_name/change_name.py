import os
import re

num = 76
endnum = 114
head = '0104-'
ext = '.png'


for var in range(num,endnum+1) :
    beforefile = head + str(var) + ext
    afterfile = head + str(var-1) + ext

    os.rename(beforefile,afterfile)
