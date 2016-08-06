import os
import re

num = 76
endnum = 114
head = '0104-'
png = '.png'


for var in range(num,endnum+1) :
    beforefile = head + str(var) + png
    afterfile = head + str(var-1) + png

    os.rename(beforefile,afterfile)
