class Graph(object):
    
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.Adj = dict
        self.v = []
        self.e = []
        
    def add_vertex(self, v):
        if v not in self.Adj:
            self.Adj[v] = []
            self.v.append(v)

    def add_edge(self, e):
        if e.s and e.t in self.Adj:
            if e.dir:
                self.Adj[e.s].append(e.t)
                self.e.append(e)
            if not e.dir:
                self.Adj[e.s].append(e.t)
                self.Adj[e.s].append(e.s)
                self.e.append(e)
                self.e.append(Edge((e.s, e.s), dir = False))
                
    def V(self):
        return {v.n:[v.v, v.c] for v in self.v}
    
    def E(self):
        return [e.n for e in self.e]
        
class Vertex:
    def __init__(self, n, mark = False, v = 0, pred = None):
        self.n = n
        self.c = 'W'
        self.v = v
        self.pred = pred 
        self.pre = 0
        self.post = 0

class Edge:
    def __init__(self, e, w = 1, dir = True):
        v1, v2 = e
        self.s = v1
        self.t = v2
        self.n = (self.s.n, self.t.n)
        self.w = w
        self.dir = dir
    
def INITBFS():
    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')

    e1 = Edge((v, r), dir = False)
    e2 = Edge((r, s), dir = False)
    e3 = Edge((s, w), dir = False)
    e4 = Edge((w, t), dir = False)
    e5 = Edge((w, x), dir = False)
    e6 = Edge((t, x), dir = False)
    e7 = Edge((t, u), dir = False)
    e8 = Edge((x, y), dir = False)
    e9 = Edge((u, y), dir = False)
    
    G = Graph()
    V = [r, s, t, u, v, w, x, y]
    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
    
    for v in V:
        G.add_vertex(v)
    for e in E:
        G.add_edge(e)
    
    return G, s
    
def BFS(G, s):
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in G.Adj[u]:
            if v.c == 'W':
                v.c = 'G'
                v.v = u.v + 1
                v.pred = u
                Q.append(v)
        u.c = 'B'
     
def INITDFS():
    s = v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')
    v5 = Vertex('v5')
    v6 = Vertex('v6')
    v7 = Vertex('v7')
    v8 = Vertex('v8')

    e1 = Edge((v1, v2))
    e2 = Edge((v1, v4))
    e3 = Edge((v1, v5))
    e4 = Edge((v2, v3))
    e5 = Edge((v2, v4))
    e6 = Edge((v3, v1))
    e7 = Edge((v4, v3))
    e8 = Edge((v5, v4))
    e9 = Edge((v5, v6))
    e10 = Edge((v6, v4))
    e11 = Edge((v7, v5))
    e12 = Edge((v7, v6))
    e13 = Edge((v7, v8))
    e14 = Edge((v8, v4))
    
    G = Graph()
    V = [v1, v2, v3, v4, v5, v6, v7, v8]
    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
    
    return G, s
    
def DFS(G, s):
    time = 0
    for u in G.Adj[s]:
        if u.c == 'W':
            DFS_Visit(G, u, time)

def DFS_Visit(G, u, time):
    u.c = 'G'
    time = time + 1
    u.pre = time
    #for v in G.
    

     
if __name__ == "__main__":
    
    G, s = INITBFS()
    BFS(G, s) 
    print(G.V())
    
    G, E = INITDFS()
    print(E)