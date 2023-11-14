import pygame
from pygame.locals import *

pygame.init()

class Opcion:

    color_texto = (0,0,0)
    boton_no_presionado = (116, 111, 140)
    boton_hovered = (116, 111, 230)
    boton_presionado = (150, 101, 140)

    def __init__(self, meta_x, meta_y, ancho, altura, texto, rect):
        self.meta_x = meta_x
        self.meta_y = meta_y
        self.ancho = ancho
        self.altura = altura
        self.texto = texto
        self.rect = rect
        self.presionado = False
        self.color_de_boton = self.boton_no_presionado

class BotonSeleccion:

    #variables de la clase
    color_texto = (0,0,0)
   
#constructor -> args: hasta el valor cant_opciones va a ser el texto de cada boton
#constructor -> args: se usa para agregar un tamaño especifico al botón cant_opciones +1 y +2

#para este me dió pereza incluir la opción de una foto(muy complicada)

    def __init__(self, x, y, escala, cant_opciones, *args ):
        """
        Crea un botón interactivo en una ventana de Pygame
        con posición inicial (x, y) y redimensionamiento (escala)
        """
        self.x = x
        self.y = y
        
        # Para manejar el evento de un click
      
        self.escala = escala
        
        

        self.opciones = {}

        inicio = x
        for x in range(cant_opciones):
            texto = args[x]
            ancho = args[cant_opciones+1] if len(args)>cant_opciones else len(texto)*8*escala + 8/len(texto)
            altura = args[cant_opciones+2] if len(args)>cant_opciones else 20*escala
            self.opciones[texto] = Opcion(inicio, y, ancho, altura, texto, Rect(inicio, y, ancho, altura))
            inicio += ancho + 10
        
        
    def draw(self, surface, varObjetivo):
        """Dibuja el botón en una superficie y maneja eventos de clic."""

        # La variable acción sirve para borrar el botón e iniciar el juego
        accion = False

        font = pygame.font.SysFont('Constantia', 12*self.escala)  

        # Lógica para manejar clicks sobre el botón
        pos = pygame.mouse.get_pos()

        

        # Si una de las opciones es tocada por el cursor, cambia de color, si es presionado se cambia la dificultad 
        for opcion in self.opciones:
            objeto = self.opciones[opcion]
            if objeto.rect.collidepoint(pos):
                objeto.color_de_boton = objeto.boton_hovered
                if pygame.mouse.get_pressed()[0] == 1 and not objeto.presionado:
                    objeto.presionado = True
                    varObjetivo = opcion       
            else:
                objeto.color_de_boton = objeto.boton_no_presionado

            # Guardar eventos cuando no se presiona el botón
            if pygame.mouse.get_pressed()[0] == 0:
                objeto.presionado = False
    
    
        for boton in self.opciones:
            objeto = self.opciones[boton]
            #print(varObjetivo, boton)
            color_recuadro = objeto.color_de_boton if varObjetivo != boton else objeto.boton_presionado
            pygame.draw.rect(surface, color_recuadro, objeto.rect, 0, 3)
            imagen_texto = font.render(objeto.texto, True, objeto.color_texto)
            len_texto = imagen_texto.get_width()
            surface.blit(imagen_texto, (objeto.meta_x + objeto.ancho*(1/7), objeto.meta_y + objeto.altura*(1/8)))
        return varObjetivo

       