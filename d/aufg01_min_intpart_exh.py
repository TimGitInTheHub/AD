from pkg_resources._vendor.more_itertools.more import permutation_index
import itertools

# MINIMUM INTERVAL PARTITIONING

# ist Intervallmenge M kompatibel?
def compatible(L,M):
    for i in M:
        for j in M:           
            if(i!=j):                  #Vergleiche jeden Knoten in der Menge
                if ( L[i][0]>=L[j][1] or L[j][0]>=L[i][1]): #Uberschneiden sich 2 Intervale, gebe False aus
                    pass
                else:
                    return False
    return True

# Bsp
L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
L_1 = [(0,2),(1,3),(0,3),(2,4)]
#print(compatible(L,{0,2,5}))
#print(compatible(L,{0,3,4,7}))
#print(compatible(L,{1,2}))
print(compatible(L_1,{1,2,3,4}))
#print(compatible(L,set()))


# zulaessige Loesung:
# - r ist stets total
# - jede Intervallmenge pro Ressource ist kompatibel
def sol_min_intpart(L,r):
    # todo
    return True

# Bewertungsfunktion:
# - Kardinalitaet Wertebereich von r
def m_min_intpart(L,r):
    # todo
    return 0

# Entwurfsmuster Exhaustive Search
from itertools import product
def min_intpart_exhaustive(L):
    m = len(L)
    opt = m
    for myProducts in product(range(m), repeat=m):
        myRessources = [set() for _ in range(m)]
        for i in range(m):
            myRessources[myProducts[i]].add(i)
        #print('myRessources', myRessources)
        not_comp = False
        for kandidat in myRessources:
            #print('mein Kandidat:', kandidat)
            if not compatible(L, kandidat):
                not_comp = True
                
        if not_comp:
            continue
        min(opt, len(list(filter(None, myRessources))))
    return opt                  


print(min_intpart_exhaustive([(0,2),(1,3),(0,3),(2,4)]))
print(min_intpart_exhaustive([(0,2),(0,3),(2,3),(3,4)]))
print(min_intpart_exhaustive([(0,2),(0,3)]))



