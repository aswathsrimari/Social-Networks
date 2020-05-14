# -*- coding: utf-8 -*-



import random
import matplotlib.pyplot as plt
import networkx as nx

city=['coimbatore','chennai','madurai','tirpur','salem']
G=nx.Graph()
for each in city:
    G.add_node(each)
cost=[]
value=100
while(value<=2000):
    cost.append(value)
    value=value+100;
print(cost)
print('number of nodes ',G.number_of_nodes())
#add 16 edges to the graph
while(G.number_of_edges()<=5):
        c1=random.choice(list(G.nodes))
        c2=random.choice(list(G.nodes))
        if(c1!=c2 and G.has_edge(c1,c1)==0):
                w=random.choice(cost)
                G.add_edge(c1,c2,weight=w)
print('nodes ',list(G.nodes))
print('edges ',list(G.edges))

#different layout available 
nx.draw(G,with_labels=1)
plt.show()