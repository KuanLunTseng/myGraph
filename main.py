from algorithm import *
from graph_class import *
from heap import *
from memory_profiler import *
from problem_set import *
import sys
import time


def dory_dfs(vertex):
    global call
    call+=1
    #print(vertex.name)
    for e in vertex.outgoing_edges:
        dory_dfs(e.target)

if __name__ == "__main__":
    
    graph = init_graph_johnson()
    dict = johnson(graph)
    #print(dict)
    #print([(e.source.name, e.target.name, e.weight) for e in graph.edges])
    
    graph, root, dest = init_graph_number_distinct_dfs_tree_basic()
    call = 0
    dory_dfs(root)
    #print(call)
    
    ## BFS test case
    graph, source = init_graph_bfs()
    bfs(graph, source)
    #print({v.name:[v.value, v.color] for v in graph.vertices})
    #print([(v.name, v.predesessor.name) for v in graph.vertices if v.predesessor != None])
    
    ## DFS test case
    graph, source = init_graph_dfs()
    dfs(graph, source)
    #print({v.name:[v.pre, v.post, v.color] for v in graph.vertices})
    
    ## Dijkstra test case
    graph, source = init_graph_dijkstra()
    dijkstra(graph, source)
    #print({v.name:[v.distance, v.predesessor.name] for v in graph.vertices if v.predesessor is not None})
    
    ## Topological sort test case
    graph, source = init_graph_topological_sort()
    topological_sort(graph, source)
    #print([v.name for v in graph.vertices])
    
    ## Bellman-Ford test case
    graph, source = init_graph_bellman_ford()
    bellman_ford(graph, source)
    #print({v.name:[v.distance, v.predesessor.name] for v in graph.vertices if v.predesessor is not None})
    
    ## Kruskal test case
    graph = init_graph_kruskal()
    mst = kruskal(graph)
    #print([(e.name, e.weight) for e in mst.edges])
    
    ## Second best minimum spanning tree
    graph = init_graph_kruskal()
    sbmst = second_best_minimum_spanning_tree(graph)
    #print('total weight of mst : ' + str(int(sum([e.weight for e in mst.edges])/2)) + '\n' + str([(e.name, e.weight) for e in mst.edges]) + '\ntotal weight of sbmst : ' + str(int(sum([e.weight for e in sbmst.edges])/2)) + '\n' + str([(e.name, e.weight) for e in sbmst.edges]))
   
    ## Acyclic graph test case
    graph, source = init_graph_dfs()
    #print(is_acyclic(graph))
    graph, source = init_graph_topological_sort()
    #print(is_acyclic(graph))
    
    ## Strong components test case
    graph = init_graph_kosaraju_sharir()
    kosaraju_sharir(graph)
    #print([(v.name, v.root.name) for v in sorted(graph.vertices, key=lambda x:x.root.name)])
    
    ## Divide by three test case(not sure it is right or not
    graph, source, target = init_graph_divide_by_three()
    #print(divide_by_three(graph, source, target))
    
    ## Number of distinct dfs tree case
    graph, root, dest = init_graph_number_distinct_dfs_tree()
    num = number_diff_dfs_tree(graph, root, dest)
    #print(num)
    
    ## DFS shortest length test
    graph, source, target = init_graph_dfs_shortest_length()
    #print(dfs_shortest_length(graph, source, target, 0))
    
    ## k-clique reduction test case
    # Example case
    if sys.argv[1] == '-e':
        graph = init_graph_toy_clique_problem()
        print(graph)
        print('')
        k, brute_ans = brutal_kclique(graph)
        print(brute_ans)
        print('')
        sat_ans, clause = clique_to_sat(graph, k)    
        print(sat_ans)
        print('number of clauses in SAT solver: %d' % (clause))
        
    ## json file transform to a graph test case
    
    # Analysis mode
    if sys.argv[1] == '-a':
        for i in range(1, 100):
            #mem_usage = memory_usage(-1, interval=.2, timeout=1)
            graph = init_graph_mfriend(i)
            
            output = open('output.txt', 'a') 
            
            brute_time = time.time()
            k, brute_ans = brutal_kclique(graph)
            brute_cost = time.time() - brute_time
            
            sat_time = time.time()
            sat_ans, clause = clique_to_sat(graph, k)
            sat_cost = time.time() - sat_time
            
            
            output.write("%s,%s,%s,%s\n" % (i, brute_cost, sat_cost, clause))
        