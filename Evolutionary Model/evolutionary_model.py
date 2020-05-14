# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:20:06 2019

@author: user
"""
#membership,triadic,foci closure implemented  and homophily
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time
def create_graph():
    G=nx.Graph()
    for i in range(1,101):
        G.add_node(i);
        
    return G
def visualize(G,t):
    time.sleep(10)
    labeldict=get_labels(G)
    nodesize=get_size(G)
    colorarray=get_colors(G)

    nx.draw(G,labels=labeldict,node_size=nodesize,node_color=colorarray)
    plt.savefig('evolution.jpg') #update in the image
    plt.clf()
    plt.cla()
    nx.write_gml(G,'evolution_'+str(t)+'.gml')
    
def get_labels(G):
    dict1={}
    for each in G.nodes():
        dict1[each]=G.nodes[each]['name']
    return dict1
    
def get_size(G):
    array1=[]
    for each in G.nodes():
        if G.node[each]['type']=='person':
            array1.append(G.node[each]['name']*20)
        else:
            array1.append(1000)
            
    return array1
def assign_bmi(G):
    for each in G.nodes():
        G.nodes[each]['name']=random.randint(15,40)
        G.nodes[each]['type']='person'

def add_foci_nodes(G):
    n=G.number_of_nodes()
    i=n+1
    foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G.node[i]['name']=foci_nodes[j]
        G.node[i]['type']='foci'
        i=i+1
def get_colors(G):
    color=[]
    for each in G.nodes():
        if G.node[each]['type']=='person':
            if G.node[each]['name']==15:
                color.append('green')
            elif G.node[each]['name']==40:
                color.append('yellow')
            else:
                color.append('blue')
        else:
            color.append('red')
    return color
def get_foci_nodes(G):
    f=[]
    for each in G.nodes():
        if G.node[each]['type']=='foci':
            f.append(each)
    return f
def get_person_nodes(G):
    p=[]
    for each in G.nodes():
        if G.node[each]['type']=='person':
            p.append(each)
    return p
def add_foci_edges(G):
    foci_nodes=get_foci_nodes(G)
    person_nodes=get_person_nodes(G)
    for each in person_nodes:
        r=random.choice(foci_nodes)
        G.add_edge(each,r,len=3)
        
def cmn(u,v,G):
    uc=set(G.neighbors(u))
    vc=set(G.neighbors(v))
    return len(uc & vc)
def closure(G):
    array1=[]   
    for u in G.nodes():
        for v in G.nodes():
            if u!=v and (G.node[u]['type']=='person' or G.node[v]['type']=='person'):
                k=cmn(u,v,G)
                p=1-math.pow((1-0.1),k)
                temp=[]
                temp.append(u)
                temp.append(v)
                temp.append(p)
                array1.append(temp)
    for each in array1:
        u=each[0]
        v=each[1]
        p=each[2]
        r=random.uniform(0,1)
        if r<p:
            G.add_edge(u,v,len=3)

                
def Homophily(G):
    pnodes=get_person_nodes(G)
    for u in pnodes:
        for v in pnodes:
            if u!=v:
                diff=abs(G.node[u]['name']-G.node[v]['name'])
                p=float(1)/(diff+1000)
                r=random.uniform(0,1) 
                if r<p:
                    G.add_edge(u,v)


def change_bmi(G):
    fnodes=get_foci_nodes(G)
    for each in fnodes:
        if G.node[each]['name']=='eatout':
            for each1 in G.neighbors(each):
                if(G.node[each1]['name']!=40):
                    G.node[each1]['name']=G.node[each1]['name']+1
        if G.node[each]['name']=='gym':
            for each1 in G.neighbors(each):
                if(G.node[each1]['name']!=15):
                    G.node[each1]['name']=G.node[each1]['name']-1
G=create_graph()
assign_bmi(G)
add_foci_nodes(G)
add_foci_edges(G)
labeldict=get_labels(G)
nodesize=get_size(G)
colorarray=get_colors(G)
time.sleep(10)
t=0
visualize(G,t)
for t in range(10):
    #visualize(G)
    Homophily(G)
    #visualize(G)
    closure(G)
    change_bmi(G)
    visualize(G,t)  
#while(1): do this for membersip closure
#   closure(G) #membership closure also forms with foci closure
#   visualize(G,labeldict,nodesize,colorarray)