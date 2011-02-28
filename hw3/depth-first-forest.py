#!/usr/bin/python

def main():
    test_graph = Graph()
    components,n = test_graph.depth_first_search()

class Graph:
    """This is a single-use graph class
    It's going to traverse a disconnected graph
    and discover the graph's connected components"""
    def __init__(self):
        # this is a python dict -- key,value pair (separated by ':') 
        # of vertex and adjacency list
        self.time = 0
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
                    self.visit(v)

        def visit(self, v):
    
