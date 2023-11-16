class Cuadricula:
    """Define el la cuadricula 13 x 13 con celdas de 50 x 50 pixeles"""

    def __init__(self):
        """Guardar tamaños fijos que representan la cuadrícula"""
        self.tamano_celdas = 40
        self.cantidad_celdas_ancho = 20
        self.cantidad_celdas_largo = 15

        self.ancho = self.tamano_celdas * self.cantidad_celdas_ancho
        self.largo = self.tamano_celdas * self.cantidad_celdas_largo
        self.color = (103, 97, 128)
