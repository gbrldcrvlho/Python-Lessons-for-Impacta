# 1) Crie um programa que solicite ao usuario um numero natural e exiba a sequencia crescente de um até o numero dado.

n = int(input('numero: '))

for i in range(0, n + 1):
    print(i, end='\n')

# 2) Crie um programa que solicite ao usuario um numero natural e exiba a sequencia crescente de zero ate o numero dado, somente os pares.

n = int(input('numero: '))

for i in range(0, n + 1, 2):
    print(i, end=' \n')

# 3) Crie um programa que solicite ao usuario um numero natural e exiba a sequencia decrescente do numero dado até o numero um.

n = int(input('numero: '))

for i in range(n, 0, -1):
    print(i, end='\n')

# 4) Crie um programa que exiba os sete dias da semana.

dias = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')

for dia in dias:
    print(dia)