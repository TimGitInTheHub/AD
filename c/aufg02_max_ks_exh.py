# MAX KNAPSACK

# zulaessige Loesung, auch fuer Teilloesungen
def sol_max_ks(s,v,S,t): 
    return ausrechnen(s, t) <= S#m

# Bewertungsfunktion, auch fuer Teilloesungen
def m_max_ks(s,v,S,t):          
    return ausrechnen(v, t) #m

# Entwurfsmuster Exhaustive Search
from itertools import product
def max_ks_exhaustive(s,v,S):            
    m=len(s)            #1
    opt = -1            #1
    for t in product(range(2),repeat=m):    #2^m
        if(sol_max_ks(s, v, S, t)): #m
            opt = max(opt, m_max_ks(s, v, S, t))#m
    return opt#1
        
def ausrechnen(liste,t): 
    wert=0  #1
    for i in range(len(t)):#O(m)
        if(t[i]==1):    
            wert+=liste[i]
    return wert

# Bsp m=4, S=7
print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],7))
print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],8))





