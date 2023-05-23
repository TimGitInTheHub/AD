
# Min TSP

# verwendet m_min_tsp
from ueb.c.aufg03_min_tsp_exh import m_min_tsp

# untere Schranke:
#  Kosten der Teilstrecke p ohne Rueckweg
def u_min_tsp(D,p):
    # todo
    return 0

# Entwurfsmuster Branch and Bound
def min_tsp_bab(D):
    # todo
    return 0


print(min_tsp_bab([[0,1,1],[1,0,1],[1,1,0]]))
print(min_tsp_bab([[0,13,2],[7,0,2],[3,8,0]]))
print(min_tsp_bab([[0,13,2],[7,0,2],[1,8,0]]))

