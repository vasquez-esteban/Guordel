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


def get_palabra_random(longitud_palabra):
    list_palabras_escogidas = list(set_palabras_escogidas)
    filtradas = [
        word for word in list_palabras_escogidas if len(word) == longitud_palabra
    ]

    return random.choice(filtradas)


def es_valida(adivina, palabra_oculta):
    return (len(adivina) == len(palabra_oculta)) and (adivina in set_palabras_validas)


def mostrar_resultado_adivinar(palabra_oculta, adivina, dificultad):
    print(palabra_oculta)
    reps_letras = {}

    for letra in palabra_oculta:
        if letra not in reps_letras:
            reps_letras[letra] = palabra_oculta.count(letra)
            
    for indice in range(len(palabra_oculta)):
        if palabra_oculta[indice] == adivina[indice]:
            # resultado.append(f"\033[32m{palabra_oculta[indice]}\033[0m")
            tablero.celdas_de_letras[
                dificultad * (tablero.n_palabras_completadas - 1) + indice
            ].color = tablero.color_letra_correcta
            reps_letras[adivina[indice]] -= 1
   
        elif adivina[indice] in reps_letras and adivina.count(adivina[indice]) == reps_letras[adivina[indice]]:
            tablero.celdas_de_letras[
                dificultad * (tablero.n_palabras_completadas - 1) + indice
            ].color = tablero.color_letra_en_palabra
            reps_letras[adivina[indice]] -= 1
            


def comparar_palabras(palabra_valida, palabra_oculta, dificultad, tablero, ganados, perdidos):
   
    if palabra_valida == False:
        pass
        
    elif palabra_valida == palabra_oculta:
        tablero.resultado_juego = True
        ganados +=1
        

    elif palabra_valida != palabra_oculta and tablero.n_palabras_completadas == 6:
        tablero.resultado_juego = False
        perdidos +=1

    elif palabra_valida != palabra_oculta and tablero.n_palabras_completadas < 6:
        mostrar_resultado_adivinar(palabra_oculta, palabra_valida, dificultad)
    print(ganados, perdidos)
    return ganados, perdidos


