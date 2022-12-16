```
def primo(n):
    i = n
    c = 0

    while i > 0:
        if n%i == 0:
            c = c + 1

        i = i -1

    if c == 2:
        ehprimo = 1
    else:
        ehprimo = 0

x = primo(5)

if x == 0:
    print('Não é primo')
else: 
    print('É primo')