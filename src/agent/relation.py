import numpy as np
import pandas as pd

def main():
    file_path = "mbb-cac40.out"
    K = 10

    # Lire le fichier et stocker les données dans un DataFrame
    data = pd.read_csv(file_path, delimiter='\s+', header=None, names=['item', 'value'])
    
    # Créer une liste vide pour stocker les résultats
    results = []

    for index, row in data.iterrows():
        if row['item'] == "block_size":
            block_size = int(row['value'])
        elif row['item'] == "Omega":
            # Créer une matrice Omega vide de taille K x K
            Omega = np.zeros((K, K))

            # Lire les valeurs d'Omega et les stocker dans la matrice
            for i in range(K):
                for j in range(K):
                    index += 1
                    Omega[i, j] = data.iloc[index]['value']
            
            # Calculer les valeurs propres d'Omega
            eigenvalues = np.linalg.eigvalsh(Omega)
            
            # Afficher les résultats
            print(f"{block_size}\t{np.sum(eigenvalues)}")

if __name__ == "__main__":
    main()

