from heap import *
import math
import random

class Graph(object):
    def __init__(self, dictionary=None):
        if dictionary == None:
            dictionary = {}
        self.adjacency_list = dictionary
        self.vertices = []
        self.edges = []
        self.time = 0
        self.count = 0
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.append(vertex)

    def add_edge(self, edge):
        if edge.source and edge.target in self.adjacency_list:
            if edge.directed:
                self.adjacency_list[edge.source].append(edge.target)
                self.edges.append(edge)
                edge.source.outgoing_edges.append(edge)
                edge.target.incoming_edges.append(edge)
            if not edge.directed:
                self.adjacency_list[edge.source].append(edge.target)
                self.adjacency_list[edge.target].append(edge.source)
                edge.directed = True
                second_edge = Edge((edge.target, edge.source), weight=edge.weight)
                self.edges.append(edge)
                self.edges.append(second_edge)
                edge.source.outgoing_edges.append(edge)
                edge.target.incoming_edges.append(edge)
                edge.target.outgoing_edges.append(second_edge)
                edge.source.incoming_edges.append(second_edge)
                
    def __str__(self):
        return '\nVertices :\n%s\n\nEdges :\n%s' %(str([v.name for v in self.vertices]), str([e.name for e in self.edges]))    
        
class Vertex:
    def __init__(self, name, mark=False, value=0, label=0, predesessor=None, distance=0, status='new', unmarked=True):
        self.name = name
        self.color = 'white'
        self.value = value
        self.label = 0
        self.distance = distance
        self.predesessor = predesessor
        self.pre = 0
        self.post = 0
        self.set = []
        self.status = status
        self.unmarked = True
        self.outgoing_edges = []
        self.incoming_edges = []
        self.neighbors = []
        self.root = None
        
class Edge:
    def __init__(self, edge, weight=1, directed=True):
        vertex_1, vertex_2 = edge
        self.source = vertex_1
        self.target = vertex_2
        self.name = (self.source.name, self.target.name)
        self.weight = weight
        self.directed = directed
              
def init_graph(graph, vertices, edges):
    reset_vertices(vertices)
    for v in vertices:
        graph.add_vertex(v)
    for e in edges:
        graph.add_edge(e)
        
def init_graph_bfs():
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
    
    graph = Graph()
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
  
def init_graph_dfs():
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

    graph = Graph()
    vertices = [v1, v2, v3, v4, v5, v6, v7, v8]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
    source = v1
    
    init_graph(graph, vertices, edges)
    
    return graph, source
  
def init_dfs(graph):
    graph.time = 0
    for v in graph.vertices:
        v.color = 'white'
        v.pre = 0
        v.post = 0
  
def dfs(graph, source):
    init_dfs(graph)
    for u in graph.vertices:
        if u.color == 'white':
            dfs_visit(graph, u)

def dfs_visit(graph, u):
    u.color = 'grey'
    graph.time = graph.time + 1
    u.pre = graph.time
    for v in graph.adjacency_list[u]:
        if v.color == 'white':
            dfs_visit(graph, v)
    u.color = 'black'
    graph.time = graph.time + 1
    u.post = graph.time
  
def init_graph_dijkstra():
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')
    v5 = Vertex('v5')
    v6 = Vertex('v6')
    v7 = Vertex('v7')

    e1 = Edge((v1, v2), weight=3)
    e2 = Edge((v1, v3), weight=4)
    e3 = Edge((v2, v4), weight=12)
    e4 = Edge((v3, v4), weight=5)
    e5 = Edge((v3, v5), weight=0)
    e6 = Edge((v5, v6), weight=3)
    e7 = Edge((v5, v7), weight=10)
    e8 = Edge((v7, v3), weight=8)
    e9 = Edge((v7, v1), weight=4)
    e10 = Edge((v2, v5), weight=2)
    e11 = Edge((v2, v3), weight=7)
    
    graph = Graph()
    vertices = [v1, v2, v3, v4, v5, v6, v7]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]
    source = v1
    
    init_graph(graph, vertices, edges)
    
    return graph, source
    
