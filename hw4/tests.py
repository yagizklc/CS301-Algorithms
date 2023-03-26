from weedBot import *
import timeit
import matplotlib.pyplot as plt
import numpy as np


def average_running_time(farms : list):
    art_bottom_up = []

    for farm in farms:
        start = timeit.default_timer()
        iter_farm(farm)
        stop = timeit.default_timer()
        art_bottom_up.append(stop - start)

    print(f"Average of bottom up approach is: {np.mean(art_bottom_up)}")
    print(f"Standard deviation of bottom up approach is: {np.std(art_bottom_up)}")
    return art_bottom_up


def draw_graph(art : dict, name : str, sub, type: str):
    mean = []
    std = []

    for size in range(5, 500):
        sub.scatter([size]*20, art[size], color="grey")
        mean.append(np.mean(art[size]))
        std.append(np.std(art[size]))
    
    if not (type == "loglog"):
        sub.plot(range(5, 500, 1), mean, color = "green", label = "Mean")
        sub.plot(range(5, 500, 1), std, color = "blue", label = "Std")
        sub.set_title(name)
    else:
        sub.loglog(range(5, 500, 1), mean, color = "green", label = "Mean")
        sub.loglog(range(5, 500, 1), std, color = "blue", label = "Std")
        sub.set_title("loglog")

    sub.set_xlabel("Size")
    sub.set_ylabel("Time (seconds)")


def black_box(test_no: int):

    # Try extremes
    if test_no == 1:
        # following code gives error and exits program
        #print("--- 1. Size = 0 ---")
        #size_0_farm = Farm((0, 0), 0.5)
        # size_0_farm.print_farm(solve(size_0_farm)) 
        pass

    elif test_no == 2:
        print("--- 2. No weed ---")
        empty_farm = Farm((5, 5), 0)
        empty_farm.print_farm(solve(empty_farm)) 
         

    elif test_no == 3:
        print("--- 3. Incrementally Increasing Size with Random Weed Locations ---")
        for size in range(5, 10):
            loading_factor = rd.uniform(0, 1)
            increasing_farm = Farm((size, size), loading_factor)
            increasing_farm.print_farm(solve(increasing_farm)    )       
            print("\n") 


def white_box(test_no: int, farm: Farm):

    # cover edges
    if test_no == 1:
        field1 = [ 
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [1,1,1,1]
        ]
        farm.set_weeds(field1)
        farm.print_farm(solve(farm))

    elif test_no == 2:
        field2 = [
            [1,1,1,1],
            [0,0,0,1],
            [0,0,0,1],
            [0,0,0,1]
        ]
        farm.set_weeds(field2)
        farm.print_farm(solve(farm))

    elif test_no == 3:
        field3 = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        farm.set_weeds(field3)
        farm.print_farm(solve(farm))

    elif test_no == 4:
        field4 = [
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,0,1]
        ]
        farm.set_weeds(field4)
        farm.print_farm(solve(farm))

    print("\n")


def main():

    case = int(input("Enter case:"))
    
    # following are the general tests
    if case == 1:
        print("\n---- General Test ----")
        n = int(input("Enter Row Number:"))
        m = int(input("Enter Column Number:"))
        factor = float(input("Enter Loading Factor:"))
        
        size = (n, m) 
        print("\n---- Initializing Farm ----")
        farm = Farm(size, factor)
        farm.print_farm()

        print("\n---- Agricultural Robot Starts ----")
        c = iter_farm(farm)
        path = backpropagate(c)
    
        print("\n---- Table ----")
        for i in range(len(c)):
            print(c[i])

        print("\n---- Path ----")
        for i in range(len(path)):
            print(path[i], end="->")

        print("\n\n---- Path on Farm ----")
        farm.print_farm(path)

    # following are the black-box tests   
    elif case == 2:
        print("\n---- Black-Box Testing ----")
        black_box(test_no=1)
        black_box(test_no=2)
        black_box(test_no=3)
   
    # following are the white-box tests
    elif case == 3:
        print("\n--- Starting White-Box Testing ---")

        farm = Farm((4,4), 0)
        for i in range(1,4):
            white_box(test_no=i, farm=farm)

    # following are the perfomance tests
    elif case == 4:
        print("\n---- Performance Tests Start ----")

        art_bottom_up = {}
        fig, sub = plt.subplots(1,2)

        farms = []
        for size in range(5,600):
            for i in range(20):
                loading_factor = rd.randrange(0,1)
                farms.append(Farm((size,size), loading_factor)) 
                
            avg = average_running_time(farms)
            art_bottom_up[size] = avg
            farms = []

        draw_graph(art_bottom_up, "Bottom Up", sub[0], "normal")
        draw_graph(art_bottom_up, "Bottom Up", sub[1], "loglog")
        plt.show()
        


main()


