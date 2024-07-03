from sys import stdin
from datetime import datetime

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = set()
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    # find a path from start_vertex to end_vertex in graph - BFS
    def find_path(self, start_vertex, end_vertex, path=None):
            if path == None:
                path = []
            graph = self._graph_dict
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return path
            if start_vertex not in graph:
                return None
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_path = self.find_path(vertex, 
                                                  end_vertex, 
                                                  path)
                    if extended_path: 
                        return extended_path
            return None

    # find all paths from start_vertex to end_vertex in graph
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self._graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

def main():
    # parse input
    dictionary, cases = map(lambda s: s.split('\n'), stdin.read().strip().split('\n\n')) # this line might be slow too? but I tested it with a random jumble of 25k words and it finished almost instantly
    # print(dictionary, cases)
    # ['booster', 'rooster', 'roaster', 'coasted', 'roasted', 'coastal', 'postal'], ['booster roasted', 'coastal postal']
    print('done reading at', datetime.now().minute, datetime.now().second)
    # create graph to represent word relations
    g = Graph()
    for word in dictionary:
        g.add_vertex(word)

    L = len(dictionary)
    # add edge between all words of diff 1
    for i, word_1 in enumerate(dictionary):
        for j in range(i, L):
            if evans_lev_dist(word_1, dictionary[j]) == 1:
                g.add_edge([word_1, dictionary[j]])

    print('done making graph at', datetime.now().minute, datetime.now().second)

    # find solutions to all cases
    for case in cases:
        start, end = case.split()
        path = g.find_path(start, end)
        if path:
            for node in path:
                print(node)
        else:
            print("No solution.")
        print()

    print('done at', datetime.now().minute, datetime.now().second)

def evans_lev_dist(str1: str, str2: str) -> int: # O(n) complexity
    '''returns 0/1 if lev dist between two words of the same length are 0/1 respectively, or 2 otherwise'''
    diff = 0
    for c1, c2 in zip(str1, str2):
        if diff > 1:
            break
        if c1 == c2:
            continue
        else:
            diff += 1
    return diff

# trash, the issue likely isn't with the dist function, we're already at O(n)
# def evan_lev_dist_v2(str1: str, str2: str) -> int:
#     str1 = str1.encode()
#     str2 = str2.encode()
#     print(str1)
#     print(str2)

#     print(str1 ^ str2)

if __name__ == '__main__':
  main()