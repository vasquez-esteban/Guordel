import pygame
from pygame.locals import *

pygame.init()

class TableroPalabras():
    color_texto = (0,0,0)
    color_celdas = (245, 233, 233)
    color_celdas_interior = (191, 215, 249)

    def __init__(self,x,y, escala, longitud_palabra):
        self.x = x
        self.y = y
        self.lado_cuadrado = 20*escala
        self.escala = escala
        self.longitud_palabra = int(longitud_palabra)
        inicio_en_x = x
        inicio_en_y = y

        self.celdas_de_letras = []
        
        for i in range(6):
            for j in range(self.longitud_palabra):
                self.celdas_de_letras.append(Rect(inicio_en_x, inicio_en_y, self.lado_cuadrado, self.lado_cuadrado))
                inicio_en_x += self.lado_cuadrado + 10
            inicio_en_x = x
            inicio_en_y += self.lado_cuadrado + 10
        
        self.palabras = [[], [], [], [], [], []]

        self.n_palabras_completadas = 0
        self.letras_en_palabra_activa = 0

    def dibujar_tablero (self, superficie, con_relleno):
        font = pygame.font.SysFont('Constantia', 12*self.escala)  
        indx_letra = 0
        indx_palabra = 0
        letras_por_completar = True
       
  

        for celda in self.celdas_de_letras:
            if con_relleno:
                pygame.draw.rect(superficie, self.color_celdas_interior, celda, 0, 2)
            pygame.draw.rect(superficie, self.color_celdas, celda, 2, 2)

            if indx_palabra < self.n_palabras_completadas :
                imagen_texto = font.render(self.palabras[indx_palabra][indx_letra], True, self.color_texto)
                superficie.blit(imagen_texto, (celda.x + celda.width // (2*self.escala), celda.y + celda.height // (2*self.escala)))
                if indx_letra == self.longitud_palabra-1:
                    indx_letra = 0
                    indx_palabra +=1
                    continue
                    
                else:
                    indx_letra += 1
            
            if indx_palabra == self.n_palabras_completadas and letras_por_completar:

                if indx_letra == len(self.palabras[indx_palabra]):
                    letras_por_completar = False
                    continue
                imagen_texto = font.render(self.palabras[indx_palabra][indx_letra], True, self.color_texto)
                superficie.blit(imagen_texto, (celda.x + celda.width // (2*self.escala), celda.y + celda.height // (2*self.escala)))
                indx_letra +=1
            
            

            
            
    
    def agregar_letra (self, letra):
        if len(self.palabras[self.n_palabras_completadas]) < self.longitud_palabra:
            self.palabras[self.n_palabras_completadas].append(letra)

    def eliminar_letra(self):
        if len(self.palabras[self.n_palabras_completadas]) != 0:
            self.palabras[self.n_palabras_completadas].pop()
          
    
    def confirmar_palabra(self):
        
        if len(self.palabras[self.n_palabras_completadas]) == self.longitud_palabra:
            self.n_palabras_completadas += 1
        else: 
            return False

        palabra = ""
        for letra in self.palabras[self.n_palabras_completadas - 1]:
            palabra += letra
        
        return palabra

        


            


        

            



