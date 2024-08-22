def quicksort(array):
    if len(array) < 2:
        return array
    else:

        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        print("Array: {}; Menores: {};  Pivo: {}; Maiores: {};".format(array, menores, pivo, maiores))        
        return quicksort(menores) + [pivo] + quicksort(maiores)        

print(quicksort([10, 5, 2, 3, 70, 1]))