def init_sssp(graph, source):
    source.distance = 0
    source.pred = None
    for v in [v for v in graph.vertices if v != source]:
        v.distance = math.inf
        v.predesessor = None
    
def tense(edge):    
    return edge.target.distance > edge.source.distance + edge.weight
    
def relax(edge):
    edge.target.distance = edge.source.distance + edge.weight
    edge.target.predesessor = edge.source
    
def dijkstra(graph, source):
    """
    Runtime : O(E+VlogV)
    """
    init_sssp(graph, source)
    pq = Heap(min = True)
    pq.Push(source, source.distance)
    while not pq.IsEmpty():
        u, distance = pq.Extract()
        for e in u.outgoing_edges:
            if tense(e):
                relax(e)
                if pq.IsInHeap(e.target):
                    pq.UpdateKey(e.target, e.target.distance)
                else:
                    pq.Push(e.target, e.target.distance)
    
def init_graph_topological_sort():
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')
    j = Vertex('j')
    k = Vertex('k')
    l = Vertex('l')
    m = Vertex('m')
    n = Vertex('n')
    o = Vertex('o')
    p = Vertex('p')
    
    e1 = Edge((a, b))
    e2 = Edge((e, i))
    e3 = Edge((i, n))
    e4 = Edge((n, o))
    e5 = Edge((o, k))
    e6 = Edge((k, h))
    e7 = Edge((k, l))
    e8 = Edge((l, p))
    e9 = Edge((f, g))
    e10 = Edge((j, m))
    e11 = Edge((g, a))
    e12 = Edge((f, b))
    e13 = Edge((g, c))
    e14 = Edge((d, c))
    e15 = Edge((h, c))
    e16 = Edge((h, d))
    e17 = Edge((f, l))
    e18 = Edge((g, k))
    e19 = Edge((l, h))
    e20 = Edge((m, i))
    e21 = Edge((j, n))
    e22 = Edge((o, l))
    
    graph = Graph()
    vertices = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21]
    source = a
    
    init_graph(graph, vertices, edges)
    
    return graph, source
    
def topological_sort(graph, source):
    dfs(graph, source)
    graph.vertices = sorted(graph.vertices, key=lambda x:x.post, reverse=True)
       
def init_graph_bellman_ford():
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')
    v5 = Vertex('v5')
    v6 = Vertex('v6')
    v7 = Vertex('v7')

    e1 = Edge((v1, v2), weight=4)
    e2 = Edge((v1, v3), weight=10)
    e3 = Edge((v1, v4), weight=3)
    e4 = Edge((v2, v3), weight=8)
    e5 = Edge((v2, v5), weight=3)
    e6 = Edge((v3, v5), weight=-5)
    e7 = Edge((v3, v6), weight=-7)
    e8 = Edge((v4, v3), weight=6)
    e9 = Edge((v4, v6), weight=2)
    e10 = Edge((v5, v6), weight=-3)
    e11 = Edge((v5, v7), weight=1)
    e12 = Edge((v7, v6), weight=-5)
    
    graph = Graph()
    vertices = [v1, v2, v3, v4, v5, v6, v7]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]
    source = v1
    
    init_graph(graph, vertices, edges)
    
    return graph, source

def bellman_ford(graph, source):
    """
    Runtime : O(VE)
    """
    init_sssp(graph, source)
    for v in graph.vertices:
        for e in graph.edges:
            if tense(e):
                relax(e)
      
def is_negative_cycle(graph, source):
    bellman_ford(graph, source)
    for e in graph.edges:
        if tense(e):
            return True
    return False

