#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:47:57 2018

@author: kaim

LABHW Ring and Shortcuts

Implement the network generation code for the "ring & shortcuts" network, 
based on the definition: "Take N≫1 nodes on a ring, where the links connect 
first and second neighbours. In addition, randomly distribute N/2 shortcuts 
among the nodes." Derive a computational estimate for the average clustering 
coefficient as N goes to infinity. Make sure that you have an estimate, which 
is not affected by random noise.

Note: although we suggested ensuring that the shortcuts are distributed 
evenly, i.e. that each node has exactly one shortcut edge added, but this
 severly complicates the implementation, so simply ensure that you are adding
 N/2 shortcut edges. Implementing this stricter variant is assigned as an optional homework.

Note 2: So far we only used plt.hist() for plotting. For this homework exercise,
 you might want to make other types of plots, for which plt.plot() might come in 
 handy: to plot a single data series, you can simply pass in a list of values: 
     plt.plot([1,2,3,4]). If you want to plot x-y values, you will need to pass 
     in two lists, one containing the x values, one containing those for y: 
         plt.plot([1,2,4,9,16], [1,2,3,4])
"""

import networkx
from random import *
import matplotlib.pyplot as plt

clustering = []
def make_ring(N):

   graph = networkx.Graph()

   for i in range(N):

       graph.add_node(i)


   for i in range(N):

       graph.add_edge(i, (i+1)%N)

       graph.add_edge(i, (i+2)%N)

   return graph

#networkx.draw_circular(make_ring(10))

def make_network(N):

   graph = make_ring(N)

   #print('NumEdges')
   #print(graph.number_of_edges())
   #print(int(2*N + N/2))
   while (graph.number_of_edges() <= (2*N + int(N/2))): 
       
       x = randint(0, graph.number_of_nodes()-1)
       #print(x)

       nodeList = list(graph.nodes())
       node = nodeList[x]
       #print(node)
       y = randint(0, graph.number_of_nodes()-1)

       while (x == y):
           y = randint(0, graph.number_of_nodes()-1)
           
       #print(y)
       node2List = list(graph.nodes())
       node2 = node2List[y]
       #print(node2)

       while (graph.has_edge(node, node2)):
           
           y = randint(0, graph.number_of_nodes()-1)
           
           node2 = node2List[y]


           #if graph.degree(node) == 4 and graph.degree(node2) == 4:
       #print(y)
       graph.add_edge(node, node2) 
   #print(networkx.average_clustering(graph))
   clustering.append(networkx.average_clustering(graph))
   return graph
l = []
for i in range(1,1000):
    N = 5+i
    l.append(N)
    print(N)
    g = make_network(N)
plt.plot(l, clustering)
print(clustering[N-6])
#networkx.draw_circular(g)


