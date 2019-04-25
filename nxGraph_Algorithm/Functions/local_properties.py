import networkx as nx

def neighbors(G,v):
    return list(nx.neighbors(G,v))

def degree(G, v):
    return len(neighbors(G, v))
