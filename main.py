from Guordel import Guordel
from res.lemario import set_palabras_validas
from res.palabras_escogidas import set_palabras_escogidas

# Archivo para correr el juego. Contiene los sets de palabras necesitados
# Se pueden jugar varias partidas


def print_yellow(text):
    return print(f"\033[33m{text}\033[0m")


def print_green(text):
    return print(f"\033[32m{text}\033[0m")


if __name__ == '__main__':
    juego = Guordel(5)
    jugando = True

    print("GUORDEL")
    intentos = 0

    # Se puede poner dentro de una función única
    while intentos < 6:
        # Se debe obtener una palabra de set_palabras_escogidas (todas están en mayúsculas)
        ejemplo = 'MELON'
        adivina = input("Adivine la respuesta: ").upper()

        # Verificar longitudes adecuadas
        if not (len(adivina) == len(ejemplo)):
            print("No ingresó una longitud válida de palabra")
            continue

        # Comprobar adivinanza y revelar letras correctas
        if adivina == ejemplo:
            print('PALABRA ADIVINADA!')
            print_green(ejemplo)
            break

        resultado = list()

        for indice in range(len(ejemplo)):
            if ejemplo[indice] == adivina[indice]:
                resultado.append(f"\033[32m{ejemplo[indice]}\033[0m")
            else:
                if adivina[indice] in ejemplo:
                    resultado.append(f"\033[33m{adivina[indice]}\033[0m")
                else:
                    resultado.append(adivina[indice])

        print("".join(resultado))
        # Controlar los intentos del jugador
        intentos += 1
