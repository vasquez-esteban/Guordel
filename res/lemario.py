archivo_lemario = 'res/lemario.txt'
set_palabras_validas = set()

with open(archivo_lemario, 'r') as file:
    for linea in file:
        palabra = linea.strip()
        set_palabras_validas.add(palabra.upper())
