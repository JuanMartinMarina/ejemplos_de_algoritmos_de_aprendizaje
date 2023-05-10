import pygame
import numpy as np
import pylance

# Inicializar Pygame y crear la ventana
pygame.init()
screen = pygame.display.set_mode((400, 400))

# Inicializar la tabla de recompensas y la política de exploración epsilon-greedy
rewards = np.zeros((5, 5))
epsilon = 0.1

# Inicializar el estado actual y la tasa de aprendizaje
state = (0, 0)
learning_rate = 0.1
discount_factor = 0.9

# Bucle de entrenamiento
while True:
  # Dibujar el estado actual en la pantalla
  pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(state[0]*80, state[1]*80, 80, 80))
  pygame.display.flip()

  # Escoger una acción utilizando una política de exploración epsilon-greedy
  if np.random.rand() < epsilon:
    action = np.random.randint(4)
  else:
    action = np.argmax(rewards[state])

  # Realizar la acción y obtener el siguiente estado
  if action == 0:
    next_state = (min(state[0]+1, 4), state[1])
  elif action == 1:
    next_state = (max(state[0]-1, 0), state[1])
  elif action == 2:
    next_state = (state[0], min(state[1]+1, 4))
  elif action == 3:
    next_state = (state[0], max(state[1]-1, 0))

# Asignar la recompensa según el estado final alcanzado

if next_state == (2, 2):
  reward = 1
else:
  reward = 0

# Actualizar la tabla de recompensas utilizando el algoritmo de Q-learning
rewards[state][action] = rewards[state][action] + learning_rate * (reward + discount_factor * np.max(rewards[next_state]) - rewards[state][action])

# Asignar el siguiente estado como el estado actual
state = next_state

# Si el juego ha terminado, salir del bucle
if state == (2, 2):
    break

# Imprimir la tabla de recompensas final
print("Tabla de recompensas final:")
print(rewards)

