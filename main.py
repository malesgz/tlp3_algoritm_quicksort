def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

# Prueba 1: Lista ordenada
print(quicksort([1, 2, 3, 4, 5]))

# Prueba 2: Lista desordenada
print(quicksort([5, 2, 8, 1, 9, 3, 7, 4, 6]))

# Prueba 3: Lista con elementos repetidos
print(quicksort([5, 2, 8, 1, 9, 3, 7, 4, 6, 5, 3]))

# Prueba 4: Lista vacía
print(quicksort([]))

# Prueba 5: Lista con un solo elemento
print(quicksort([42]))