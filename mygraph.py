class Graph(object):
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.graph_dict = dict
        
    def add_vertex(self, object):
        if object not in self.graph_dict:
            self.graph_dict[object] = []
            self.weight = object.value
        
    '''
    def vertices(self):
        return list(self.graph_dict.keys())
    
    def __str__(self):
        res = "vertices: "
        #for k in self.__graph_dict
    '''
        
class Vertex(object):
    def __init__(self, dict):
        self.mark = False
        self.value = 0
        self.predecessors = []
        self.children = []
        if dict == None:
            vertex_dict = {}
        self.vertex_dict = dict

#class EDGE(object):
    #def __init__(self, src, dst, weight=1, directed=True):
        
        
if __name__ == "__main__":

    attributes = {"weight":1, "mark":True}
    predecessors = {"v2", "v3"}
    
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list1.append(list2)
    print(list2)
    
    v1 = Vertex(predecessors)
    graph = Graph()
    print("\nvertex_dict:")
    print(v1.vertex_dict)\
    
    graph.add_vertex(v1)
    #graph.add_vertex("v4")
    print("\ngraph_dict:")
    print(graph.graph_dict)
   

