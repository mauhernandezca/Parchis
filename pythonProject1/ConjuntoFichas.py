# ==============================================================================
# IMPORTACIÓN DEL MÓDULO FICHA
# ==============================================================================
import Ficha


# ==============================================================================
# CLASE FICHAS
# ==============================================================================
class Fichas():

    # ------------------------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE FICHAS
    # ------------------------------------------------------------------------------
    def __init__(self, cordenadax1, cordenadax2, cordenaday1, cordenaday2, color_ficha):
        """
        Inicializa el conjunto de fichas creando las piezas en función de las coordenadas
        y el color especificado.

        Parámetros:
          cordenadax1   -- Coordenada x para la primera columna.
          cordenadax2   -- Coordenada x para la segunda columna.
          cordenaday1   -- Coordenada y para la primera fila.
          cordenaday2   -- Coordenada y para la segunda fila.
          color_ficha   -- Color de las fichas.
        """
        self.piezas = self.crear_fichas(xvar1=cordenadax1, xvar2=cordenadax2,
                                        yvar1=cordenaday1, yvar2=cordenaday2,
                                        color=color_ficha)

    # ------------------------------------------------------------------------------
    # MÉTODO: crear_fichas
    # ------------------------------------------------------------------------------
    def crear_fichas(self, xvar1, xvar2, yvar1, yvar2, color):
        """
        Crea y retorna una lista de cuatro fichas ubicadas en posiciones
        definidas por las coordenadas proporcionadas.

        Parámetros:
          xvar1  -- Coordenada x para la primera columna.
          xvar2  -- Coordenada x para la segunda columna.
          yvar1  -- Coordenada y para la primera fila.
          yvar2  -- Coordenada y para la segunda fila.
          color  -- Color de las fichas.

        Retorna:
          Una lista que contiene cuatro objetos Ficha.
        """
        ficha_1 = Ficha.Ficha(x_var=xvar1, y_var=yvar1, color=color)
        ficha_2 = Ficha.Ficha(x_var=xvar1, y_var=yvar2, color=color)
        ficha_3 = Ficha.Ficha(x_var=xvar2, y_var=yvar1, color=color)
        ficha_4 = Ficha.Ficha(x_var=xvar2, y_var=yvar2, color=color)
        return [ficha_1, ficha_2, ficha_3, ficha_4]