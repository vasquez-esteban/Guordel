import random
from Guordel import Guordel
from res.lemario import set_palabras_validas
from res.palabras_escogidas import set_palabras_escogidas


def print_yellow(text):
    return print(f"\033[33m{text}\033[0m")


def print_green(text):
    return print(f"\033[32m{text}\033[0m")


def jugar():
    juego = Guordel(4)

    print("GUORDEL")
    intentos = 0
    palabra_oculta = get_palabra_random(juego.dificultad)

    while intentos < 6:
        adivina = input("Adivine la respuesta: ").upper()

        if not es_valida(adivina, palabra_oculta):
            print("No ingresó una palabra válida")
            continue

        if adivina == palabra_oculta:
            print('PALABRA ADIVINADA!')
            print_green(palabra_oculta)
            break

        mostrar_resultado_adivinar(palabra_oculta, adivina)

        intentos += 1

    else:
        print(f"la palabra oculta era: {palabra_oculta}")


def get_palabra_random(longitud_palabra):
    list_palabras_escogidas = list(set_palabras_escogidas)
    filtradas = [word for word in list_palabras_escogidas if len(word) == longitud_palabra]
    return random.choice(filtradas)


def es_valida(adivina, palabra_oculta):
    return (len(adivina) == len(palabra_oculta)) and (adivina in set_palabras_validas)


def mostrar_resultado_adivinar(palabra_oculta, adivina):
    resultado = []

    for indice in range(len(palabra_oculta)):
        if palabra_oculta[indice] == adivina[indice]:
            resultado.append(f"\033[32m{palabra_oculta[indice]}\033[0m")
        else:
            if adivina[indice] in palabra_oculta:
                resultado.append(f"\033[33m{adivina[indice]}\033[0m")
            else:
                resultado.append(adivina[indice])

    print("".join(resultado))


if __name__ == '__main__':
    jugar()
