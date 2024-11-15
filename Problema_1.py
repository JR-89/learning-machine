lista = [2, -3, -5, 7, -8, 1, -6, 10]
def separar_numeros(lista):
    # Crear listas separadas para negativos y positivos
    negativos = [num for num in lista if num < 0]
    positivos = [num for num in lista if num > 0]
    
    return negativos, positivos

negativos, positivos = separar_numeros(lista)

print("Negativos:", negativos)  # Resultado esperado: [-3, -5, -8, -6]
print("Positivos:", positivos)  # Resultado esperado: [2, 7, 1, 10]