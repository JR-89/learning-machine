import string

def contar_palabras(texto):
    # Convertir a minúsculas y eliminar signos de puntuación
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Crear un diccionario para contar la frecuencia de cada palabra
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

# Pedir al usuario que ingrese una frase o párrafo
texto = input("Ingresa una frase o párrafo: ")

# Contar las palabras y mostrar la frecuencia de cada una
frecuencias = contar_palabras(texto)

print("\nFrecuencia de cada palabra:")
for palabra, frecuencia in frecuencias.items():
    print(f"'{palabra}': {frecuencia} vez/veces")