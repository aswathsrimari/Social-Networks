    # -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:46:37 2019

@author: user
"""

import networkx as nx


def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G) 
    list_of_tuples = dict1.items()
    print(list_of_tuples)
    list_of_tuples=sorted(list_of_tuples,key=lambda x:x[1],reverse=True) #reverse true for descending
    #x:x[1] to sort based on second value in tuple
    return list_of_tuples[0][0] #returns edge (A,B) A-source B-end

def girvan(G):
    c=nx.connected_component_subgraphs(G) #returns an 'generator' of graphs
    n=len(list(c))
    print('no of connected components are ',n) #initially 1
    while(n==1):
      G.remove_edge(*edge_to_remove(G)) #((A,B)) -> (A,B) by unpack it (*)
      c=nx.connected_component_subgraphs(G)
      n=len(list(c))
      print('no of connected components are ',n)
    return c

G=nx.barbell_graph(5,0)
c=girvan(G)
for i in c:
   print(i.nodes()) 
      
      