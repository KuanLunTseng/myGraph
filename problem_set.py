from algorithm import *
from copy import deepcopy as cpy 
from graph_class import *
from heap import *
from pysmt import *
from mfriend import *

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
    
def init_graph_divide_by_three():
    s = Vertex('s')
    w = Vertex('w')
    t = Vertex('t')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')
    
    e1 = Edge((s, w))
    e2 = Edge((w, t))
    e3 = Edge((w, y))
    e4 = Edge((z, t))
    e5 = Edge((y, z))
    e6 = Edge((y, x))
    e7 = Edge((x, s))
    
    graph = Graph()
    vertices = [s, w, t, x, y, z]
    edges = [e1, e2, e3, e4, e5, e6, e7]
    
    init_graph(graph, vertices, edges)
    source = s
    target = t
    
    return graph, source, target
    
def init_graph_number_distinct_dfs_tree():
    x1 = Vertex('x1')
    x2 = Vertex('x2')
    x3 = Vertex('x3')
    x4 = Vertex('x4')
    x5 = Vertex('x5')
    x6 = Vertex('x6')
    
    t1 = Vertex('t1')
    t2 = Vertex('t2')
    t3 = Vertex('t3')
    t4 = Vertex('t4')
    t5 = Vertex('t5')
   
    b1 = Vertex('b1')
    b2 = Vertex('b2')
    b3 = Vertex('b3')
    b4 = Vertex('b4')
    b5 = Vertex('b5')
    
    e1 = Edge((x1, t1))
    e2 = Edge((x1, b1))
    e3 = Edge((t1, x2))
    e4 = Edge((b1, x2))
    
    e5 = Edge((x2, t2))
    e6 = Edge((x2, b2))
    e7 = Edge((t2, x3))
    e8 = Edge((b2, x3))
      
    e9 = Edge((x3, t3))
    e10 = Edge((x3, b3))
    e11 = Edge((t3, x4))
    e12 = Edge((b3, x4))
    
    e13 = Edge((x4, t4))
    e14 = Edge((x4, b4))
    e15 = Edge((t4, x5))
    e16 = Edge((b4, x5))
      
    e17 = Edge((x5, t5))
    e18 = Edge((x5, b5))
    e19 = Edge((t5, x6))
    e20 = Edge((b5, x6))
    
    graph = Graph()
    vertices = [x1, x2, x3, x4, x5, x6, t1, t2, t3, t4, t5, b1, b2, b3, b4, b5]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]
    root = x1
    dest = x6
    init_graph(graph, vertices, edges)
    
    return graph, root, dest
    
def init_graph_number_distinct_dfs_tree_easy():
    x1 = Vertex('x1')
    x2 = Vertex('x2')
    x3 = Vertex('x3')
    x4 = Vertex('x4')
    
    t1 = Vertex('t1')
    t2 = Vertex('t2')
    t3 = Vertex('t3')
   
    b1 = Vertex('b1')
    b2 = Vertex('b2')
    b3 = Vertex('b3')
    
    e1 = Edge((x1, t1))
    e2 = Edge((x1, b1))
    e3 = Edge((t1, x2))
    e4 = Edge((b1, x2))
    
    e5 = Edge((x2, t2))
    e6 = Edge((x2, b2))
    e7 = Edge((t2, x3))
    e8 = Edge((b2, x3))
    
    e9 = Edge((x3, t3))
    e10 = Edge((x3, b3))
    e11 = Edge((t3, x4))
    e12 = Edge((b3, x4))
      
    
    graph = Graph()
    vertices = [x1, x2, x3, t1, t2, t3, b1, b2, b3]
    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]
    root = x1
    dest = x4
    init_graph(graph, vertices, edges)
    
    return graph, root, dest
    
def init_graph_number_distinct_dfs_tree_basic():
    x1 = Vertex('x1')
    x2 = Vertex('x2')
    
    t1 = Vertex('t1')
   
    b1 = Vertex('b1')
    
    e1 = Edge((x1, t1))
    e2 = Edge((x1, b1))
    e3 = Edge((t1, x2))
    e4 = Edge((b1, x2))
    
    graph = Graph()
    vertices = [x1, x2, t1, b1]
    edges = [e1, e2, e3, e4]
    root = x1
    dest = x2
    init_graph(graph, vertices, edges)
    
    return graph, root, dest
    
def init_graph_dfs_shortest_length():

    s = Vertex('s')
    b = Vertex('b')
    c = Vertex('c')
    t = Vertex('t')
    
    e1 = Edge((s, b), weight=4)
    e2 = Edge((s, c), weight=17)
    e3 = Edge((b, t), weight=2)
    e4 = Edge((c, t), weight=1)
    
    
    graph = Graph()
    vertices = [s, b, c, t]
    edges = [e1, e2, e3, e4]
    source = s
    target = t
    
    init_graph(graph, vertices, edges)
    
    return graph, source, target
    
def init_graph_johnson():
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')
    
    e1 = Edge((w, z), weight=2)
    e2 = Edge((z, x), weight=-7)
    e3 = Edge((x, w), weight=6)
    e4 = Edge((x, y), weight=3)
    e5 = Edge((y, z), weight=5)
    e6 = Edge((z, y), weight=-3)
    e7 = Edge((y, w), weight=4)
    
    graph = Graph()
    vertices = [w, x, y, z]
    edges = [e1, e2, e3, e4, e5, e6, e7]
    
    init_graph(graph, vertices, edges)
    
    return graph
    
def init_graph_toy_clique_problem():
  
    name = 'abcdef'
    vertices = [Vertex(n) for n in name]
    
    e1 = Edge((vertices[0], vertices[1]), directed=False)
    e2 = Edge((vertices[1], vertices[2]), directed=False)
    e3 = Edge((vertices[2], vertices[3]), directed=False)
    e4 = Edge((vertices[3], vertices[0]), directed=False)
    e5 = Edge((vertices[0], vertices[4]), directed=False)
    e6 = Edge((vertices[4], vertices[5]), directed=False)
    e7 = Edge((vertices[5], vertices[0]), directed=False)
    
    graph = Graph()
    
    edges = [e1, e2, e3, e4, e5, e6, e7]
    
    init_graph(graph, vertices, edges)
    
    return graph
    
def init_graph_mfriend(k):
    
    jfile = mfriend(k)
    vertices = [Vertex(j.name) for j in jfile]
    
    edges = []
    
    for j in jfile:
        for u in vertices:
            if j.name == u.name:
                for f in j.friend_list:
                    for v in vertices:
                        if v.name == f:
                            uv = Edge((u, v), directed=False)
                            edges.append(uv)
                            for e in edges:
                                if (uv.source.name, uv.target.name) == (e.source.name, e.target.name) or (uv.target.name, uv.source.name) == (e.source.name, e.target.name):
                                    pass
                                    
    
    graph = Graph()
    init_graph(graph, vertices, edges)
        
    return graph