# Busca por seleção
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def buscaMaior(arr):
    maior = arr[0]
    maior_indice = 0
    for i in range(1, len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            maior_indice = i
    return maior_indice

# def ordenacaoporSelecao(arr):
#     novoArr = []
#     for i in range(len(arr)):
#         menor = buscaMenor(arr)
#         novoArr.append(arr.pop(menor))
#     return novoArr

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

desc = ordenacaoporSelecao([27, 5, 3, 6, 2, 10], 'desc') 
asc = ordenacaoporSelecao([27, 5, 3, 6, 2, 10], 'asc')
print(desc)
print(asc)