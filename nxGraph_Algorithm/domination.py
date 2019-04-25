from itertools import combinations
from functions.bool_functions import is_dominating
from functions.global_properties import V, n



def minimum_dominating(G):
    for k in range(1, n(G)):
        for S in combinations(V(G), k):
            if is_dominating(G, list(S)) == True:
                return list(S)
            
def domination_number(G):
    return len(minimum_dominating(G))
