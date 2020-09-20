
import os
from sys import argv, exit
from read_evac import *

print("================================")
print ("Length of input parameters:", len(argv))
print("================================")

if len(argv)==2:
    file1 = argv[1]
    if file1 == '-help':
        print ('Show help info in readme.txt!')
        exit(-1)
    elif file1:
        if os.path.exists(file1):
            print ('load .fds file and extract evac-related information', file1)
        else:
            print ("Input file %s does not exit!" %file1)
            exit(-1)

    CHID=readCHID(file1)
    print CHID
    readPRTfile(CHID+'_evac_0001.prt5')
    visualizeEvac(CHID+'_evac_0001.npz', file1)


if len(argv)==3:
    file1 = argv[1]
    flag = argv[2]
    if file1 == '-help':
        print ('Show help info in readme.txt!')
        exit(-1)
    elif file1:
        if os.path.exists(file1):
            print ('load .fds file and extract evac-related information', file1)
        else:
            print ("Input file %s does not exit!" %file1)
            exit(-1)
    
    CHID=readCHID(file1)
    print CHID
    if flag == '/readonly':
        readPRTfile(CHID+'_evac_0001.prt5')
    if flag == '/showonly':
        visualizeEvac(CHID+'_evac_0001.npz', file1)

if len(argv)>3:
    print("Too many input parameters!")
    exit(-1)

    
