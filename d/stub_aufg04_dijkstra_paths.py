
# (SINGLE-SOURCE) SHORTEST PATH

# Ergaenzung von dijkstra um Pfade

def dijkstra_paths(G,s):
    # todo
    return [], []


# s-v-Pfad bestimmen
def shortest_path(s,v,p):
    # todo
    return []


# Bsp aus der VL
# Knotennummern: s=0, u=1, x=2, y=3, v=4, z=5
def define_G():
    G = [   {1:1, 4:4, 2:2},   # Nachfolger von s
            {3:3, 4:1},        # von u
            {4:2, 5:3},        # von x
            {},                # von y
            {3:1, 5:2},        # von v
            {}                 # von z
        ]
    return G

G = define_G()
d,p = dijkstra_paths(G,0)

print(shortest_path(0,3,p))
print(shortest_path(0,0,p))

