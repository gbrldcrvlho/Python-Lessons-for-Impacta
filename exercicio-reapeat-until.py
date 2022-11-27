# Crie um programa que receba um numero.
# n >= 0 e exiba o valor da raiz quadrada.
# De n. Enquanto n for um numero negativo, repita a solicitação de entrada

from math import sqrt

while True:
    n = float(input('Número: '))
    if n >= 0: break

print(f'Raiz quadrada de {n} é {sqrt(n)}')