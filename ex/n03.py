#---------------------------------
# n03.py: drawing a small graph
import os
import math
fs = open('a.txt','w')
tstop = 200
for t in range(tstop):
    s = str(t) + ' ' + str(math.sin(0.1*t)) + '\n'
    fs.write(s)
fs.close()
os.system('gc a.txt') # cmd 'gc' is not applicable to linux system. See www.nips.ac.jp/huinfo/documents/index.htm for detailed information. 
#---------------------------------