def init_graph_kruskal():
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')
    v5 = Vertex('v5')
    v6 = Vertex('v6')
    v7 = Vertex('v7')

    e1 = Edge((v1, v2), directed=False, weight=26)
    e2 = Edge((v1, v3), directed=False, weight=14)
    e3 = Edge((v1, v4), directed=False, weight=4)
    e4 = Edge((v2, v3), directed=False, weight=30)
    e5 = Edge((v3, v4), directed=False, weight=12)
    e6 = Edge((v2, v5), directed=False, weight=16)
    e7 = Edge((v5, v3), directed=False, weight=3)
    e8 = Edge((v4, v6), directed=False, weight=18)
    e9 = Edge((v6, v3), directed=False, weight=2)
    e10 = Edge((v6, v5), directed=False, weight=10)
    e11 = Edge((v6, v7), directed=False, weight=8)
    e12 = Edge((v5, v7), directed=False, weight=5)
    
    graph = Graph()
    vertices = [v1, v2, v3, v4, v5, v6, v7]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]
    
    init_graph(graph, vertices, edges)
    
    return graph

def make_set(vertex):
    vertex.set = [vertex]

def find(vertex):
    return sorted(set(vertex.set), key=lambda x:x.name)
    
def union(u, v):
    u.set.extend(v.set)
    u.set = sorted(u.set, key=lambda x:x.name)
    for q in u.set:
        q.set = u.set
    v.set = u.set = list(set(u.set))
    
def kruskal(graph):
    """
    Joseph Kruskal in 1956
    Runtime : O(ElogV)
    """
    graph.edges = sorted(graph.edges, key=lambda x:x.weight)
    edges = []
    for v in graph.vertices:
        make_set(v)
    for e in range(int(len(graph.edges)/2)):    # undirected edges are bi-directional 
        edge = graph.edges[e*2]
        u, v = edge.source, edge.target
        if find(u) != find(v):
            union(u, v)
            edge.directed = True
            edges.append(edge)
            graph.edges[(e*2)+1].directed = True
            edges.append(graph.edges[(e*2)+1])
    mst = Graph()
    init_graph(mst, graph.vertices, edges)
    return mst
     
def min_total_weight(temp_graph, graph):
    if (int(sum([e.weight for e in temp_graph.edges])/2) < int(sum([e.weight for e in graph.edges])/2)):
        return temp_graph
    else:
        return graph
    
def second_best_minimum_spanning_tree(graph):
    mst = kruskal(graph)
    sbmst = graph
    for e in range(int(len(mst.edges)/2)):
        graph.edges.remove(mst.edges[e*2])
        graph.edges.remove(mst.edges[(e*2)+1])
        temp_graph = kruskal(graph)
        sbmst = min_total_weight(temp_graph, sbmst)
        graph.edges.append(mst.edges[e*2])
        graph.edges.append(mst.edges[(e*2)+1])
    return sbmst
        
def is_acyclic(graph):
    for v in graph.vertices:
        if v.status == 'new':
            if not is_acyclic_dfs(v):
                return False
    return True

def is_acyclic_dfs(vertex):
    vertex.status = 'active'
    for e in vertex.outgoing_edges:
        if e.target.status == 'active':
            return False
        elif e.target.status == 'new':
            if is_acyclic_dfs(e.target) == False:
                return False
    vertex.status = 'finished'
    return True
     
def init_graph_kosaraju_sharir():
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')
    j = Vertex('j')
    k = Vertex('k')
    l = Vertex('l')
    m = Vertex('m')
    n = Vertex('n')
    o = Vertex('o')
    p = Vertex('p')

    e1 = Edge((a, b))
    e2 = Edge((b, f))
    e3 = Edge((f, g))
    e4 = Edge((g, a))
    e5 = Edge((e, f))
    e6 = Edge((e, i))
    e7 = Edge((i, n))
    e8 = Edge((n, j))
    e9 = Edge((j, m))
    e10 = Edge((m, i))
    e11 = Edge((f, l))
    e12 = Edge((g, c))
    e13 = Edge((g, k))
    e14 = Edge((j, k))
    e15 = Edge((n, o))
    e16 = Edge((d, c))
    e17 = Edge((c, h))
    e18 = Edge((h, d))
    e19 = Edge((k, h))
    e20 = Edge((k, l))
    e21 = Edge((l, o))
    e22 = Edge((o, k))
    e23 = Edge((l, p))
    e24 = Edge((h, l))
    
    graph = Graph()
    vertices = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24]
    
    init_graph(graph, vertices, edges)
    
    return graph
    
