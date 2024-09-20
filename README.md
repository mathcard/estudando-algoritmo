# estudando-algoritmo

## Capítulo 1
### BigO
- Trata-se de uma notação que diz quão rápido é um algoritmo.
- Tipos de execução BigO: O(n). O(logn), 

### Memória
- A memória do seu computador e como um conjunto gigante de gavetas.

### Pesquisa Binaria
Pesquisa binária é um algotimo, utilizado em uma lista ordenada



## Capítulo 2 - Ordenação por seleção
Endereço de memória

### Arary
- Os dados são inseridos em um espeço definido de memória
- Possuem capacidade de leitura mais raída.

#### Tempo de Execução
Leitura O(1)
Inserção O(n)
Deleção O(n)

### Lista encadeadas
- Os dados são armazenados em endereços aleatorios
- Possuem capacidade de inserção mais rápida

#### Tempo de Execução
Leitura O(n)
Inserção O(1)
Deleção O(1)

### Ordenção por seleção
- Algoritmos de ordenação são muito úteis, porém não são muito rápidos. Tempo de execução O(n)2
```phyton
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def buscaMaior...

def ordenacaoporSelecao(arr, operation):
    novoArr = []
    for i in range(len(arr)):
        if operation == 'asc':            
            menor = buscaMenor(arr)
            novoArr.append(arr.pop(menor))
        else:
            maior = buscaMaior(arr)
            novoArr.append(arr.pop(maior))        
    return novoArr
```

## Capítulo 3 - Recursão
- Utiliza Pilha - CallStack
- É uma função que chama ela mesma.
-  As funções tem dois casos, caso-base e caso recursivo.
- Caso a função não possua um caso-base, a pilha irá crescer até chegar o overflow.

Push - Adicionar em novo item ao top
POP - Reve o item do top

## Capítulo 4 - 
####  Dividir para Conquistar DC
1 - Descubra o caso-base, que deve ser mais simples possível.
2 - Divia ou diminua o seu problema até que ele se torne o caso-base



#### Quicksort
- Algoritmo de ordenação elegante que é utilizado com frequência. Utiliza técnica dividir para conquistar. DC.

1 - Escolha um pivô
2 - Particione o array em dois subarray
3 - Execute o quicksort recursivamnete em ambos subarrays.

Merge sort versus quicksort

Caso médio versus pior caso




## Capítulo 5 - Tabelas Hash



## Capítulo 6 - Pesquisa em Largura BFS
A pesquisa em largura permite encontrar o menor caminho entre dois objetos. 

Exe: Menor qtd movimento vencer no xadrex. Medico mais próximo. etc...

A pesquisa em largura utiliza grafos.

A pesquisa em largura diz se há um caminha de A para B.

Se o caminho existir, a pesquisa em largura lhe dará o caminho mínimo.

Valide para não verificar o mesmo grafo novamente, para não ficar me loop infinito.

#### Grafos
Um conjunto de conexões () -> () -> ()

#### Filas
Funciona como filas da vida real, apenas duas funções, enfileirar e desenfileirar. FIFO

## Capítulo 7 - Algortimo de Dijkstra
Permite trabalho do grafos ponderados.

A pesquisa em largura traz o caminho com menos percursos, porém o Algoritmo de Dijkstra traz o caminho mais rápido. (menor tempo)

1 - Encontre o vértie mais barato. Vertice consegue chegar em menos tempo.
2 - Verifica se há um caminho mais barato para os vizinhos desse vértice, caso exista atualiza o custo.
3 -  Repita até que você tenho feito isso para cada vértice do grafo.
4 -  Calcule o caminho final

Caminho mais rápido

Não funciona com peses negativos.

## Capítulo 8 - Algortimos gulosos

Cobertura dos conuntos