Neste texto é discutido o conceito de Estrutura de Repetição. Basicamente, a Estrutura de Repetição (também chamada loop ou laço) repete comandos. Podemos classificá-las em dois tipos: Indefinida e Definida. Na Estrutura de Repetição Indefinida, não sabemos o número de vezes que teremos que repeti-los. Na Estrutura de Repetição Definida, tem o objetivo de repetir comandos um determinado número fixo de vezes, ou seja, sabemos o número de vezes que teremos que repeti-los. Abordamos também o uso de laços usados na validação de dados de entrada, laços que utilizam variáveis chamadas Flags e, por fim, as variáveis contadoras usadas em contagens de eventos. Em seguida, abordamos laços que utilizam variáveis chamadas acumuladoras usadas para somar valores e por fim loops infinitos, aqueles que nunca terminam. Ao final é mostrado um exemplo usando fluxograma com sua conversão para Python.

```
def somatemp()
    soma = 0
    cont = 1

    while (cont <= 30):
        temp = float(input())
        soma = soma + temp
        cont = cont + 1
    return soma

S = somatemp()
print('A soma da temperatura é ', S)