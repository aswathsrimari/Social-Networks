# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:04:55 2019

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt

def plot_density():
    x=[]
    y=[]
    for i in range(0,5):
        G=nx.read_gml('evolution_'+str(i)+'.gml')
        x.append(i)
        y.append(nx.density(G))
    plt.xlabel('time')
    plt.ylabel('density')
    plt.title('change in density')
    plt.plot(x,y)
    plt.show()
 
def obesity(G):
    num=0
    for each in G.node():
        if G.node[each]['name']==40:
            num=num+1
    return num
    
def plot_obesity():
    x=[]
    y=[]
    for i in range(0,5  ):
        G=nx.read_gml('evolution_'+str(i)+'.gml')
        x.append(i)
        y.append(obesity(G))
    plt.xlabel('time')
    plt.ylabel('obesity')
    plt.title('change in obesity')
    plt.plot(x,y)
    
plot_density()
plot_obesity()