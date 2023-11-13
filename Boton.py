import pygame
from pygame.locals import *

pygame.init()


class Boton:

    #variables de la clase
    color_texto = (0,0,0)
    boton_no_presionado = (116, 111, 140)
    boton_hovered = (116, 111, 130)
    boton_presionado = (116, 101, 140)



#constructor -> args: se usa para agregar un tamaño especifico al botón (ingresa dos valores para ancho y después largo)
#constructor -> kwargs["imagen"]: si en el constructor escribes imagen= el botón va a ser la imagen que le agregues al parametro
#constructor -> kwargs["texto"]: si escribes texto= el botón va a contener el texto que le ingreses

    def __init__(self, x, y, escala,*args, **kwargs):
        """
        Crea un botón interactivo en una ventana de Pygame
        con posición inicial (x, y) y redimensionamiento (escala)
        """
        self.x = x
        self.y = y
        
        # Para manejar el evento de un click
        self.presionado = False
        self.escala = escala
        
        self.color_de_boton = self.boton_no_presionado

        if "imagen" in kwargs:
            ancho = imagen.get_width()
            altura = imagen.get_height()
            self.imagen = pygame.transform.scale(kwargs["imagen"], (int(ancho * escala), int(altura * escala)))
            self.rect = self.imagen.get_rect()
            self.rect.topleft = (x, y)
        else: 
            self.imagen = False
        #Este fue mi intento de que se viera bien con palabras cortas y largas, medio funciona
        if "texto" in kwargs:
            self.ancho = args[0] if args else len(kwargs["texto"])*8*escala + 8/len(kwargs["texto"])
            self.altura = args[1] if args else 20*escala
            self.texto = kwargs["texto"]
            self.rect = Rect(x,y, self.ancho, self.altura)
        else:
            self.imagen = False
        
        


    

        

    def draw(self, surface):
        """Dibuja el botón en una superficie y maneja eventos de clic."""

        # La variable acción sirve para borrar el botón e iniciar el juego
        accion = False

        font = pygame.font.SysFont('Constantia', 12*self.escala)  

        # Lógica para manejar clicks sobre el botón
        pos = pygame.mouse.get_pos()

        

        # Si el botón es presionado dentro de su rectángulo, inicia el juego
        if self.rect.collidepoint(pos):
            self.color_de_boton = self.boton_hovered
            if pygame.mouse.get_pressed()[0] == 1 and not self.presionado:
                
                self.presionado = True
                accion = True
                
        else:
            self.color_de_boton = self.boton_no_presionado
        

        # Guardar eventos cuando no se presiona el botón
        if pygame.mouse.get_pressed()[0] == 0:
            self.presionado = False
            

        # Dibujar el botón y comenzar el juego si se cumple la lógica
        if self.imagen:
            surface.blit(self.imagen, (self.rect.x, self.rect.y))

        if self.texto:
            pygame.draw.rect(surface, self.color_de_boton, self.rect, 0, 3)
            imagen_texto = font.render(self.texto, True, self.color_texto)
            len_texto = imagen_texto.get_width()
            surface.blit(imagen_texto, (self.x + self.ancho*(1/7), self.y+self.altura*(1/8)))

        return accion