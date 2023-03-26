from table import * 

# iter farm
def iter_farm(farm: Farm):

    # get dimensions of farm 
    n, m = farm.n, farm.m
    
    # initialize c to be all None
    c = []
    for i in range(n):
        c.append([])
        for j in range(m):
            c[i].append(None)
    
    # initialize W to be all 0, except weedy cells
    W = []
    for i in range(n):
        W.append([])
        for j in range(m):
            W[i].append(0)    

    for cell in farm.weeds:
        W[cell[0]][cell[1]] = 1
    
    # Bottom-up Iterative approach. Base: (0, 0), Target: (n-1, m-1)
    for i in range(n): # from i = 0 to n-1
        for j in range(m): # from j = 0 to m-1
            if (i == 0) and (j == 0): # at (0, 0)
                c[i][j] = W[i][j] 
            elif (i == 0): # at first row, other than (0, 0)
                c[i][j] = c[i][j-1] + W[i][j] # left cell + w
            elif (j == 0): # at first column, other than (0, 0)
                c[i][j] = c[i-1][j] + W[i][j] # above cell + w
            else: # max(left, above) + w
                c[i][j] = max(c[i][j-1], c[i-1][j]) + W[i][j]
            
    return c

# backpropagate to find the path    
def backpropagate(c: list):
    n, m = len(c), len(c[0])
    i, j = n-1, m-1

    # starting from right-bottom
    # add the max value cell to path
    path = [(i, j)] 
    while not (i == 0 and j == 0): # while not reached start
        if i == 0: # if at the bottom, go left
            j = j - 1 
        elif j == 0:
            i = i - 1 # if at the most left, go up
        else: # if at somewhere else
            if c[i-1][j] > c[i][j-1]: # if above > left
                i = i - 1 # go up
            else: # if left > above
                j = j - 1 # go left
        
        path.append((i, j))

    # since the path is constructed from end to start
    # return the reversed version: start to end
    return path[::-1]

# solution path
def solve(farm: Farm):
    return backpropagate(iter_farm(farm)) 
