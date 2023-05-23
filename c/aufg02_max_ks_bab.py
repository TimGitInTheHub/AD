
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks, K_max_ks 
from AD.src.ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks
from AD.src.ueb.c.aufg02_max_ks_bt import K_max_ks


# obere Schranke:
# Bewertung der Teilloesung t + Werte aller restlichen Gegenstaende
def o_max_ks(s,v,S,t,opt):
    erlaubt = K_max_ks(s, v, S, t)
    while(len(t)<len(s)):
        t = t + (1, )
    effizient = opt < m_max_ks(s,v,S,t)
    return erlaubt and effizient

# Entwurfsmuster Branch and Bound
def max_ks_bab(s,v,S):
    opt = -1
    m=len(s)
    M={()}
    while M:
        t_prev = M.pop()
        for a in range(m):
            for auswahl in range(2):
                t = t_prev + (auswahl, )
                if len(t) == m:
                    if sol_max_ks(s,v,S,t):
                        opt = max(opt, m_max_ks(s, v, S, t))
                else:
                    if o_max_ks(s, v, S, t,opt):
                        M.add(t)
                    else:
                        pass
    return opt


# Bsp m=4, S=7
print(max_ks_bab([3,2,1,5],[3,1,1,4],7))
print(max_ks_bab([3,8,1,5],[3,1,1,4],8))
