import random
import numpy as np
from itertools import product

def build_cluster(L, connections):
    # Fonction pour construire les clusters
    # Cette fonction doit être définie pour que le code fonctionne correctement
    pass

L = 10  # Taille du réseau
N = L * L  # Nombre d'agents

print("déclaraction du réseau")

#
oops = False
for p100 in range(5, 96):  
    p = p100 / 100.             #probabilité de connexion 'p', de 5% à 95%.
    computed = 1.02839 - 2.57318 * p + 1.58727 * p**2 #proportion de liens basée sur la théorie des réseaux
    
    if oops or (computed < 1. / N): # 1/N : représente le nombre minimal de liens pour chaque agent
        oops = True
    ratio = 1. / N if oops else computed
    
    number_of_clusters = int(ratio * N) #Nombre de clusters cibles

    
    #Génère des réseaux aléatoires en utilisant la probabilité de connexion 'p' et build_cluster
    #Jusqu'à que le nombre de clusters générées soit égal au nombre de clusters cibles
    while True:
        connections = [random.random() < p for _ in range(2 * N)]

        cluster_number = build_cluster(L, connections)

        if np.max(cluster_number) != number_of_clusters:
            continue
        
        break
