
# l-CLUSTERING
from ueb.d.aufg07_kruskal import kruskal
from ueb.b.aufg12_comp import comp

def cluster(m,d,l):
    # 1. vollstaendigen Graph mit m Knoten, m^2 Kanten und Kosten d[u,v] konstruieren
    #
    # 2. Alg. kruskal unveraendert aufrufen
    #
    # 3. die l-1 teuersten Kanten löschen
    #
    # 4. Zush.komponenten bestimmen,  via B.12 (comp)
    # dazu Graph mit allen Knoten konstuieren und Kanten einf.
    #
    return []


# Distanzfunktion symmetrisch, Diag. 0
def define_d():
    d = {}
    d[0,0]= 0
    d[0,1]= 11
    d[0,2]= 7
    d[0,3]= 15
    d[0,4]= 8
    d[1,0]= 11
    d[1,1]= 0
    d[1,2]= 12
    d[1,3]= 9
    d[1,4]= 2
    d[2,0]= 7
    d[2,1]= 12
    d[2,2]= 0
    d[2,3]= 13
    d[2,4]= 14
    d[3,0]= 15
    d[3,1]= 9
    d[3,2]= 13
    d[3,3]= 0
    d[3,4]= 6
    d[4,0]= 8
    d[4,1]= 2
    d[4,2]= 14
    d[4,3]= 6
    d[4,4]= 0
    return d

d = define_d()
m = 5
for l in range(1,6):
    print(cluster(m,d,l))




