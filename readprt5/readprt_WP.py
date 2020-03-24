# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 10:00:58 2014

@author: 
"""

import numpy as np
import sys
import os
import struct

infile = open("test.prt5","rb")
outfile = open("output2.txt", "w")

#filedata = infile.read()
#filesize = infile.tell()
#filedata2 = bytearray(filedata)
#print filedata
#print >> outfile, filedata


#Read fortran record, return payload as bytestring
def readFRec(infile,fmt):
    len1   = infile.read(4)
    if not len1:
        return None
    len1   = struct.unpack('@I', len1)[0]

    if len1==0:
        len2=infile.read(4)
        return None
    num    = int(len1/struct.calcsize(fmt))
    fmt2   = str(num)+fmt
    if num>1:
        result = struct.unpack(fmt2,infile.read(len1))
    else:
        result = struct.unpack(fmt2,infile.read(len1))[0]
    len2   = struct.unpack('@I', infile.read(4))[0]
    if fmt == 's':
        result=result[0].rstrip()
    return result

#Assumes single precision
def readPRTfile(fname,max_time=np.Inf):
    fin = open(fname,'rb')
    one_integer=readFRec(fin,'I')  #! Integer 1 to check Endian-ness
    version=readFRec(fin,'I')       # FDS version number
    n_part=readFRec(fin,'I')        # Number of PARTicle classes
    q_labels = []
    q_units  = []
    for npc in range(0,n_part):
        n_quant,zero_int=readFRec(fin,'I')  # EVAC_N_QUANTITIES, ZERO_INTEGER
        for nq in range(0,n_quant):
            smv_label=readFRec(fin,'s')
            units    =readFRec(fin,'s')
            q_units.append(units)  
            q_labels.append(smv_label)
    Q=[]
    T  = []
    diam =[]
    while True:

        Time  = readFRec(fin,'f')  # Time index
        if Time == None or Time>max_time:
            break
        nplim = readFRec(fin,'I')  # Number of particles in the PART class
        if nplim>0:
            xyz  = np.array(readFRec(fin,'f'))
            tag  = np.array(readFRec(fin,'I'))
            q    = np.array(readFRec(fin,'f'))
            print >> outfile, "xyz:", xyz, "\n" 
            print >> outfile, "tag:", tag, "\n"
            #print >> outfile, "g", q, "\n"
            #xyz.shape = (3,nplim)
            #q.shape   = (n_quant,nplim)
            # process timestep data
            T.append(Time)
            Q.append(q)
        else:
            tmp = fin.read(24)
    fin.close()
    return (np.array(T),np.hstack(Q),q_labels,q_units)



if __name__ == "__main__":
    if len(sys.argv)<2:
        sys.exit("Give .prt5 file as argument")
    T,Q,labels,units =  readPRTfile(sys.argv[1])
    print(labels,units)
    print(len(T),Q.shape)       
