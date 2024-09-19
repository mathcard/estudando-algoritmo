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



## Capítulo 6 - Pesquisa em Largura
Grafos

## Capítulo 7 - Algortimo de Dijkstra


## Capítulo 8 - Algortimos gulosos

Cobertura dos conuntos