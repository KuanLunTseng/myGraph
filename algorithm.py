from graph_class import *
from heap import *
from problem_set import *
import math
import random

def bfs(graph, source):
    source.value = 0
    queue = [source]
    while queue:
        u = queue.pop(0)
        for v in graph.adjacency_list[u]:
            if v.color == 'white':
                v.color = 'grey'
                v.value = u.value + 1
                v.predesessor = u
                queue.append(v)
            if v.color == 'black':
                v.predesessor = u
        u.color = 'black'

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

def topological_sort(graph, source):
    dfs(graph, source)
    graph.vertices = sorted(graph.vertices, key=lambda x:x.post, reverse=True)

def bellman_ford(graph, source):
    """
    Runtime : O(VE)
    """
    init_sssp(graph, source)
    for i in range(len(graph.vertices) - 1):
        for e in graph.edges:
            if tense(e):
                relax(e)

def is_negative_cycle(graph, source):
    bellman_ford(graph, source)
    for e in graph.edges:
        if tense(e):
            return True
    return False
    
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

def check(graph, source, target):
    reset_vertices(graph.vertices)
    bfs(graph, source)
    return target.value % 3 == 0

def divide_by_three(graph, source, target):
    if check(graph, source, target):
        return True
    else:
        source.unmarked = False
        if source.predesessor != None:
            vertex = source.predesessor
            if vertex.unmarked:
                return divide_by_three(graph, vertex, target)
    return False

## Constructing...
'''
def init_modified_bfs(graph):
 
 
def modified_bfs(graph, source, target, distance):
    init_modified_bfs(graph)
       
def num_shortest_path(graph, source, target):
    dijkstra(graph, source)
    distance = target.distance
    reverse_graph(graph)
    count = modified_bfs(graph, source, target, distance)
    reverse_graph(graph)
    return count
'''

## Constructing...
def k_walk():
    if k == 0:
        return False

def number_diff_dfs_tree(graph, root, dest):
    """
    Modified version of BFS search
    """
    root.count = 1
    queue = [root]
    while queue:
        u = queue.pop(0)
        for v in graph.adjacency_list[u]:
            if v.count == 0:
                v.count = u.count
                queue.append(v)
            elif v.count != 0:
                v.count += u.count
    return dest.count

## Constructing...
def johnson(graph):
    
    # Add an artificial source
    s = Vertex('s')
    graph.add_vertex(s)
    
    #for v in graph.vertices:
    #    graph.add_edge(Edge((s, v), weight=0))
    for e in [Edge((s, v), weight=0) for v in graph.vertices]:
        graph.add_edge(e)
        
    # Compute vertex prices
    dist = {}
    bellman_ford(graph, s)
    for v in graph.vertices:
        dist[s, v] = v.distance
        print(dist)
    #if is_negative_cycle:
    #    return
    print(dist)
    # Reweight the edges
    for e in graph.edges:
        u = e.source
        v = e.target
        e.weight = dist[s, u] + e.weight - dist[s, v]
    
    # Compute reweighted shortest path distances
    dist_dijkstra = {}
    for u in graph.vertices:
        dijkstra(graph, u)
        for v in graph.vertices: 
            dist_dijkstra[u, v] = v.distance
        
    # Compute original shortest-path distances
    for u in graph.vertices:
        for v in graph.vertices:
            dist[u, v] = dist_dijkstra[u, v] - dist[s, u] + dist[s, v]
    return dist
        
## Constructing...
def floyd_warshall(graph):
    for u in graph.vertices:
        for v in graph.vertices:
            dist[u][v] = 0
            
def dfs_shortest_length(graph, source, target, weight):
    """
    Works only in a graph in topological order
    """
    if source == target:
        return weight
    return min([dfs_shortest_length(graph, e.target, target, weight + e.weight) for e in source.outgoing_edges])




