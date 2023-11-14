import random
from Guordel import Guordel
from res.lemario import set_palabras_validas
from res.palabras_escogidas import set_palabras_escogidas

import pygame
from pygame.locals import *
from Boton import Boton
from BotonSeleccion import BotonSeleccion
from Cuadricula import Cuadricula

from TableroPalabras import TableroPalabras



def print_yellow(text):
    return print(f"\033[33m{text}\033[0m")


def print_green(text):
    return print(f"\033[32m{text}\033[0m")


def jugar(dificultad):
    juego = Guordel(dificultad)

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
    font = pygame.font.SysFont('Constantia', 32)
    
    cuadricula = Cuadricula()

    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))
    reloj = pygame.time.Clock()

    game_menu = True

    boton_inicio = Boton(260, 400, 2,texto= "Empezar a jugar")
    otro_boton = Boton(500, 400, 2,texto= "Recibir por consola")
    seleccion_dificultad = BotonSeleccion(310, 300, 2, 3, "4","5","6")
    

    dificultad = None

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

            #Titulo
            texto = font.render("GUORDEL", True,(0,0,0))
            textoRect = texto.get_rect()
            textoRect.topleft = (290, 200)
            pantalla.blit(texto, textoRect)

            dificultad = seleccion_dificultad.draw(pantalla, dificultad)
            

            if boton_inicio.draw(pantalla):
                game_menu = False
                tablero_de_palabras = TableroPalabras(200, 100, 2, dificultad)
                recibir = True
           

        if not game_menu:
            #jugar(int(dificultad))
            
            tablero_de_palabras.dibujar_tablero(pantalla, True)
            #Cuando esté habilitado escribir por consola utilizas los comandos "a","f","b","d"
            if recibir:
            
                accion = input().split()
                #prefijo "a" para agregar una letra
                if accion[0] == "a":
                    tablero_de_palabras.agregar_letra(accion[1])
                #cambiar a vizualizazión del juego
                if accion[0] == "f":
                    recibir = False
                #equivalente a Enter
                if accion[0] == "b":
                    #regresa la palabra si cumple con el tamaño establecido
                    print(tablero_de_palabras.confirmar_palabra())
                #delete
                if accion[0] == "d":
                    tablero_de_palabras.eliminar_letra()
            
            if otro_boton.draw(pantalla):
                recibir = True
                
        
        pygame.display.update()

        reloj.tick(9)
    
