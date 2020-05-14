# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:25:32 2019

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def get_signs_of_tris(tri_list,G):
    all_signs=[]
    for i in range(len(tri_list)):
        temp=[]
        temp.append(G[tri_list[i][0]][tri_list[i][1]]['sign'])
        temp.append(G[tri_list[i][1]][tri_list[i][2]]['sign'])
        temp.append(G[tri_list[i][2]][tri_list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs
def count_unstable(all_signs,G):
    stable=0
    unstable=0
    for i in range(len(all_signs)):
        if all_signs[i].count('+')==3 or all_signs[i].count('+')==1:
            stable+=1
        elif all_signs[i].count('+')==2 or all_signs[i].count('+')==0:
            unstable+=1
    print('unstable triangles ',unstable)
    print('stable triangles ',stable)
    return unstable
def move_a_Tri_to_stable(G,tri_list,all_signs):
    found_unstable=False
    while(found_unstable==False):
        index = random.randint(0,len(tri_list)-1)
        if all_signs[index].count('+')==2 or all_signs[index].count('+')==0:
            found_unstable=True
        else:
            continue
    r=random.randint(1,3)
    if all_signs[index].count('+')==2:
        if(r==1):
            if G[tri_list[index][0]][tri_list[index][1]]['sign']=='+':
                G[tri_list[index][0]][tri_list[index][1]]['sign']='-'
            elif G[tri_list[index][0]][tri_list[index][1]]['sign']=='-':
                G[tri_list[index][0]][tri_list[index][1]]['sign']='+'
        elif(r==2):
            if G[tri_list[index][1]][tri_list[index][2]]['sign']=='+':
                G[tri_list[index][1]][tri_list[index][2]]['sign']='-'
            elif G[tri_list[index][1]][tri_list[index][2]]['sign']=='-':
                G[tri_list[index][1]][tri_list[index][2]]['sign']='+'
        elif(r==3):
            if G[tri_list[index][0]][tri_list[index][2]]['sign']=='+':
                G[tri_list[index][0]][tri_list[index][2]]['sign']='-'
            elif G[tri_list[index][0]][tri_list[index][2]]['sign']=='-':
                G[tri_list[index][0]][tri_list[index][2]]['sign']='+'
    elif all_signs[index].count('+')==0:
        if(r==1):
            G[tri_list[index][0]][tri_list[index][1]]['sign']='+'
        elif(r==2):
            G[tri_list[index][1]][tri_list[index][2]]['sign']='+'
        elif(r==3):
            G[tri_list[index][0]][tri_list[index][2]]['sign']='+'
    return G        
            
def see_coalitions(G):
    first_coalitions=[]
    second_coalitions=[]
    nodes=G.nodes()
    r=random.choices(nodes)
    processed_nodes=[]
    to_be_processed=[r]
    for each in to_be_processed:
        if each not in processed_nodes:
            neigh=G.neighbors(each)
            
            for i in range(len(neigh)):
                if G[each][neigh[i]]['sign']=='+':
                    if neigh[i] not in first_coalitions:
                        first_coalitions.append(neigh[i])
                    if neigh[i] not in to_be_processed:
                        to_be_processed.append(neigh[i])
                elif G[each][neigh[i]]['sign']=='-':
                    if neigh[i] not in second_coalitions:
                        second_coalitions.append(neigh[i])
                        processed_nodes.append(neigh[i])
            processed_nodes.append(each)            
                    
    return first_coalitions,second_coalitions
    
            
                
G=nx.Graph()
n=8
node_list=[i for i in range(1,n+1)]
#print(node)
G.add_nodes_from(node_list)
mapping = {1:'America',2:'Brazil',3:'India',4:'Japan',5:'Pakistan'}
G=nx.relabel_nodes(G,mapping)
signs=['+','-']
for i in G.nodes(): 
    for j in G.nodes():
        if i!=j:
            G.add_edge(i,j,sign=random.choice(signs))

edge_labels= nx.get_edge_attributes(G,'sign')
pos=nx.circular_layout(G)
nx.draw(G,pos, node_size=5000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='red')
plt.show()

nodes=G.nodes()
tri_list=[list(x) for x in itertools.combinations(nodes,3)]
all_signs= get_signs_of_tris(tri_list,G) #[[+,-,-].[]]
unstable=count_unstable(all_signs,G)
unstable_track=[unstable]
while(unstable!=0):
    G= move_a_Tri_to_stable(G,tri_list,all_signs)
    all_signs= get_signs_of_tris(tri_list,G) #[[+,-,-].[]]
    unstable=count_unstable(all_signs,G)
    unstable_track.append(unstable)
    
plt.bar([i for i in range(len(unstable_track))],unstable_track)
plt.show()  

edge_labels= nx.get_edge_attributes(G,'sign')
pos=nx.circular_layout(G)
nx.draw(G,pos, node_size=5000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='red')
plt.show()

first,second=see_coalitions(G)
print(first)
print(second)

raw_input() 
edge_labels= nx.get_edge_attributes(G,'sign')
pos=nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,nodelist=first,node_color='red',node_size=5000,alpha=0.8)
nx.draw_networkx_nodes(G,pos,nodelist=second,node_color='blue',node_size=5000,alpha=0.8) 
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='green')
plt.show()
    