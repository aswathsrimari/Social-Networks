# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 07:11:56 2019

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt
import random

def add_edges(G):
    list_nodes=list(G.nodes())
    #print(list_nodes)
    n=G.number_of_nodes()
    for i in range(len(list_nodes)):
        #print(list_nodes[i],list_nodes[i+1],list_nodes[i-1],list_nodes[i+2],list_nodes[i-2])
        G.add_edge(list_nodes[i],list_nodes[i-1])
        G.add_edge(list_nodes[i],list_nodes[i-2])
        target=i+1
        if(target>n-1):
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)
        target=i+2
        if(target>n-1):
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)
     
def add_long_link(G):
    #print('addd the weak tie edges')
    v1=int(random.choice(list(G.nodes())))
    v2=int(random.choice(list(G.nodes())))
    while(v1==v2):
        #print(v1,' ',v2)
        v1=int(random.choice(list(G.nodes())))
        v2=int(random.choice(list(G.nodes())))
    G.add_edge(v1,v2)  
    
    
def find_best_neighbor(G,c,v):
    dis=G.number_of_nodes()
    for each in G.neighbors(c):
        dis1=len(nx.shortest_path(H,source=each,target=v))
        if dis1<dis:
            dis=dis1
            choice=each
    return choice
def myopic_search(G,u,v):
    path=[u]
    current=u
    while(1):
        w=find_best_neighbor(G,current,v)
        path.append(w)
        current=w
        if(current==v):
            break;
    return path

def set_path_colors(G,p,p1):
    c=[]
    for each in G.nodes():
        if(each==p[0]):
            c.append('red')
        if(each==p[len(p)-1]):
            c.append('red')
        if(each in p and each in p1 and each!=p1[0] and each!=p1[len(p1)-1]):
            c.append('yellow')
        if(each in p and each not in p1): #nodes in myopic 
            c.append('blue')
        if(each in p1 and each not in p): #nodes in optimal
            c.append('green')
        if(each not in p and each not in p1):
            c.append('black')
    return c

    


G=nx.Graph()
G.add_nodes_from(range(0,100))

add_edges(G)  #add ties based on homophily

#for each in G.nodes():
#    print(each,'=',end="")
#    for each1 in G.neighbors(each):
#        print(each1,' ',end="")
#    print('\n')
    
#add_long_link(G)

H=G.copy() #network without weak tie to find distance of neighbors- myopic search
x=[0]
y=[nx.diameter(G)]
t=0
while(t<=10):
    add_long_link(G)
    t=t+1
    x.append(t)
    y.append(nx.diameter(G))
    
plt.xlabel('Number of weak ties added')
plt.ylabel('Diamter')
plt.plot(x,y)
plt.show()

m=[] #path length corresponding to myopic 
o=[] #path length corre..... to optimal
x=[] #each point on x axis is one pair of nodes -(0,49)(1,51)
t=0
for u in range(0,49):
    v=u+50
    p=myopic_search(G,u,v)
    p1=nx.shortest_path(G,source=u,target=v)
    m.append(len(p))
    o.append(len(p1))
    x.append(t)
    t=t+1
plt.plot(x,m,'r')
plt.plot(x,o,'b')
plt.show()
    
    
#p=myopic_search(G,0,40)
#p1=nx.shortest_path(G,source=0,target=40)

colors=set_path_colors(G,p,p1)

nx.draw(G,node_color=colors)
plt.show()
