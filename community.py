# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:45:56 2019

@author: user
"""

import networkx as nx
import itertools
import matplotlib.pyplot as plt

def communities_Brute(G):
    nodes=G.nodes()
    n=G.number_of_nodes()
    first_Community=[]
    for i in range(1,n//2+1):
        com=[list(x) for x in itertools.combinations(nodes,i)]
        first_Community.extend(com)
    second_Community=[]
    print(first_Community)
    for i in range(len(first_Community)):
        l=list(set(nodes)-set(first_Community[i]))
        second_Community.append(l)
    num_intra_edges1=[]
    num_intra_edges2=[]
    num_inter_edges=[]
    ratio=[]
    for i in range(len(first_Community)):
        num_intra_edges1.append(G.subgraph(first_Community[i]).number_of_edges())
    for i in range(len(second_Community)):
        num_intra_edges2.append(G.subgraph(second_Community[i]).number_of_edges())
    e=G.number_of_edges()
    for i in range(len(first_Community)):
        num_inter_edges.append(e-num_intra_edges1[i]-num_intra_edges2[i])
    #ratio
    for i in range(len(first_Community)):
        ratio.append((float)(num_intra_edges1[i]+num_intra_edges2[i])/num_inter_edges[i])
        
    max_value=max(ratio)
    max_index=ratio.index(max_value)
    
    print('(',first_Community[max_index],'),(',second_Community[max_index],')')


G=nx.barbell_graph(4,1)
communities_Brute(G)
nx.draw(G)
plt.show()