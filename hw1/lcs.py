import timeit
import matplotlib.pyplot as plt
import numpy as np


def sequenceReader(fileName1 : str, fileName2 : str, n: int)->dict:
    fileName1 = "./randomDNA/" + fileName1
    fileName2 = "./randomDNA/" + fileName2
    
    file1 = open(fileName1, "r")
    file2 = open(fileName2, "r")
    counter = 0
    seqDict = {}

    for (line1, line2) in zip(file1, file2):
        if counter > 30:
            break
        if line1.startswith('>'):
            counter += 1
            seqDict[counter] = ["", ""]
        elif counter != 0:
            seqDict[counter][0] += line1.strip()[0:n+1]
            seqDict[counter][1] += line2.strip()[0:n+1]
        
    return seqDict


def generate_sample(X: str, Y: str, n: int) -> tuple:
    x = X[0:n]
    y = Y[0:n]
    return x, y


def lcs(X:str,Y:str,i:int,j:int) -> int:
    if (i == 0 or j == 0):
       return 0
    elif X[i-1] == Y[j-1]:
       return 1 + lcs(X,Y,i-1,j-1)
    else:
        return max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))


def lcs_memo(X:str,Y:str,i:int,j:int, c:list)->int:
    if c[i][j] >= 0:
        return c[i][j]
    if (i == 0 or j == 0):
        c[i][j] = 0
    elif X[i-1] == Y[j-1]:
        c[i][j] = 1 + lcs_memo(X,Y,i-1,j-1,c)
    else:
        c[i][j] = max(lcs_memo(X,Y,i,j-1,c),lcs_memo(X,Y,i-1,j,c))
    return c[i][j]


def average_running_time(dna_seq: list, base:int) -> tuple:

    art_naive = []
    art_memo = []

    for p in dna_seq:
        X, Y = p[0], p[1]
        
        if base <= 20:   
            start = timeit.default_timer()
            lcs(X,Y,base,base)
            stop = timeit.default_timer()
            art_naive.append(stop - start)

        c = [[-1 for k in range(base+1)] for l in range(base+1)]
        start = timeit.default_timer()
        lcs_memo(X,Y,base,base, c)
        stop = timeit.default_timer()
        art_memo.append(stop - start)
    
    # runtimes of each 30 runs in list format
    # to be stored in a dict= {5: [...], 6:[...], ... }
    print("Base:", base)
    print("Averge mean of naive LCS is: ", np.mean(art_naive))
    print("Averge std of naive LCS is: ", np.std(art_naive))
    print("Averge mean of memoization LCS is: ", np.mean(art_memo))
    print("Averge std of memoization LCS is: ", np.std(art_memo))
    return art_naive, art_memo


def worst_running_time(X:str, Y:str, base:int) -> tuple:
    print("Base:", base)
    start = timeit.default_timer()
    lcs(X,Y, base, base)
    stop = timeit.default_timer()
    naive_rt = stop - start
    print("Worst running time of naive LCS is: ", naive_rt)

    c = [[-1 for k in range(base+1)] for l in range(base+1)]
    start = timeit.default_timer()
    lcs_memo(X,Y,base,base, c)
    stop = timeit.default_timer()
    memo_rt =  stop - start
    print("Worst running time of memoization LCS is: ", memo_rt)

    return naive_rt, memo_rt


def drawGraph_average(art: dict, alg:str, sub, interval):
    # naive/memo art
    mean_values_list = list()
    std_values_list = list()

    for base in interval:
        sub.scatter([base]*30, art[base], color="grey") # multiple dots on x = 5 vertical line
        mean_values_list.append(np.mean(art[base])) # mean of average run times per base
        std_values_list.append(np.std(art[base])) # std of art per base

    sub.plot(interval, mean_values_list, color = "green", label = "Mean") # plot of means
    sub.plot(interval, std_values_list, color = "blue", label = "Std") # plot of std
    
    sub.set_xlabel("Length of String")
    sub.set_ylabel("Time (seconds)")
    sub.set_title(alg)




def drawGraph_worst(wrt: dict, alg: str, sub):

    wrt_values = [wrt[base] for base in range(5,16,1)]    
    
    sub.plot(np.arange(5,16), wrt_values, color = "red") # plot of wrt
    sub.set_xlabel("Length of String")
    sub.set_ylabel("Time (seconds)")
    sub.set_title(alg)
    


def main():

    wrt_naive, wrt_memo, art_naive, art_memo = dict(), dict(), dict(), dict()

    fig, sub = plt.subplots(2,2)
    worst_range = np.arange(5, 16)
    average_range = np.arange(5, 26)
    
    
    """
    # worst_case
    for base in worst_range:
        X, Y = generate_sample("aaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbb", base)
        n, m = worst_running_time(X, Y, base)
        wrt_naive[base] = n
        wrt_memo[base] = m
    
    drawGraph_worst(wrt_naive, "naive", sub[0][0])
    drawGraph_worst(wrt_memo, "memoization", sub[0][1])
    """
    
    # average_case
    for base in average_range:
        dna_seq = sequenceReader("seq{}_1".format(base), "seq{}_2".format(base), base)
        del dna_seq[31]   

        n, m = average_running_time(list(dna_seq.values()), base)
        art_naive[base] = n
        art_memo[base] = m
        


    drawGraph_average(art_naive, "naive", sub[1][0], np.arange(5,21))
    drawGraph_average(art_memo, "memoization", sub[1][1], np.arange(5,26))    
    

    fig.tight_layout()
    fig.legend()
    plt.show()

# -------------------------


if __name__ == "__main__":
    main()

