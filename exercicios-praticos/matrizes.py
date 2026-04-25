# Crie uma matriz 3x3 de zeros no VSCode e preencha com números aleatórios (use import random e loops).
import random

matriz = []

for i in range(3):
    linha = []  
    for j in range(3):
        linha.append(random.randint(0, 9))
    matriz.append(linha)  

for linha in matriz:
    print(linha)

# Some duas matrizes de vendas (ex.: vendas semanais) e calcule o total.
vendas1 = [
    [10, 20, 30],
    [5, 15, 25],
    [8, 12, 18]
]

vendas2 = [
    [7, 14, 21],
    [3, 6, 9],
    [2, 4, 6]
]

soma = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(vendas1[i][j] + vendas2[i][j])
    soma.append(linha)

print("Matriz soma:")
for linha in soma:
    print(linha)

total = 0
for linha in soma:
    total += sum(linha)

print("\nTotal geral de vendas:", total)

# Usando NumPy, crie uma matriz de dados de alunos e calcule médias por linha.
import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5],
    [9.0, 8.5, 10.0],
    [5.5, 6.0, 7.0]
])

medias = notas.mean(axis=1)

print("Notas:")
print(notas)

print("\nMédias por aluno:")
print(medias)

# Calcule o determinante de uma matriz 3x3 representando coeficientes de um sistema linear e verifique se é resolvível.

import numpy as np
A = np.array([
    [2, -1, 3],
    [1, 0, 2],
    [4, 1, 8]
])

det = np.linalg.det(A)

print("Matriz A:")
print(A)

print("\nDeterminante:", det)

if det != 0:
    print("Sistema possui solução única")
else:
    print("Sistema não possui solução única")

# Transponha uma matriz de dados de estoque e multiplique por uma matriz de preços para calcular totais.
import numpy as np

estoque = np.array([
    [10, 5, 8],   # produto 1
    [7, 3, 6],    # produto 2
    [4, 2, 9]     # produto 3
])

precos = np.array([2.5, 5.0, 10.0])

estoque_T = estoque.T

totais = np.dot(estoque_T, precos)

print("Estoque transposto:")
print(estoque_T)

print("\nTotais por loja:")
print(totais)