import numpy as np

def main():
    L = 10  # Lattice size
    N = L * L  # Number of agents

    for p in range(5, 96):
        print(p)
        cluster_number = build_cluster(L, nets[p])
        print(cluster_number[0])
        print(cluster_number[1])
        print(cluster_number[N-1])
        print(max(cluster_number))
        if p == 10:
            return

def build_cluster(L, net):
    #define params L and net
    #implemente the function
    
    pass


if __name__ == "__main__":
    main()
