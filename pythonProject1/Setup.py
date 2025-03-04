# ==============================================================================
# IMPORTACIÓN DEL MÓDULO TURTLE
# ==============================================================================
from turtle import Turtle


# ==============================================================================
# CLASE ESCENARIO
# ==============================================================================
class Escenario(Turtle):

    # ------------------------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE ESCENARIO
    # ------------------------------------------------------------------------------
    def __init__(self):
        """
        Inicializa el objeto Escenario configurando la tortuga para dibujar.
        """
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()
        self.speed(500)
        self.orientacion_offset = 0

    # ------------------------------------------------------------------------------
    # MÉTODO: set_orientacion_offset
    # ------------------------------------------------------------------------------
    def set_orientacion_offset(self, angulo):
        """
        Establece el offset de orientación para ajustar la dirección.

        Parámetros:
          angulo -- Ángulo de offset a aplicar.
        """
        self.orientacion_offset = angulo

    # ------------------------------------------------------------------------------
    # MÉTODO: setheading
    # ------------------------------------------------------------------------------
    def setheading(self, angle):
        """
        Ajusta la dirección de la tortuga sumando el offset de orientación.

        Parámetros:
          angle -- Ángulo base para la dirección.
        """
        super().setheading(angle + self.orientacion_offset)

    # ------------------------------------------------------------------------------
    # MÉTODO: carcel
    # ------------------------------------------------------------------------------
    def carcel(self):
        """
        Dibuja la cárcel en el tablero posicionándose en (-200, -200) y
        dibujando cuatro cuadrados con colores y rellenos diferentes.
        """
        self.goto(-200, -200)
        self.pendown()
        self.cuadrado(0, "#0077b6", "#ade8f4")
        self.cuadrado(90, "#800f2f", "#ffccd5")
        self.cuadrado(90, "#805b10", "orange")
        self.cuadrado(90, "#155d27", "#92e6a7")

    # ------------------------------------------------------------------------------
    # MÉTODO: cuadrado
    # ------------------------------------------------------------------------------
    def cuadrado(self, angulo, color, color_relleno):
        """
        Dibuja un cuadrado rellenado y avanza 360 unidades.

        Parámetros:
          angulo        -- Ángulo inicial de rotación.
          color         -- Color del borde.
          color_relleno -- Color de relleno del cuadrado.
        """
        self.left(angulo)
        self.color(color)
        self.fillcolor(color_relleno)
        self.begin_fill()
        for i in range(4):
            self.forward(105)
            self.left(90)
        self.end_fill()
        self.color("Black")
        self.forward(360)

    # ------------------------------------------------------------------------------
    # MÉTODO: casillas
    # ------------------------------------------------------------------------------
    def casillas(self, varx1, varx2, varx3, vary1, vary2, vary3, cor1, cor2):
        """
        Dibuja tres casillas de distintos tipos:
          - Casilla normal (varx1, vary1) con color cor1.
          - Casilla de llegada (varx2, vary2) con color cor2.
          - Otra casilla normal (varx3, vary3) con color cor2.
        """
        self.casillas_tipo_normal(varx1, vary1, cor1)
        self.casillas_tipo_llegada(varx2, vary2, cor2)
        self.casillas_tipo_normal(varx3, vary3, cor2)

    # ------------------------------------------------------------------------------
    # MÉTODO: casillas_tipo_normal
    # ------------------------------------------------------------------------------
    def casillas_tipo_normal(self, x_pos, y_pos, color_relleno):
        """
        Dibuja casillas normales en una posición dada.

        Parámetros:
          x_pos         -- Posición x inicial.
          y_pos         -- Posición y inicial.
          color_relleno -- Color de relleno para la casilla central.
        """
        self.penup()
        self.goto(x_pos, y_pos)
        self.pendown()
        for i in range(7):
            if i == 4:
                self.fillcolor(color_relleno)
                self.begin_fill()
                self.caja()
                self.devolver()
                self.end_fill()
            else:
                self.caja()
                self.devolver()

    # ------------------------------------------------------------------------------
    # MÉTODO: caja
    # ------------------------------------------------------------------------------
    def caja(self):
        """
        Dibuja una caja simple (dos lados) para formar parte de una casilla.
        """
        for j in range(2):
            self.forward(50)
            self.left(90)
            self.forward(15)
            self.left(90)

    # ------------------------------------------------------------------------------
    # MÉTODO: caja_final
    # ------------------------------------------------------------------------------
    def caja_final(self):
        """
        Dibuja la caja final con dimensiones invertidas.
        """
        for j in range(2):
            self.forward(15)
            self.left(90)
            self.forward(50)
            self.left(90)

    # ------------------------------------------------------------------------------
    # MÉTODO: devolver
    # ------------------------------------------------------------------------------
    def devolver(self):
        """
        Realiza el movimiento para retornar una casilla:
        gira 90°, avanza 15 y gira -90°.
        """
        self.left(90)
        self.forward(15)
        self.right(90)

    # ------------------------------------------------------------------------------
    # MÉTODO: casillas_tipo_llegada
    # ------------------------------------------------------------------------------
    def casillas_tipo_llegada(self, x_pos, y_pos, color_relleno):
        """
        Dibuja una casilla de llegada con relleno.

        Parámetros:
          x_pos         -- Posición x.
          y_pos         -- Posición y.
          color_relleno -- Color de relleno.
        """
        self.penup()
        self.goto(x_pos, y_pos)
        self.pendown()
        self.fillcolor(color_relleno)
        self.begin_fill()
        for i in range(8):
            self.caja()
            self.devolver()
        self.end_fill()

    # ------------------------------------------------------------------------------
    # MÉTODO: centro
    # ------------------------------------------------------------------------------
    def centro(self, x_pos, y_pos, ang, color):
        """
        Dibuja la zona central de una sección del tablero.

        Parámetros:
          x_pos -- Posición x del centro.
          y_pos -- Posición y del centro.
          ang   -- Ángulo de orientación para el centro.
          color -- Color de relleno del centro.
        """
        self.set_orientacion_offset(angulo=ang)
        self.penup()
        self.goto(x_pos, y_pos)
        self.pendown()
        self.fillcolor(color)
        self.begin_fill()
        self.setheading(315)
        self.forward(105)
        self.setheading(225)
        self.forward(105)
        self.penup()
        self.back(22.5)
        self.setheading(90)
        self.pendown()
        self.forward(119.5)
        self.end_fill()

    # ------------------------------------------------------------------------------
    # MÉTODO: numeros
    # ------------------------------------------------------------------------------
    def numeros(self):
        """
        Escribe los números en el tablero distribuidos en varios segmentos,
        asignando números y etiquetas especiales a cada casilla.
        """
        self.penup()
        cordenada = 15
        count = 1
        count_especial_roja = 1
        count_especial_verde = 1
        count_especial_amarilla = 1
        count_especial_azul = 1
        corx1 = -197.5
        cory1 = -95
        corx2 = 42.5
        cory2 = 40

        # --------------------------------------------------------------------------
        # Segmento A (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(270)
            self.goto(corx1, -70)
            self.write(f"{str(count).zfill(2)}", font=("Arial", 8, "normal"))
            count += 1
            corx1 += cordenada

        # --------------------------------------------------------------------------
        # Segmento B (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(90)
            self.goto(-70, cory1)
            self.write(f"{str(count).zfill(2)}", font=("Arial", 8, "normal"))
            count += 1
            cory1 -= cordenada

        # --------------------------------------------------------------------------
        # Casilla individual en Segmento B
        # --------------------------------------------------------------------------
        cory1 += cordenada
        self.goto(-25, cory1)
        self.write(f"{count}", font=("Arial", 8, "normal"))
        count += 1

        # --------------------------------------------------------------------------
        # Segmento especial en B (8 casillas)
        # --------------------------------------------------------------------------
        cory1_temp = cory1
        for i in range(8):
            self.setheading(90)
            cory1_temp += cordenada
            self.goto(-25, cory1_temp)
            print(f"{count}: (-25, {cory1_temp})")
            self.write(f"{str(count_especial_roja).zfill(2)}", font=("Arial", 8, "normal"))
            count_especial_roja += 1

        # --------------------------------------------------------------------------
        # Segmento D (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(180)
            self.goto(20, cory1)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            cory1 += cordenada

        # --------------------------------------------------------------------------
        # Segmento E (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(270)
            self.goto(corx2, -70)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            corx2 += cordenada

        # --------------------------------------------------------------------------
        # Casilla individual en Segmento E
        # --------------------------------------------------------------------------
        corx2 -= cordenada
        self.goto(corx2, -30)
        self.write(f"{count}", font=("Arial", 8, "normal"))
        count += 1

        # --------------------------------------------------------------------------
        # Segmento especial en E (8 casillas)
        # --------------------------------------------------------------------------
        corx2_temp = corx2
        for i in range(8):
            self.setheading(90)
            corx2_temp -= cordenada
            self.goto(corx2_temp, -30)
            print(f"{count}: ({corx2_temp}, -30 )")
            self.write(f"{str(count_especial_amarilla).zfill(2)}", font=("Arial", 8, "normal"))
            count_especial_amarilla += 1

        # --------------------------------------------------------------------------
        # Segmento G (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(270)
            self.goto(corx2, 15)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            corx2 -= cordenada

        # --------------------------------------------------------------------------
        # Segmento H (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(270)
            self.goto(20, cory2)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            cory2 += cordenada

        # --------------------------------------------------------------------------
        # Casilla individual en Segmento H
        # --------------------------------------------------------------------------
        cory2 -= cordenada
        self.goto(-25, cory2)
        self.write(f"{count}", font=("Arial", 8, "normal"))
        count += 1

        # --------------------------------------------------------------------------
        # Segmento especial en H (8 casillas)
        # --------------------------------------------------------------------------
        cory2_temp = cory2
        for i in range(8):
            self.setheading(90)
            cory2_temp -= cordenada
            self.goto(-25, cory2_temp)
            print(f"{count}: (-25, {cory2_temp})")
            self.write(f"{str(count_especial_verde).zfill(2)}", font=("Arial", 8, "normal"))
            count_especial_verde += 1

        # --------------------------------------------------------------------------
        # Segmento J (8 casillas)
        # --------------------------------------------------------------------------
        for i in range(8):
            self.setheading(180)
            self.goto(-70, cory2)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            cory2 -= cordenada

        # --------------------------------------------------------------------------
        # Ajuste para Segmento K
        # --------------------------------------------------------------------------
        corx1 -= cordenada
        for i in range(8):
            self.setheading(180)
            self.goto(corx1, 15)
            self.write(f"{count}", font=("Arial", 8, "normal"))
            count += 1
            corx1 -= cordenada

        # --------------------------------------------------------------------------
        # Casilla individual final en Segmento K
        # --------------------------------------------------------------------------
        corx1 += cordenada
        self.goto(corx1, -30)
        self.write(f"{count}", font=("Arial", 8, "normal"))
        count += 1

        # --------------------------------------------------------------------------
        # Segmento especial en K (8 casillas)
        # --------------------------------------------------------------------------
        corx1_temp = corx1
        for i in range(8):
            self.setheading(90)
            corx1_temp += cordenada
            self.goto(corx1_temp, -30)
            print(f"{count}: ({corx1_temp}, 30)")
            self.write(f"{str(count_especial_azul).zfill(2)}", font=("Arial", 8, "normal"))
            count_especial_azul += 1