Neste capítulo vamos abordar algoritmos um pouco mais complexos. Primeiramente vamos discutir dois tipos de busca: a busca linear e uma busca otimizada que é a busca binária. Em seguida vamos discutir um algoritmo de ordenação pouco eficiente mas de fácil implementação: o Bubble Sort. Ao final, mostramos a conversão do Bubble Sort para Python.

```
def buscab(V,num,tam):
    ini = 0
    fim = tam - 1
    
    while ini <= tam:
        meio = (ini + fim) // 2

        if V[meio] == num:
            return meio
        elif num > V[meio]:
            ini = meio + 1
        else: 
            fim = meio - 1

    return -1

V = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
pos = buscab (V, 70, 10)

if pos == -1:
    print('O numero não foi encontrado'
else:
    print('O numero foi encontrado na posição', pos)