import random as rd

class Farm:

    def __init__(self, size: tuple, loading_factor: float) -> None:
        self.n, self.m = size[0], size[1]
        
        # init table
        if (self.n == 0) or (self.m == 0):
            print("size fields cannot be zero")
            exit()

        self.farm = [ (i, j) for j in range(self.m) for i in range(self.n) ]
        
        # start and target cells
        self.target_cell = (self.n-1, self.m-1)
        self.start_cell = (0, 0)

        # init weedy cells
        loading_factor = int(loading_factor * (self.n * self.m))
        self.weeds = [(rd.randint(0, self.n-1), rd.randint(0, self.m-1)) for i in range(loading_factor)]

        # make start and target cells weedy
        self.weeds.append(self.start_cell)
        self.weeds.append(self.target_cell)


    def print_farm(self, trace = None):

        for i in range(self.n):
            for j in range(self.m):
                s = ""
                if trace is not None and (i, j) in trace:
                    s += "+"
                if (i, j) in self.weeds:
                    s += "x"
                else:
                    s+= "-"
                print(s, end='\t')

            print("\n")

    def set_weeds(self,  manuel: list):
        self.weeds = []
        for i, row in enumerate(manuel):
            for j, column in enumerate(row):
                if column == 1:
                    self.weeds.append((i, j))