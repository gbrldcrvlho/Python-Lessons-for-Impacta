Neste texto é discutido o conceito de estrutura de repetição encadeada ou aninhada. Nessa construção um laço é inserido dentro de outro laço. Forma-se assim uma repetição de uma repetição. Como exemplificação mostra-se uma implementação de um exemplo usando fluxogramas, um segundo exemplo usando fluxogramas juntamente com uma simulação. Ao final é mostrada a conversão do fluxograma para Python.

```
def tabuada():
    tab = 1
    
    while tab <= 5:
    i = 1
        while i <= 10:
            print(tab,' x ',i,' ',tab*i)
            i = i + 1
        tab = tab + 1
    return

tabuada()