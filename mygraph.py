from heap import *
import math

# V : Vertices
# E : Edges
# t : Time
# Adj : Adjacency list
class Graph(object):
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.Adj = dict
        self.V = []
        self.E = []
        self.t = 0
        
    def add_vertex(self, v):
        if v not in self.Adj:
            self.Adj[v] = []
            self.V.append(v)

    def add_edge(self, e):
        if e.s and e.t in self.Adj:
            if e.dir:
                self.Adj[e.s].append(e.t)
                self.E.append(e)
            if not e.dir:
                self.Adj[e.s].append(e.t)
                self.Adj[e.s].append(e.s)
                self.E.append(e)
                self.E.append(Edge((e.s, e.s), dir = False))
                
    def Vertices(self):
        return {v.n for v in self.V}
        
    def Edges(self):
        return [e.n for e in self.E]
        
    def BFS(self):
        return {v.n:[v.v, v.c] for v in self.V}
        
    def DFS(self):
        return {v.n:[v.pre, v.post, v.c] for v in self.V}
        
    def Dijkstra(self):
        return {v.n:[v.d, v.pred.n] for v in self.V if v.pred is not None}
    
# n : Name
# c : Color
# v : Value
# pred : Predecessor
# pre & post : Enter and exit time of a vertex
class Vertex:
    def __init__(self, n, mark = False, v = 0, pred = None, d = 0):
        self.n = n
        self.c = 'W'
        self.v = v
        self.d = d
        self.pred = pred
        self.pre = 0
        self.post = 0

# s : Source
# t : Target
# n : Name
# w : Weight
# dir : Direted
class Edge:
    def __init__(self, e, w = 1, dir = True):
        v1, v2 = e
        self.s = v1
        self.t = v2
        self.n = (self.s.n, self.t.n)
        self.w = w
        self.dir = dir

        
# l : Label
# n : Name
# num : Number of vertices in a component
# o : Outgoing edges
# i : Incoming edges
class Component:
    def __init__(self, V):
        self.n = [v.n for v in V]
        self.l = 0
        self.num = len(V)
        self.o = 
        
''' 
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i-1)/2
        
    def insertKey(self, k):
        heappush(self.heap.k)
        
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])
    
    def extractMin(self):
        return heappop(self.heap)
        
    def deleteKey(self, i):
        self.decreaseKey(i, -math.inf)
        self.extractMin()
'''

def INITGRAPH(G, V, E):
    for v in V:
        G.add_vertex(v)
    for e in E:
        G.add_edge(e)
         
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
    
    INITGRAPH(G, V, E)
    
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
    v1 = Vertex('v1')
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
    
    INITGRAPH(G, V, E)
    
    return G, v1
    
def DFS(G, s):
    G.t = 0
    for u in G.V:
        if u.c == 'W':
            DFS_Visit(G, u)

def DFS_Visit(G, u):
    u.c = 'G'
    G.t = G.t + 1
    u.pre = G.t
    for v in G.Adj[u]:
        if v.c == 'W':
            DFS_Visit(G, v)
    u.c = 'B'
    G.t = G.t + 1
    u.post = G.t
   
def INITDijkstra():
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')
    v5 = Vertex('v5')
    v6 = Vertex('v6')
    v7 = Vertex('v7')

    e1 = Edge((v1, v2), w = 3)
    e2 = Edge((v1, v3), w = 4)
    e3 = Edge((v2, v4), w = 12)
    e4 = Edge((v3, v4), w = 5)
    e5 = Edge((v3, v5), w = 0)
    e6 = Edge((v5, v6), w = 3)
    e7 = Edge((v5, v7), w = 10)
    e8 = Edge((v7, v3), w = 8)
    e9 = Edge((v7, v1), w = 4)
    e10 = Edge((v2, v5), w = 2)
    e11 = Edge((v2, v3), w = 7)
    
    G = Graph()
    V = [v1, v2, v3, v4, v5, v6, v7]
    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]
    
    INITGRAPH(G, V, E)
    
    return G, v1
   
def INITSSSP(G, s):
    s.d = 0
    s.pred = None
    for v in [v for v in G.V if v != s]:
        v.d = math.inf
        v.p = None
        
def TENSE(e):
    return e.t.d > e.s.d + e.w
        
def RELAX(e):
    e.t.d = e.s.d + e.w
    e.t.pred = e.s

def OutgoingEdges(G, s):
    return [e for e in G.E if e.s == s]
    
def IncomingEdges(G, s):
    return [e for e in G.E if e.t == s]
    
def Dijkstra(G, s):
    INITSSSP(G, s)
    pq = Heap(min = True)
    pq.Push(s, s.d)
    while not pq.IsEmpty():
        u, dist = pq.Extract()
        for e in OutgoingEdges(G, u):
            if TENSE(e):
                RELAX(e)
                if pq.IsInHeap(e.t):
                    pq.UpdateKey(e.t, e.t.d)
                else:
                    pq.Push(e.t, e.t.d)

#def BFS(G, t, s, sp):
                   
def ReverseGraph(G):
    new_Graph = Graph()
    E = [Edge((e.t, e.s), w = e.w) for e in G.E]
    INITGRAPH(new_Graph, G.V, E)
    return new_Graph
                   
def NumOfShortestPaths(G, H, s, t):
    Dijkstra(G, s)
                    
if __name__ == "__main__":
    
    # BFS test case
    '''
    G, s = INITBFS()
    BFS(G, s) 
    print(G.BFS())
    '''
    
    # DFS test case
    '''
    G, s = INITDFS()
    #DFS(G, s)
    #print(G.DFS())
    '''
    
    # Dijkstra test case
    
    G, s = INITDijkstra()
    Dijkstra(G, s)
    #print(G.Dijkstra())
    print(G.Edges())
    G = ReverseGraph(G)
    print(G.Edges())
    
    #print(G.E)
    #print([e.n for e in G.E if e.s == s])
    
    