#!/usr/bin/env python
from collections import defaultdict
class Graph:
    def __init__(self,vertices): 
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def printGraph(self):
        print(self.graph)
    def DLS(self,src,target,maxDepth):  
        if src == target :
            return True
        if maxDepth <= 0 :
            return False
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False
g = Graph(9)
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
g.addEdge(3,7)
g.addEdge(3,8)
target = 7; maxDepth = 2; src = 0
g.printGraph()
if g.DLS(src,target,maxDepth) == True:
    print("Target %d is reachable from source %d within max depth %d" %(target,src, maxDepth))
else: 
    print("Target %d is NOT reachable from source %d within max depth %d" % (target,src, maxDepth))