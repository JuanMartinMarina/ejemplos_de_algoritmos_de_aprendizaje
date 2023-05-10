# Importar las librerías necesarias
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar el conjunto de datos
X = [[0], [1], [2], [3]]
y = [0, 1, 2, 3]

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones con los datos de prueba
predictions = model.predict(X_test)

# Evaluar el rendimiento del modelo
score = model.score(X_test, y_test)
print("Puntuación:", score)
