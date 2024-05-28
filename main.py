# Función que toma como argumento una lista.
def quicksort(array):
    # Se realiza verifica si la lista contiene menos de 1 elemento para devolverla en su estado orgininal.
    if len(array) <= 1:
        return array
    
    # Se selecciona como pivote al primer elemento de la lista.
    pivot = array[0]

    # Dos listas que contienen los elementos mayores y menores e iguales al pivote.
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    # Llamada recursiva de ambas listas de forma concatenada con el pivote para que al devolver el resultado se encuentre en el medio. 
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