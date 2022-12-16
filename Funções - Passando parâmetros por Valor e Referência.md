Sabemos que os parâmetros de uma função tem o importante papel de fornecer os insumos (matéria-prima) da função. Utilizando corretamente os parâmetros de uma função podemos deixá-la muito mais reutilizável. Sabemos também que as funções conseguem alterar apenas as variáveis do seu escopo, as variáveis locais a função. Vamos aprender neste capítulo as duas formas que a função tem de passar parâmetros para uma função: por valor e por referência. Vamos ver que na passagem por valor a variável utilizada como parâmetro não consegue ser alterada pela função mas na passagem por referência a função consegue alterar essa variável.

```
def mult(v, tam, mul):
    i = 0
    
    while i < tam:
        v[i] = mul*v[i]
        i = i + 1
    mul = 0
    return

a = [1, 2, 3]
n = 3
m = 5
mult(a,n,m)

