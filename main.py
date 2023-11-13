import random
from Guordel import Guordel
from res.lemario import set_palabras_validas
from res.palabras_escogidas import set_palabras_escogidas
import pygame
from Boton import Boton
from Cuadricula import Cuadricula


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

    pygame.init()
    cuadricula = Cuadricula()

    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))
    reloj = pygame.time.Clock()

    game_menu = True

    boton_inicio = Boton(24,4,2,texto= "Buenos días alegría")

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
                # Ciclo principal del juego
        for event in pygame.event.get():

            # Salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #fondo de pantalla
        pantalla.fill(cuadricula.color)

        if game_menu:
            # Si se da al botón de empezar, se inicia el juego
            if boton_inicio.draw(pantalla):
                game_menu = False
            pygame.display.update()
            # El menu se actualiza a 60 fps
            reloj.tick(60)

        if not game_menu:
            pass

    #jugar()
