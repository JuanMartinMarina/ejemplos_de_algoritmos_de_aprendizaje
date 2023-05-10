import numpy as np
from sklearn.cluster import KMeans

# Crear un conjunto de datos de clientes aleatorios
clientes = np.array([["Juan", 1, 3], ["Pedro", 2, 3], ["María", 1, 2], ["Ana", 2, 2], ["Luis", 5, 6], ["Marta", 6, 5], ["José", 5, 7], ["Lucía", 6, 6]])

# Seleccionar las columnas que se utilizarán para el clustering
X = clientes[:, 1:]

# Crear el modelo de clustering K-Means con dos clusters
model = KMeans(n_clusters=2)

# Entrenar el modelo con los datos
model.fit(X)

# Obtener los clusters asignados para cada punto de datos
clusters = model.predict(X)

# Asignar las etiquetas de cluster a cada cliente
for i in range(len(clientes)):
    clientes[i, 0] = "Cluster " + str(clusters[i] + 1)

# Imprimir la lista de clientes con las etiquetas de cluster asignadas
print(x)
