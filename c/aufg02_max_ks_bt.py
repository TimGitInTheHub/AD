
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks
from AD.src.ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks, ausrechnen

# vereinfachtes Backtracking-Kriterium:
#   Teilloesung noch zulaessig?
def K_max_ks(s,v,S,t):
    while(len(t)<len(s)):
        t = t + (0, )
    return sol_max_ks(s, v, S, t)

# Entwurfsmuster Backtracking
def max_ks_backtracking(s,v,S):
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
                    if K_max_ks(s, v, S, t):
                        M.add(t)
                    else:
                        pass
    return opt
                    
        
    
    


# Bsp m=4, S=7
print(max_ks_backtracking([3,2,1,5],[3,1,1,4],7))
print(max_ks_backtracking([3,8,1,5],[3,1,1,4],8))
