Usamos vetores no nosso dia-a-dia. Talvez o nome não seja bem esse. Conhecemos mais como listas. Neste texto é discutido o conceito de vetores, seus componentes e a sua forma de utilização. A grande vantagem dos vetores reside justamente na sua capacidade de armazenar uma grande quantidade de informação na memória. É esse justamente o seu objetivo como ferramenta: sempre que tivermos a necessidade de armazenar uma grande quantidade de informação vamos usar esse recurso. Como exemplificação mostra-se uma implementação de um exemplo usando fluxogramas e um segundo exemplo usando fluxogramas juntamente com uma simulação mostrando como percorrer um vetor. Ao final é mostrada a conversão de um fluxograma usando vetores e funções para Python.

```
def conta(v, n, tam):
    cont = 0
    i = 0

    while i < tam:
        if [i] == n:
            cont = cont + 1
        i = i + 1
    return cont

a = [23, 4, 21, 3, 23]
print('Digite o numero a ser pesquisado')
num = int(input())
contn = conta(a, num, 5)
print('O numero foi encontrado', contn, 'vezes')