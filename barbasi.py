# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 07:12:54 2019

@author: user
"""

import networkx as nx
import random
import matplotlib.pyplot as plt


def display_graph(G,i,ne):
    pos=nx.circular_layout(G)
    if i=='' and ne=='':
        new_node=[]
        rest_nodes=G.nodes()
        new_edges=[]
        rest_edges=G.edges()
    else:
        new_node=[i]
        rest_nodes=list(set(G.nodes())-set(new_node))
        new_edges=ne
        rest_edges=list(set(G.edges())-set(new_edges)-set([(b,a) for (a,b) in new_edges]))
    nx.draw_networkx_nodes(G,pos,nodelist=new_node,node_color='g')
    nx.draw_networkx_nodes(G,pos,nodelist=rest_nodes,node_color='r')
    nx.draw_networkx_edges(G,pos,edgelist=new_edges,edge_color='g',style='dashdot')
    nx.draw_networkx_edges(G,pos,edgelist=rest_edges,edge_color='g') 
    plt.show()
    
def add_nodes_barabasi(G,n,m0):
    m=m0-1
    
    for i in range(m0+1,n+1):
        G.add_node(i)
        #add the edges one by one
        #preprocessing
        degrees=nx.degree(G)  #returns dict of (node:value-degree) DegreeView object    
        node_probabilities={}
        
        for each in G.nodes():
            node_probabilities[each]=(float)(degrees[each]/sum(dict(degrees).values()))
            
        node_probabilities_cum=[]
        prev=0
        for n,p in node_probabilities.items():
            temp=[n,prev+p]
            node_probabilities_cum.append(temp)
            prev=prev+p
        new_edges=[]
        
        num_edges_added=0
        target_nodes=[]
        
        while(num_edges_added<m):
            prev_cum=0
            r=random.random() #float value between 0 and 1..if uniform(a,b) range specified
            k=0
            while(not(r>prev_cum and r<=node_probabilities_cum[k][1])):
               prev_cum=node_probabilities_cum[k][1]
               k+=1
            target_node=node_probabilities_cum[k][0]
            if target_node in target_nodes:
                continue
            else:
                target_nodes.append(target_node)
        
            G.add_edge(i,target_node)
            num_edges_added+=1
            new_edges.append((i,target_node))
        
        print(num_edges_added, 'edges added')
        display_graph(G,i,new_edges)
    return G

def plot_deg_dist(G):
    
    all_degrees=list(dict(nx.degree(G)).values()) #all the degrees
    unique_degrees=list(set(all_degrees)) 
    unique_degrees.sort()
    count_of_degrees=[]
    
    for i in unique_degrees:
        c=all_degrees.count(i)
        count_of_degrees.append(c)
        
    print(unique_degrees)
    print(count_of_degrees)
    
    
    plt.plot(unique_degrees,count_of_degrees,'ro-')
    #loglog plot will give a straight line for power law graph
    plt.xlabel('Degrees')
    plt.ylabel('Number of nodes')
    plt.title('Degree distribution')
    plt.show()
    
    
      
            
        
        
        
def main():
    n=int(input('enter the value of n'))
    m0=random.randint(2,n/5)
    #m<=m0
    G=nx.path_graph(m0)
    #m=m0-1
    
    display_graph(G,'','')
    G=add_nodes_barabasi(G,n,m0)
   # input()
    plot_deg_dist(G)
    
main()
    