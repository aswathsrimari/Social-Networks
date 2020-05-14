# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 03:59:37 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 03:40:06 2019

@author: user
"""
#independent cascade model

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from collections import OrderedDict

def ic(G,s):
    #print(s)
    jst_inf=list(s)
    infected=list(s)
    while(1):
        #print(jst_inf,' ',infected)
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
            
    return infected                

G=nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),
             (5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])

dict_deg={}
dict_cl={}
dict_bw={}
dict_cr={}

for each in G.nodes():
    dict_deg[each]=G.degree(each)
    dict_cl[each]=nx.closeness_centrality(G,each)
    dict_bw[each]=nx.betweenness_centrality(G,each)
    dict_cr[each]=nx.core_number(G)[each] #returns dict with core number for each node
dict_cascade={}
for each in G.nodes():
    c=[]
    for num in range(0,1000):
        seed=[each]
        i=ic(G,seed)
        c.append(len(i))
    dict_cascade[each]=np.average(c)
sorted_dict_cascade=OrderedDict(sorted(dict_cascade.items(), key=itemgetter(1)))
sorted_dict_cl=OrderedDict(sorted(dict_cl.items(), key=itemgetter(1)))
#sorted_dict_bw=OrderedDict(sorted(dict_bw.items(), key=itemgetter(1)))
#sorted_dict_cr=OrderedDict(sorted(dict_cr.items(), key=itemgetter(1)))    
print(sorted_dict_cascade)
print(sorted_dict_cl)
##print(sorted_dict_bw)
#print(sorted_dict_cr)
#seed=[3,8]
#list1=ic(G,seed)