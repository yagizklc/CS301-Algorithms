def main():

    # input M, W
    M = {
        "m1":[["w3", "w2", "w1"], False],
        "m2":[["w2", "w3", "w1"], False],
        "m3":[["w3", "w2", "w1"], False],
    }
    W = {
        "w1":[["m3", "m1", "m2"], False],
        "w2":[["m3", "m1", "m2"], False],
        "w3":[["m3", "m2", "m1"], False],
    }

    stableMariage(M, W)
    Print(W)

if __name__ == "__main__":
    main()

# ----Helper Functions---- #

def freeCandidate(M: dict):
    for man, prefList in M.items():
        if prefList[1] == False:
            return man    
    return False

def preferredWife(M: dict, m: str):
    w = M[m][0][0]
    M[m][0].remove(w)
    return w

def hasHusband(W:dict, w: str):
    return W[w][1]

def betterHusband(W:dict, w:str, m: str, m_p: str) -> bool:
    if W[w][0].index(m) < W[w][0].index(m_p):
        return True
    return False
    
def divorce(W:dict, M:dict, w:str, m_p:str):
    W[w][1] = False
    M[m_p][1] = False

def marry(W:dict, M:dict, w:str, m:str):
    W[w][1] = m
    M[m][1] = w

def Print(W:dict):
    for w, prefList in W.items():
        print(w, prefList[1])

def stableMariage(M: dict, W: dict):
    """
    input: preference list of men and women as dicts 
    output: pairs of (m, w) that are stable, 
        i.e no man and woman from different pairs prefer each other over their current match
    """
    

    m = freeCandidate(M)
    while m: # there exists a free man m with a woman w to propose to
        w = preferredWife(M, m) 
        m_p = hasHusband(W, w)
        if m_p: # w has a husband
            if betterHusband(W, w, m, m_p):
                divorce(W, M, w, m_p)
                marry(W, M, w, m)
        else:
            marry(W, M, w, m)

        m = freeCandidate(M)



