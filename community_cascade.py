# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:24:35 2019

@author: user
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def create_first_community(G):
    for i in range(0,10):
        G.add_node(i)
    for i in range(0,10):
        for j in range(0,10):
            if i<j:
                r=random.uniform(0,1)
                if r<0.5:
                    G.add_edge(i,j)
                    
def create_second_community(G):
    for i in range(11,20):
        G.add_node(i)
    for i in range(11,20):
        for j in range(11,20):
            if i<j:
                r=random.uniform(0,1)
                if r<0.5:
                    G.add_edge(i,j)


G=nx.Graph()
create_first_community(G)
create_second_community(G)
G.add_edge(5,15)
#nx.draw(G)
#plt.show()

nx.write_gml(G,'random_graph_community.gml')
