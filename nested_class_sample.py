from heap import *
import math

class Graph(object):
    def __init__(self, dictionary=None):
        if dictionary == None:
            dictionary = {}
        self.adjacency_list = dictionary
        self.vertices = []
        self.edges = []
        self.time = 0
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.append(vertex)

    def add_edge(self, edge):
        if edge.source and edge.target in self.adjacency_list:
            if edge.directed:
                self.adjacency_list[edge.source].append(edge.target)
                self.edges.append(edge)
            if not edge.directed:
                self.adjacency_list[edge.source].append(edge.target)
                self.adjacency_list[edge.target].append(edge.source)
                self.edges.append(edge)
                self.edges.append(Edge((edge.source, edge.source), directed=False))
                
    def Vertices(self):
        return {vertex.name for vertex in self.vertices}
        
    def Edges(self):
        return [edge.name for edge in self.edges]
        
    class Vertex:
        def __init__(self, name, mark=False, value=0, predesessor=None, distance=0):
            self.name = name
            self.color = 'white'
            self.value = value
            self.distance = distance
            self.predesessor = predesessor
            self.pre = 0
            self.post = 0
            
    class Edge:
        def __init__(self, edge, weight=1, directed=True):
            vertex_1, vertex_2 = edge
            self.source = vertex_1
            self.target = vertex_2
            self.name = (self.source.name, self.target.name)
            self.weight = weight
            self.directed = directed
            
    class Component:
        def __init__(self, vertices):
            self.name = [v.name for v in vertices]
            self.label = 0
            self.size = len(vertices)
        
def init_graph(graph, vertices, edges):
    for v in vertices:
        graph.add_vertex(v)
    for e in edges:
        graph.add_edge(e)
        
def init_bfs():
    graph = Graph()
    
    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')

    e1 = Edge((v, r), directed=False)
    e2 = Edge((r, s), directed=False)
    e3 = Edge((s, w), directed=False)
    e4 = Edge((w, t), directed=False)
    e5 = Edge((w, x), directed=False)
    e6 = Edge((t, x), directed=False)
    e7 = Edge((t, u), directed=False)
    e8 = Edge((x, y), directed=False)
    e9 = Edge((u, y), directed=False)
    
    
    vertices = [r, s, t, u, v, w, x, y]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
    source = s
    
    init_graph(graph, vertices, edges)
    
    return graph, source
    
def bfs(graph, source):
    queue = [source]
    while queue:
        u = queue.pop(0)
        for v in graph.adjacency_list[u]:
            if v.color == 'white':
                v.color = 'grey'
                v.value = u.value + 1
                v.predesessor = u
                queue.append(v)
        u.color = 'black'
    return {v.name:[v.value, v.color] for v in graph.vertices}

       
if __name__ == "__main__":
    
    # BFS test case
    #graph, source = init_bfs()
    #print(bfs(graph, source))
    g = Graph()
    r = g.Vertex('r')
    g.add_vertex(r)
    
    print(g.vertices())
    