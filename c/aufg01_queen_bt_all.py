
# sol_queen und K_queen vorher deklarieren
from AD.src.vl.lek04.queen_exh import sol_queen
from AD.src.vl.lek04.queen_bt import K_queen


def queen_backtracking_all(m):
    T = set()
    M = {()}
    while M:
        t_prev = M.pop()
        for a in range(m):          # bei QUEEN ist k=m
            t = t_prev + (a,)       # neues Tupel
            if len(t) == m:
                if sol_queen(m,t): 
                    T.add(t)
            else:
                if K_queen(m,t):
                    M.add(t)
                else:
                    pass
    return T 

queen_backtracking_all(3)
queen_backtracking_all(4)
queen_backtracking_all(5)

for m in range(2,12):
    T = queen_backtracking_all(m)
    print('m =',m, '#T =', len(T))