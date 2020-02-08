class Graph(object):
    
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.adjacent = dict
        self.vertices = []
        self.edges = []
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []
            self.vertices.append(vertex)

    def add_edge(self, edge):
        if edge.src and edge.dst in self.adjacent:
            if edge.directed:
                self.adjacent[edge.src].append(edge.dst)
                self.edges.append(edge)
            ##if not edge.directed:
                self.adjacent[edge.src].append(edge.dst)
                self.adjacent[edge.dst].append(edge.src)
    
    def V(self):
        return [v.name for v in self.vertices]
    
    def E(self):
        return [e.name for e in self.edges]
        
class Vertex:
    def __init__(self, name, mark = False, value = 0, pred = None):
        self.name = name
        self.color = 'White'
        self.value = value
        self.pred = pred 

class Edge:
    def __init__(self, edge, weight = 1, directed = True):
        v1, v2 = edge
        self.src = v1
        self.dst = v2
        self.name = (self.src.name, self.dst.name)
        self.weight = weight
        self.directed = directed
    
def BFS(G, s):
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in graph.adjacent[u]:
            if v.color == 'WHITE':
                v.color = 'GREY'
                v.value = u.value + 1
                v.pred = u
                Q.append(v)
        u.color = 'BLACK'

if __name__ == "__main__":
    
    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    
    V = [r, s, t, u, v, w, x, y]
    
    G = Graph()
    
    for v in V:
        G.add_vertex(v)
        
    e1 = Edge((s,t), directed = False)
    ##G.add_edge(e1)
    
    print(G.V())
    
    print(G.E())