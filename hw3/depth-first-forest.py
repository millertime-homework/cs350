#!/usr/bin/python

import sys

def main():
    test_graph = Graph()
    components,n = test_graph.depth_first_search()
    i = 1
    for c in components:
        sys.stdout.write("cc[%d] = " % i)
        i += 1
        print(c)
    print("%d total components" % n)

class Graph:
    """This is a single-use graph class
    It's going to traverse a disconnected graph
    and discover the graph's connected components"""
    def __init__(self):
        self.components = []
        # this is a python dict -- key,value pair (separated by ':') 
        # of vertex and adjacency list
        self.graph = { 'A': ['B',],
                       'B': ['A','C'],
                       'C': ['B',],
                       'D': ['E',],
                       'E': ['D',],
                       'F': ['G',],
                       'G': ['F','H'],
                       'H': ['G',] }
        # this is the 'color' label for each vertex: 
        #    unvisited, discovered, or visited
        self.status = {}
        for v in self.graph.keys():   # keys is the vertices from the graph dict
            self.status[v] = 'unvisited'
        
    def depth_first_search(self):
        """this is the algorithm from the slides"""
        for v in self.graph.keys():
            if self.status[v] == 'unvisited':
                self.components.append([])
                self.visit(v)
        return self.components,len(self.components)

    def visit(self, v):
        self.status[v] = 'discovered'
        if v not in self.components[len(self.components)-1]:
            self.components[len(self.components)-1].append(v)
        for u in self.graph[v]:
            if u not in self.components[len(self.components)-1]:
                self.components[len(self.components)-1].append(u)
            if self.status[u] == 'unvisited':
                self.visit(u)
            self.status[v] = 'visited'

if __name__=="__main__":
    main()
