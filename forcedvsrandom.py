# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:01:47 2019

@author: user
"""

import networkx as nx
import random

def main():
    G=nx.read_edgelist('email.txt')
    print(nx.info(G))
    
    
main()