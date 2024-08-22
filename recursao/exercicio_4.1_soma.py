def soma_array(arr):    
    if len(arr) == 0:
        return 0
    
    primeiro_elemento = arr[0]
    restante_do_array = arr[1:]  # Array sem o primeiro elemento        
    return primeiro_elemento + soma_array(restante_do_array)

# Exemplo de uso:
numeros = [2, 4, 6]
resultado = soma_array(numeros)

print(f'A soma dos elementos do array é: {resultado}')
