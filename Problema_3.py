def crear_conjunto():
    # Pedir al usuario ingresar números separados por comas y convertirlos a un conjunto de enteros
    entrada = input("Ingresa números enteros separados por comas: ")
    conjunto = {int(num) for num in entrada.split(",")}
    return conjunto

# Crear los dos conjuntos de números enteros
print("Conjunto 1:")
conjunto1 = crear_conjunto()

print("Conjunto 2:")
conjunto2 = crear_conjunto()

# Calcular la intersección, unión y diferencia simétrica
interseccion = conjunto1.intersection(conjunto2)
union = conjunto1.union(conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

# Mostrar los resultados
print("\nResultados:")
print("Intersección (elementos comunes):", interseccion)
print("Unión (todos los elementos sin duplicados):", union)
print("Diferencia simétrica (elementos en uno u otro conjunto, pero no en ambos):", diferencia_simetrica)