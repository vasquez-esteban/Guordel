# Archivo para definir los atributos y métodos de una instancia del juego
# La interfaz debe mostrar la cantidad de aciertos y fallos cada partida

class Guordel:
    def __init__(self, dificultad):
        """La dificultad es un entero entre 4 y 8 (cantidad de letras)"""
        self.dificultad = dificultad
        self.aciertos = 0
        self.fallos = 0
        self.intentos = 6
        self.adivino_palabra = False

        self.palabras_validas = set()
        self.palabras_escogidas = set()
        self.palabra_oculta = None

    def nueva_ronda(self, dificultad):
        self.dificultad = dificultad
        self.aciertos = 0
        self.fallos = 0
        self.intentos = 6
        self.adivino_palabra = False
        self.set_palabra_oculta(self.palabras_escogidas)

    def set_palabra_oculta(self, lista_palabras_posibles):
        """Selecciona una palabra aleatoria de self.palabras_escogidas"""
        pass
