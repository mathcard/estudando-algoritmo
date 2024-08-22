# Minha resposta
def soma_array(arr):    
    if len(arr) == 0:
        return 0
                
    restante_do_array = arr[1:]      
    return 1+soma_array(restante_do_array)

numeros = [2, 4, 6, 50, 80]
resultado = soma_array(numeros)

print(f'A contagem dos elementos do array é: {resultado}')


# Responsta do livro
def soma_array2(arr):    
    if arr == []:
        return 0
    return 1+soma_array2(arr[1:])

numeros2 = [2, 4, 6, 50, 80]
resultado2 = soma_array(numeros2)
print(f'A contagem dos elementos do array é: {resultado2}')