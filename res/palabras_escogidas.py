archivo_escogidas = 'res/palabras_escogidas.txt'
set_palabras_escogidas = set()

with open(archivo_escogidas, 'r') as file:
    for linea in file:
        palabra = linea.strip()
        set_palabras_escogidas.add(palabra.upper())
