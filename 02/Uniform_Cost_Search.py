#!/usr/bin/env python

import heapq

def build_graph_weighted(file) :
    graph={}
    for line in file :
        v1,v2,w=line.split(',')
        v1,v2,w=v1.strip(),v2.strip(),int(w.strip())
        if v1 not in graph :
            graph[v1]={}
        if v2 not in graph :
            graph[v2]={}
        graph[v1][v2]=w
        graph[v2][v1]=w
    return graph

def ucs(graph, start, dest) :
    frontier=[]
    heapq.heappush(frontier,(0,[(start,0)]))
    explored= set()
    while len(frontier)!=0 :
        for i in range(len(frontier)) :
            print(frontier[i])
        print()
        path=heapq.heappop(frontier)[1]
        node=path[-1][0]
        g_cost=path[-1][1]
        explored.add(node)
        if node==dest :
            return [x for x, y in path]
        for neighbor, distance in graph[node].items() :
            total_cost=g_cost+distance
            new_path=path+[(neighbor,total_cost)]
            if neighbor not in explored :
                heapq.heappush(frontier,(total_cost,new_path))
            elif neighbor in frontier :
                if total_cost < frontier[0] :
                    heapq.heappush(frontier,(total_cost,new_path))
                print(path)
    return False

with open('Graph.txt','r') as file :
    lines= file.readlines()
start=lines[1].strip()
dest=lines[2].strip()
graph=build_graph_weighted(lines[4:])
print(ucs(graph,start,dest),"\n\n")