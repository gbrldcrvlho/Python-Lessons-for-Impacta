Você tem ideia de como três programadores conseguem trabalhar em um mesmo programa? Existe uma maneira simples de reaproveitar um código que resolve um problema em um outro programa? Uma função nada mais é do que um trecho de código que damos um nome. Os parâmetros e o retorno potencializam muito o uso das funções.  Esses são os assuntos discutidos nesse texto.

```
def bem_vindo():
    print('Bem vindo! Vamos calcular a média')
    return

def retorna_media(num1, num2, num3):
    media = (num1+num2+num3)/3
    return media

bem vindo()

print('Digite o primeiro valor: ')
n1 = int(input())

print('Digite o segundo: ')
n2 = int(input())

print('Digite o terceiro valor: ')
n3 = int(input())

resposta = retorna_media(n1,n2,n3)
print('A média é:', resposta)
