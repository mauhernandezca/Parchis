# ==============================================================================
# IMPORTACIÓN DE MÓDULOS
# ==============================================================================
import turtle
import Boton
import Setup
import ConjuntoFichas
import coordenadas


# ==============================================================================
# CREACIÓN DE LA PANTALLA Y CONFIGURACIÓN INICIAL
# ==============================================================================
screen = turtle.Screen()
screen.title("Parques")
screen.setup(width=800, height=600)


# ==============================================================================
# CREACIÓN DEL ESCENARIO Y DIBUJO DEL TABLERO
# ==============================================================================
escenario = Setup.Escenario()

# Dibuja la cárcel
escenario.carcel()
escenario.penup()

# Dibuja las casillas en la parte superior
escenario.casillas(varx1=-200, varx2=-200, varx3=-200, vary1=55, vary2=5, vary3=-45, cor1="#92e6a7", cor2="#ade8f4")
escenario.right(270)

# Dibuja las casillas en la parte izquierda
escenario.casillas(varx1=-95, varx2=-45, varx3=5, vary1=-200, vary2=-200, vary3=-200, cor1="#ade8f4", cor2="#ffccd5")
escenario.right(270)

# Dibuja las casillas en la parte inferior
escenario.casillas(varx1=160, varx2=160, varx3=160, vary1=-95, vary2=-45, vary3=5, cor1="#ffccd5", cor2="orange")
escenario.right(270)

# Dibuja las casillas en la parte derecha
escenario.casillas(varx1=55, varx2=5, varx3=-45, vary1=160, vary2=160, vary3=160, cor1="orange", cor2="#92e6a7")

# Dibuja los centros de las zonas y los números
escenario.centro(x_pos=-95, y_pos=55, ang=0, color="#ade8f4")
escenario.centro(x_pos=-95, y_pos=-95, ang=90, color="#ffccd5")
escenario.centro(x_pos=55, y_pos=-95, ang=180, color="orange")
escenario.centro(x_pos=55, y_pos=55, ang=270, color="#92e6a7")
escenario.numeros()


# ==============================================================================
# CREACIÓN DE LAS FICHAS DE LOS JUGADORES
# ==============================================================================
PiezasAzules = ConjuntoFichas.Fichas(cordenadax1=-167.5, cordenadax2=-127.5, cordenaday1=-127.5, cordenaday2=-167.5, color_ficha="blue")
PiezasRojas = ConjuntoFichas.Fichas(cordenadax1=87.5, cordenadax2=127.5, cordenaday1=-127.5, cordenaday2=-167.5, color_ficha="red")
PiezasAmarillas = ConjuntoFichas.Fichas(cordenadax1=87.5, cordenadax2=127.5, cordenaday1=87.5, cordenaday2=127.5, color_ficha="gold")
PiezasVerdes = ConjuntoFichas.Fichas(cordenadax1=-167.5, cordenadax2=-127.5, cordenaday1=87.5, cordenaday2=127.5, color_ficha="green")


# ==============================================================================
# ASIGNACIÓN DE FICHAS A CADA JUGADOR
# ==============================================================================
fichas_jugador = {
    "blue": PiezasAzules,
    "red": PiezasRojas,
    "gold": PiezasAmarillas,
    "green": PiezasVerdes
}


# ==============================================================================
# CREACIÓN DEL BOTÓN DE INTERACCIÓN
# ==============================================================================
boton = Boton.Boton(screen, fichas_jugador)


# ==============================================================================
# MANTENER LA VENTANA ABIERTA
# ==============================================================================
screen.mainloop()