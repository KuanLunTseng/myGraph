class Graph(object):
    
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.graph_dict = dict
        self.vertices = []
        self.edge = []
        
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            self.vertices.append(vertex.name)

    def add_edge(self, edge):
        
        if edge.src and edge.dst in self.graph_dict:
            self.graph_dict[v1].append(v2)

    def V(self):
        return list(self.graph_dict.keys())
        
    def __str__(self):
        res = "vertices: "
        for v in self.graph_dict:
            res += v.name + " "
        res += "\nedges: "
        
        return res
        
class Vertex:
    def __init__(self, name, mark = False, value = 0):
        self.name = name
        self.mark = mark
        self.value = value

class Edge:
    def __init__(self, edge, weight = 1, directed = True):
        v1, v2 = edge
        self.src = v1
        self.dst = v2
        self.name = (self.src.name, self.dst.name)
        self.weight = weight

if __name__ == "__main__":
    
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    graph = Graph()
    
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    
    e = (v1, v2)
    
    e1 = Edge(e)
    
    graph.add_edge(e1)
   
    
    print(graph.__str__())
    
