Neste texto é discutido o conceito de estrutura de seleção encadeada ou aninhada.
Como exemplificação mostra-se uma implementação de um exemplo usando fluxogramas,
um segundo exemplo usando fluxogramas juntamente com uma simulação.
Ao final é mostrado um terceiro exemplo usando fluxograma com sua conversão para Python.

```
print('Digite a idade')
idade = int(input())

if idade < 10:
    print('Infantil')
else:
    if idade < 18:
        print('Teen')
    else:
        print('Senior')