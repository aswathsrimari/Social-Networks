# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 05:41:04 2019

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt 
import random
import numpy
#add nodes
def add_nodes(n):
    G=nx.Graph()
    n=int(n)
    G.add_nodes_from(list(range(n)))
    return G
#add one random edge
def add_random_edge(G):
    v1=random.choice(list(G.nodes))
    v2=random.choice(list(G.nodes))
    if v1!=v2:
        G.add_edge(v1,v2)
    return G
#keeps adding random edges untill G becomes connected
def keep_adding_edges(G):
    while(nx.is_connected(G)==False):
        G=add_random_edge(G)
    return G

def plot_graph(G):
    nx.draw(G,with_labels=True)
    plt.show()

def create_instance(n):
    G=add_nodes(n)
    G=add_random_edge(G)
    G=keep_adding_edges(G)
    return G.number_of_edges() 


#check below function not working
def create_avg_instance(n):
     i=0
     list1=[]
     while(i<5):
         list1.append(create_instance(n))
         i=i+1
     return numpy.average(list1)                     
def plot_connectivity():
    i=10
    x=[]
    y=[]
    while(i<=50):
        x.append(i)
        y.append(create_avg_instance(i))
        i=i+10
    plt.plot(x,y)
    plt.xlabel('number of nodes')
    plt.ylabel('number of edges required for connectedness')
    plt.title('emergence of connectedness')
    plt.show()
    
    i=10
    x1=[]
    y1=[]
    while(i<=50):
        x1.append(i)
        y1.append(i*numpy.log(i))
        i=i+10
    plt.plot(x1,y1)
    plt.xlabel('number of nodes')
    plt.ylabel('nlogn')
    plt.title('emergence of connectedness')
    plt.show()
  
    
   
    
    
n=input('enter the number of nodes')
G=add_nodes(n)
print('connected? ',nx.is_connected(G))
G=add_random_edge(G)
G=keep_adding_edges(G)
print('number of edges ',G.number_of_edges())
print('connected? ',nx.is_connected(G))
plot_graph(G)

plot_connectivity()