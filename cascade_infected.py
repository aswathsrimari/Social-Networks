# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 03:40:06 2019

@author: user
"""
#independent cascade model

import networkx as nx
import matplotlib.pyplot as plt


def ic(G,s):
    print(s)
    jst_inf=list(s)
    infected=list(s)
    while(1):
        print(jst_inf,' ',infected)
        if(len(jst_inf)==0):
            return infected
        tmp=[]
        for each in jst_inf:
            for each1 in G.neighbors(each):
                r=random.uniform(0,1)
                if(r<0.5 and each1 not in infected and each1 not in tmp):
                    tmp.append(each1)
        
        for each in tmp:
            infected.append(each)
        jst_inf=list(tmp)
            
                    

G=nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),
             (5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])

seed=[3,8]
list1=ic(G,seed)