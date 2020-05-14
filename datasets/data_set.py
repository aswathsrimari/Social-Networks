# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:44:12 2019

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt
#G=nx.read_edgelist('facebook_combined.txt')

def plot_Deg_distribution(G):
    #print(nx.degree(G))
    all_degrees=list(dict(nx.degree(G)).values())
    unique=list(set(all_degrees))
    count_of_Degrees=[]
    for i in unique:
        count_of_Degrees.append(all_degrees.count(i))
    print('unique degrees ',unique)
    print('count of nodes with a degree ',count_of_Degrees)
    plt.plot(unique,count_of_Degrees,'ro-')
    plt.show()
G=nx.read_gml('internet_routers-22july06.gml')
print(nx.info(G))
print(nx.number_of_edges(G))
print(nx.number_of_nodes(G))
print(nx.is_directed(G)) 
#print(dict(nx.degree(G)))
#nx.draw(G)
#plt.show()
plot_Deg_distribution(G)
print('density of graph ',nx.density(G))
print('clustering coefficient ',nx.clustering(G).items())
print('diameter ',nx.diameter(G))