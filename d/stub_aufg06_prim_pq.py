
# MINIMUM SPANNING TREE

# Verbesserung von prim mittels MinPrioQueue
from heapq import heappush, heappop

def prim_pq(G):
    # todo
    return set(), 0
  

# Bsp aus der VL
def define_G():
    G = [   {1:4, 2:1, 3:3}, 
            {0:4, 2:4, 3:4}, 
            {0:1, 1:4, 3:2, 5:4},
            {0:3, 1:4, 2:2, 5:6},  
            {5:5},  
            {2:4, 3:6, 4:5}  
        ]
    return G

G = define_G()
print(prim_pq(G))
