# ==============================================================================
# IMPORTACIÓN DEL MÓDULO TURRET
# ==============================================================================
from turtle import Turtle


# ==============================================================================
# CLASE FICHA
# ==============================================================================
class Ficha(Turtle):

    # ------------------------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE FICHA
    # ------------------------------------------------------------------------------
    def __init__(self, x_var, y_var, color):
        """
        Inicializa una ficha con la posición inicial, color y estado en cárcel.

        Parámetros:
          x_var -- Coordenada x inicial de la ficha.
          y_var -- Coordenada y inicial de la ficha.
          color -- Color (y propietario) de la ficha.
        """
        super().__init__()

        # Asigna el color y propietario de la ficha.
        self.propietario = color

        # Configuración visual de la ficha.
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.shape("circle")
        self.goto(x_var, y_var)
        self.speed(10)

        # Inicializa el índice de la casilla y estado de cárcel.
        self.pos_index = 0
        self.jail_coord = (x_var, y_var)
        self.en_carcel = True

    # ------------------------------------------------------------------------------
    # MÉTODO: volver_a_carcel
    # ------------------------------------------------------------------------------
    def volver_a_carcel(self):
        """
        Retorna la ficha a su posición de cárcel.

        Reinicia el índice de la casilla y mueve la ficha a la coordenada
        original almacenada en jail_coord.
        """
        self.pos_index = 0
        self.goto(self.jail_coord)