def reset_vertices(vertices):
    for v in vertices:
        v.outgoing_edges = []
        v.incoming_edges = []
        v.adjacency_list = {}
    
def reverse_graph(graph):
    reversed_graph = Graph()
    vertices = [v for v in graph.vertices]
    edges = [Edge((e.target, e.source)) for e in graph.edges]
    init_graph(reversed_graph, vertices, edges)
    return reversed_graph
     
def sink_component(graph): 
    random_vertex = random.choice(graph.vertices)
    topological_sort(graph, random_vertex)
    sink_vertex = graph.vertices[0]
    return sink_vertex
    
def mark(vertex):
    vertex.unmarked = False
    
def reach(vertex, reach_list):
    if vertex.unmarked:
        mark(vertex)
        for e in vertex.outgoing_edges:
            reach_list.append(e.target)
            reach(e.target, reach_list)
    return list(set(reach_list))
     
def label_one_dfs(vertex, root):
    vertex.root = root
    for e in vertex.outgoing_edges:
        if e.target.root == None:
            label_one_dfs(e.target, root)
     
def post_order_in_reversed_graph(graph):
    graph = reverse_graph(graph)
    random_vertex = random.choice(graph.vertices)
    topological_sort(graph, random_vertex)
    post_order = [v for v in graph.vertices]
    graph = reverse_graph(graph)
    return post_order
     
def kosaraju_sharir(graph):
    """
    Strong Connected Components
    Runtime : O(V+E)
    """
    post_order = post_order_in_reversed_graph(graph)
    while post_order != []:
        vertex = post_order.pop(0)
        if vertex.root == None:
            label_one_dfs(vertex, vertex)
            
if __name__ == "__main__":
    
    ## BFS test case
    graph, source = init_graph_bfs()
    bfs(graph, source)
    print({v.name:[v.value, v.color] for v in graph.vertices})
    
    ## DFS test case
    graph, source = init_graph_dfs()
    dfs(graph, source)
    print({v.name:[v.pre, v.post, v.color] for v in graph.vertices})
    
    ## Dijkstra test case
    graph, source = init_graph_dijkstra()
    dijkstra(graph, source)
    print({v.name:[v.distance, v.predesessor.name] for v in graph.vertices if v.predesessor is not None})
    
    ## Topological sort test case
    graph, source = init_graph_topological_sort()
    topological_sort(graph, source)
    print([v.name for v in graph.vertices])
    
    ## Bellman-Ford test case
    graph, source = init_graph_bellman_ford()
    bellman_ford(graph, source)
    print({v.name:[v.distance, v.predesessor.name] for v in graph.vertices if v.predesessor is not None})
    
    ## Kruskal test case
    graph = init_graph_kruskal()
    mst = kruskal(graph)
    print([(e.name, e.weight) for e in mst.edges])
    
    ## Second best minimum spanning tree
    graph = init_graph_kruskal()
    sbmst = second_best_minimum_spanning_tree(graph)
    print('total weight of mst : ' + str(int(sum([e.weight for e in mst.edges])/2)) + '\n' + str([(e.name, e.weight) for e in mst.edges]) + '\ntotal weight of sbmst : ' + str(int(sum([e.weight for e in sbmst.edges])/2)) + '\n' + str([(e.name, e.weight) for e in sbmst.edges]))
   
    ## Acyclic graph test case
    graph, source = init_graph_dfs()
    print(is_acyclic(graph))
    graph, source = init_graph_topological_sort()
    print(is_acyclic(graph))
    
    ## Strong components case
    graph = init_graph_kosaraju_sharir()
    kosaraju_sharir(graph)
    print([(v.name, v.root.name) for v in sorted(graph.vertices, key=lambda x:x.root.name)])
    
