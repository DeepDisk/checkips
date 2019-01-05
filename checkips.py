#!/usr/bin/python

#####[A]#####[M]#####[D]###
#                         # 
#-Coded By Mo7ammed 7amad-#
#-Date : 5th Jan 2019     #
#      [DeepDisk]         # 
#####[I]#####[L]#####[L]###

import os
import sys

if len(sys.argv)<=1:
    print('[+]checkips.py fileIpname.txt')
    exit(1)
elif 1 < len(sys.argv) <=2:
    filetext = sys.argv[1]
path = os.getcwd()+'\\'+filetext
ipsU=[]
if os.path.isfile(path):
    file = open(path,'r')
    try :
        line = file.readline()
        r=0
        while line!='':
            line = line.strip()
            lines = line.split('.')
            if len(lines)==4:
                if len(lines[0]) <=3 and len(lines[1]) <=3 and len(lines[2]) <=3 and len(lines[3]) <=3:
                    if lines[0].isdigit() and lines[1].isdigit() and lines[2].isdigit() and lines[3].isdigit():      
                        n1,n2,n3,n4=int(lines[0]),int(lines[1]),int(lines[2]),int(lines[3])
                        if n1!=0 and n1 !=127 and n1!=10 and n1!=169 and n1!=192 and n1<223 and n2 <= 255  and n3 <= 255 and n4 <= 255:
                            line = '.'.join(lines)
                            ipsU.append(line)                                        
            line = file.readline() 
            r+=1 
    except Exception as e:
        print(e)
    file.close()
    file = open(path,mode='w')
    n=0
    for i in set(ipsU):
        file.write(i+'\n')
        n+=1
    print('Befor examining Your ips the count lines were [',r,'] and the new count of lines is [',n,']')
    file.close()
else:
    print('There is an error in your setup ')
    exit(1)


