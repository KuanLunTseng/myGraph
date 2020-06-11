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
                edge.source.neighbors.append(edge.target)
                edge.target.neighbors.append(edge.source)
            if not edge.directed:
                edge.directed = True
                second_edge = Edge((edge.target, edge.source), weight=edge.weight)
                self.adjacency_list[edge.source].append(edge.target)
                self.adjacency_list[edge.target].append(edge.source)
                self.edges.append(edge)
                self.edges.append(second_edge)
                edge.source.outgoing_edges.append(edge)
                edge.target.incoming_edges.append(edge)
                edge.target.outgoing_edges.append(second_edge)
                edge.source.incoming_edges.append(second_edge)
                edge.target.neighbors.append(edge.source)
                edge.target.neighbors = list(set(edge.target.neighbors))
                edge.source.neighbors.append(edge.target)
                edge.source.neighbors = list(set(edge.source.neighbors))
                
    def __str__(self):
        return '\nVertices :\n%s\n\nEdges :\n%s' %(str([v.name for v in self.vertices]), str([e.name for e in self.edges]))    

class Vertex:
    def __init__(self, name, mark=False, value=0, label=0, predesessor=None, distance=0, status='new', unmarked=True, negation=False):
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
        self.count = 0
        self.negation = negation
        self.boolean = 0

class Edge:
    def __init__(self, edge, weight=1, directed=True):
        vertex_1, vertex_2 = edge
        self.source = vertex_1
        self.target = vertex_2
        self.name = (self.source.name, self.target.name)
        self.weight = weight
        self.directed = directed
        
def reset_vertices(vertices):
    for v in vertices:
        v.outgoing_edges = []
        v.incoming_edges = []
        v.adjacency_list = {}
        v.color = 'white'

def init_graph(graph, vertices, edges):
    reset_vertices(vertices)
    for v in vertices:
        graph.add_vertex(v)
    for e in edges:
        graph.add_edge(e)
        