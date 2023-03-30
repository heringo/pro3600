import random
import numpy as np
from itertools import product

def build_cluster(L, connections):
    # Fonction pour construire les clusters
    # Cette fonction doit être définie pour que le code fonctionne correctement
    pass

L = 10  # Taille du réseau
N = L * L  # Nombre d'agents

print("std::map<UInt, std::vector<char>> nets {")

#
oops = False
for p100 in range(5, 96):
    p = p100 / 100.
    computed = 1.02839 - 2.57318 * p + 1.58727 * p**2
    
    if oops or (computed < 1. / N):
        oops = True
    ratio = 1. / N if oops else computed
    
    number_of_clusters = int(ratio * N)

    while True:
        connections = [random.random() < p for _ in range(2 * N)]

        cluster_number = build_cluster(L, connections)

        if np.max(cluster_number) != number_of_clusters:
            continue

        print(f"{{ {p100}, {{", end=" ")
        for cell in connections:
            print(f"{'\\1' if cell else '\\0'},", end=" ")
            print("}},", end="\n")
        break


print("};")
