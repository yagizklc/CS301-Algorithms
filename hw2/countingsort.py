
# A = [4, 2, 7, 5, 3, 6, 1, 4, 6, 10, 3, 2, 3, 7, 5]
#A = [329, 457, 657, 839, 436, 720, 355]


def countingsort(A: list, digit: int):
    # k = max(A) use this for only countingsort
    n = len(A) # 5

    # init B to empty list of size n
    B = [None] * n

    # init C to all 0, size = 26 since 26 based for each char
    C = [0] * 26

    # for all i, C[A[i]-1] += 1 
    for i in range(n):
        """
        index = A[i] // digit
        index = index % 26
        """
        
        index = A[i][digit] % 26
        #print("A[i]:", A[i])
        #print("index:", index)
        
        C[index] += 1
    print("Reading from A to C:", C)
    
    # for all i, C[A[i]] = sum of all #'s SEQ than it
    for i in range(1, 26):
        C[i] += C[i-1]
    print("Compound C:", C)
    #print("C:", C)
    
    # place A[i] to B wrt their occurance # in C (stable sort)

    for i in range(n-1, -1, -1):
        """
        index = A[i] // digit
        index = index % 10
        """
        #
        #print("i:", i)
        index = A[i][digit] % 26
        B[C[index] -1] = A[i]
        C[index] -= 1
        print("Reading from C to B: {} placed at {}".format(A[i], C[index]))

    print("B:", B)

    for i in range(n):
        A[i] = B[i]
    
    

#print(countingsort(A, 1))