if __name__ == "__main__":

    pygame.init()

    font = pygame.font.SysFont("Constantia", 32)

    cuadricula = Cuadricula()

    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))

    reloj = pygame.time.Clock()

    game_menu = True

    boton_inicio = Boton(260, 400, 2, texto="Empezar a jugar")
    
    seleccion_dificultad = BotonSeleccion(290, 300, 2, 5, "4", "5", "6", "7", "8")

    juegos_perdidos = 0
    juegos_ganados = 0

    teclas_qwerty = [
        ("Q", 50, 450),
        ("W", 110, 450),
        ("E", 170, 450),
        ("R", 230, 450),
        ("T", 290, 450),
        ("Y", 350, 450),
        ("U", 410, 450),
        ("I", 470, 450),
        ("O", 530, 450),
        ("P", 590, 450),
        ("A", 80, 510),
        ("S", 140, 510),
        ("D", 200, 510),
        ("F", 260, 510),
        ("G", 320, 510),
        ("H", 380, 510),
        ("J", 440, 510),
        ("K", 500, 510),
        ("L", 560, 510),
        ("Ñ", 620, 510),  # Añadir la letra "Ñ"
        ("Z", 110, 570),
        ("X", 170, 570),
        ("C", 230, 570),
        ("V", 290, 570),
        ("B", 350, 570),
        ("N", 410, 570),
        ("M", 470, 570),
        ("Borrar", 660, 450),
        ("Enter", 530, 570),
    ]

    BLANCO = (255, 255, 255)
    AZUL = (70, 130, 180)  # Color azul acero
    AZUL_CLARO = (100, 160, 210)  # Color azul claro al presionar la tecla

    # Crear un diccionario para almacenar los colores de cada tecla
    colores_teclas = {tecla: AZUL for tecla, _, _ in teclas_qwerty}

    dificultad = None

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        # Ciclo principal del juego
        for evento in pygame.event.get():
            # Salir del juego
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not game_menu  and tablero.resultado_juego == None:
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    # Botón izquierdo del ratón
                    for tecla, x, y in teclas_qwerty:
                        rect = pygame.Rect(x, y - 100, 60, 60)
                        if rect.collidepoint(evento.pos):
                            if tecla == "Borrar":
                                tablero.eliminar_letra()  # Eliminar letra del tablero
                                colores_teclas[tecla] = AZUL_CLARO
                            elif tecla == "Enter":
                                palabra_valida = tablero.confirmar_palabra()
                                juegos_ganados, juegos_perdidos = comparar_palabras(
                                    palabra_valida,
                                    palabra_oculta,
                                    int(dificultad),
                                    tablero,
                                    juegos_ganados,
                                    juegos_perdidos
                                )
                                cuadricula.color = cuadricula.color_incorrecto if palabra_valida == False else cuadricula.color_correcto
                            else:
                                colores_teclas[tecla] = AZUL_CLARO
                                tablero.agregar_letra(tecla)

                elif evento.type == pygame.KEYDOWN  and tablero.resultado_juego == None:
                    tecla = pygame.key.name(evento.key)
                    if len(tecla) == 1 and tecla.isalpha():
                        tablero.agregar_letra(tecla.upper())
                    elif evento.key == K_BACKSPACE:
                        tablero.eliminar_letra()
                    elif evento.key == K_RETURN:
                        palabra_valida = tablero.confirmar_palabra()
                        juegos_ganados, juegos_perdidos = comparar_palabras(
                            palabra_valida, palabra_oculta, int(dificultad), tablero, juegos_ganados, juegos_perdidos
                        )
                        cuadricula.color = cuadricula.color_incorrecto if palabra_valida == False else cuadricula.color_correcto

        # fondo de pantalla
        pantalla.fill(cuadricula.color)
        cuadricula.color = cuadricula.color_defecto

        if game_menu:
            # Si se da al botón de empezar, se inicia el juego

            # Titulo
            texto = font.render("GUORDEL", True, (0, 0, 0))
            textoRect = texto.get_rect()
            textoRect.topleft = (290, 200)
            pantalla.blit(texto, textoRect)

            dificultad = seleccion_dificultad.draw(pantalla, dificultad)

            if boton_inicio.draw(pantalla):
                game_menu = False
                tablero = TableroPalabras(
                    x=cuadricula.ancho // 4, y=50, escala=2, longitud_palabra=dificultad
                )
                
                palabra_oculta = get_palabra_random(int(dificultad))
              

        if not game_menu:
       
            tablero.dibujar_tablero(pantalla, True)

            for tecla, x, y in teclas_qwerty:
                if tecla == "Borrar":
                    rect = pygame.Rect(x - 5, y - 100, 70, 50)
                elif tecla == "Enter":
                    rect = pygame.Rect(x - 5, y - 100, 70, 50)
                else:
                    rect = pygame.Rect(x, y - 100, 50, 50)
                color = colores_teclas[tecla]
                pygame.draw.rect(pantalla, color, rect, border_radius=8)
                fuente = pygame.font.SysFont("calibri", 26)
                texto = fuente.render(tecla, True, BLANCO)
                text_rect = texto.get_rect(center=(rect.centerx, rect.centery))
                pantalla.blit(texto, text_rect)
            if (pygame.mouse.get_pressed()[0] == 0):  
            # Si no se está presionando el botón izquierdo
                for tecla in colores_teclas:
                    colores_teclas[tecla] = AZUL

            if tablero.resultado_juego == True:
                rect = Rect(200, 200, 400, 200)
                pygame.draw.rect(pantalla, (0, 0, 0), rect, border_radius=3)
                fuente = pygame.font.SysFont("calibri", 26)
                
                info_partida = f"GANASTE\nPartidas ganadas: {juegos_ganados}\nPartidas perdidas: {juegos_perdidos}\nIntentos fallidos: {tablero.n_palabras_completadas-1}"
                info_partida = info_partida.split("\n")
                renglon = 0
                for frase in info_partida:
                    texto = fuente.render(frase, True, BLANCO)
                    text_rect = texto.get_rect(center=(rect.centerx, rect.centery - 40 + renglon))
                    pantalla.blit(texto, text_rect)
                    renglon += 25
                
                

                boton_reinicio = Boton(300, 350, 2, texto="Volver a jugar")
                if boton_reinicio.draw(pantalla):
                    game_menu = True
            
            if tablero.resultado_juego == False:
                rect = Rect(200, 200, 400, 200)
                pygame.draw.rect(pantalla, (0, 0, 0), rect, border_radius=3)
                fuente = pygame.font.SysFont("calibri", 26)
                info_partida = f"PERDISTE\nPalabra correcta: {palabra_oculta}\nPartidas ganadas: {juegos_ganados}\nPartidas perdidas: {juegos_perdidos}"
                info_partida = info_partida.split("\n")
                renglon = 0
                for frase in info_partida:
                    texto = fuente.render(frase, True, BLANCO)
                    text_rect = texto.get_rect(center=(rect.centerx, rect.centery - 40 + renglon))
                    pantalla.blit(texto, text_rect)
                    renglon += 25
                

                boton_reinicio = Boton(300, 350, 2, texto="Volver a jugar")
                if boton_reinicio.draw(pantalla):
                    game_menu = True

        pygame.display.update()

        reloj.tick(9)
