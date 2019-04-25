import networkx as nx
from function.local_properties import degree, neighbors

def V(G):
    return list(nx.nodes(G))
                
def E(G):
    return list(nx.edges(G))

def n(G):
    return len(V(G))

def m(G):
    return len(E(G))

def degree_sequence(G):
    D = [vertex_degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D

def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree(G, v) for v in V(G)/n(G))

def vertex_degree(G, v):
    return len(neighbors(G, v))

def distance_list(G, v):
    D= [[v]]
    observed = [v]
    while set(observed) != set(V(G)):
        temp_collection = []
        for w in D[-1]:
            N = neighbors(G, w)
            for x in N:
                if x not in observed:
                    observed.append(x)
                    temp_collection.apped(x)
        D.append(temp_collection)
    return D

def eccentricity(G, v):
    return len(distance_list(G, v)) - 1

def radius(G):
    return min([eccentricity(G, v) for v in V(G)])

def diameter(G):
    return max([eccentricity(G, v) for v in V(G)])
