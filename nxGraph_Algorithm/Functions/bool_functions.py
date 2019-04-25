from global_properties import V
from local_properties import neighbors

def is_independent (G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) !=[]:
            return False
    return True

def is_dominating(G, S):
    S_complement = list(set(V(G))-set(S))
    for v in S_complement:
        N = neighbors(G, v)
        if list(set(N) & set(S)) == []:
            return False
    return True

def is_clique (G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) !=[]:
            return False
    return True

def is_matching(G, m):
    for edge1 in m:
        v, w = edge1
        for edge2 in m:
            if edge2 != edge1:
                if v in edge1 or w in edge1:
                    return False
    return True 
