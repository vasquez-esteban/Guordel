# import random

# palabras_por_longitud = {4: [], 5: [], 6: [], 7: [], 8: []}
#
# with open('palabras_validas.txt', 'r') as file:
#     palabras = file.readlines()
#
# for palabra in palabras:
#     palabra = palabra.strip()
#     longitud = len(palabra)
#     if 4 <= longitud <= 8:
#         palabras_por_longitud[longitud].append(palabra)
#
# palabras_seleccionadas = []
# longitudes = list(range(4, 9))
# for longitud in longitudes:
#     if len(palabras_por_longitud[longitud]) >= 10:
#         seleccion = random.sample(palabras_por_longitud[longitud], 10)
#         palabras_seleccionadas.extend(seleccion)
#     else:
#         print(f"No hay suficientes palabras de {longitud} letras en el palabras_validas.")
#
# with open('palabras_escogidas.txt', 'w') as file:
#     file.writelines('\n'.join(palabras_seleccionadas))

if __name__ == '__main__':
    with open('palabras_escogidas.txt', 'r') as file:
        palabras_4_letras = 0
        palabras_5_letras = 0
        palabras_6_letras = 0
        palabras_7_letras = 0
        palabras_8_letras = 0

        for linea in file:
            palabra = linea.strip()

            if len(palabra) == 4:
                palabras_4_letras += 1
            elif len(palabra) == 5:
                palabras_5_letras += 1
            elif len(palabra) == 6:
                palabras_6_letras += 1
            elif len(palabra) == 7:
                palabras_7_letras += 1
            elif len(palabra) == 8:
                palabras_8_letras += 1

    print("Palabras de 4 letras:", palabras_4_letras)
    print("Palabras de 5 letras:", palabras_5_letras)
    print("Palabras de 6 letras:", palabras_6_letras)
    print("Palabras de 7 letras:", palabras_7_letras)
    print("Palabras de 8 letras:", palabras_8_letras)
