# crie um programa que receba um numero natural n (n>1).
# exiba uma mensagem indicando se não for primo.

n = int(input('Numero: '))
divisor = 2

while divisor < n:
    print(f'{n} % {divisor} = {n % divisor}')
    if n % divisor == 0:
        break
    divisor += 1

if divisor == n:
    print('Primo!')
else:
    print('Não é primo!')