import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Parâmetros
Lx = 1.0  # Comprimento do domínio em x
Ly = 1.0  # Comprimento do domínio em y
Nx = 100   # Número de pontos de grade em x
Ny = 100   # Número de pontos de grade em y
angle = 45.0  # Ângulo em graus

# Converte o ângulo para radianos
theta = np.radians(angle)

# Criação da grade em coordenadas oblíquas
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Transformação das coordenadas oblíquas
X_oblique = X * np.cos(theta) - Y * np.sin(theta)
Y_oblique = X * np.sin(theta) + Y * np.cos(theta)

# Condições iniciais
u = np.zeros((Ny, Nx))

# Condições de contorno
u[:, 0] = 0  # Condição de contorno esquerda
u[:, -1] = 0  # Condição de contorno direita
u[0, :] = 1  # Condição de contorno superior
u[-1, :] = 0  # Condição de contorno inferior

# Parâmetros do método de diferenças finitas
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

# Iterações para resolver a equação de Laplace
for _ in range(1000):  # Número de iterações
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[j, i] = 0.25 * (u[j, i - 1] + u[j, i + 1] + u[j - 1, i] + u[j + 1, i])

# Plotagem dos resultados
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_oblique, Y_oblique, u, cmap='viridis')
ax.set_title('Solução da Equação de Laplace em Coordenadas Oblíquas (45 graus)')
ax.set_xlabel('X_oblique')
ax.set_ylabel('Y_oblique')
ax.set_zlabel('U')
plt.show()
