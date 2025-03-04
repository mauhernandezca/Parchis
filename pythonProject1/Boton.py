# ==============================================================================
# IMPORTACIONES
# ==============================================================================
from turtle import Turtle
from coordenadas import coordenadas, paths, full_paths
import random


# ==============================================================================
# FUNCIÓN: validar_entrada
# ==============================================================================
def validar_entrada(numero, valores_validos):
    """
    Verifica si el número ingresado es válido.

    Parámetros:
      numero          -- Número a validar.
      valores_validos -- Conjunto de valores permitidos.

    Retorna:
      True si el número es válido, False en caso contrario.
    """
    return numero in valores_validos


# ==============================================================================
# CLASE BOTON
# ==============================================================================
class Boton(Turtle):

    # ------------------------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE BOTON
    # ------------------------------------------------------------------------------
    def __init__(self, screen, fichas_jugador, x=-70, y=200, width=100, height=30, text="¡Lanza!"):
        """
        Inicializa el botón para interactuar en el juego.

        Parámetros:
          screen          -- Pantalla de Turtle.
          fichas_jugador  -- Diccionario que asocia el color del jugador con su objeto Fichas.
          x, y            -- Coordenadas iniciales del botón.
          width, height   -- Dimensiones del botón.
          text            -- Texto a mostrar en el botón.

        Se asume que cuando una ficha está en la cárcel, su atributo 'en_carcel' es True.
        """
        super().__init__()
        self.screen = screen
        self.fichas_jugador = fichas_jugador
        self.hideturtle()
        self.penup()
        self.block_markers = {}

        # Configuración del botón
        self.x_min = x
        self.x_max = x + width
        self.y_min = y
        self.y_max = y + height

        # Turtles para mensajes
        self.tiro_texto = Turtle()
        self.tiro_texto.hideturtle()
        self.tiro_texto.penup()
        self.error_texto = Turtle()
        self.error_texto.hideturtle()
        self.error_texto.penup()

        # Dibujar el botón
        self.goto(self.x_min, self.y_min)
        self.pendown()
        self.color("black", "lightblue")
        self.begin_fill()
        for _ in range(2):
            self.forward(width)
            self.left(90)
            self.forward(height)
            self.left(90)
        self.end_fill()
        self.penup()

        # Mostrar el texto en el botón
        self.goto(self.x_min + 25, self.y_min + 5)
        self.color("black")
        self.write(text, font=("Arial", 12, "bold"))

        # Turtles para mostrar dados y turno
        self.dado_1_cuadro = Turtle()
        self.dado_1_cuadro.speed(500)
        self.dado_2_cuadro = Turtle()
        self.dado_2_cuadro.speed(500)
        self.dado_1_texto = Turtle()
        self.dado_1_texto.speed(500)
        self.dado_2_texto = Turtle()
        self.dado_2_texto.speed(500)
        self.jugador_texto = Turtle()
        self.jugador_texto.speed(500)

        for objeto in (self.dado_1_cuadro, self.dado_2_cuadro,
                       self.dado_1_texto, self.dado_2_texto, self.jugador_texto):
            objeto.hideturtle()
            objeto.penup()

        # Definir los jugadores (Nombre, Color)
        self.jugadores = [
            ("Azul", "blue"),
            ("Rojo", "red"),
            ("Amarillo", "gold"),
            ("Verde", "green")
        ]
        self.colores = ["red", "blue", "green", "purple", "orange", "brown"]

        self.jugador_actual = 0
        self.pares_consecutivos = 0
        self.ultima_ficha_movida = None

        # Configuración del modo de juego: desarrollador o normal, y modo dados vs. manual
        self.modo_desarrollador = False
        self.dice_mode = True
        self.manual_moves = []

        # Contador de intentos para salir de la cárcel
        self.jail_attempts = 0

        self.elegir_modo()
        self.mostrar_jugador_actual()

        # Asigna el evento de clic a la pantalla
        self.screen.onclick(self.detectar_clic)

    # ------------------------------------------------------------------------------
    # MÉTODO: elegir_modo
    # ------------------------------------------------------------------------------
    def elegir_modo(self):
        """
        Permite al usuario seleccionar el modo desarrollador.
        """
        resp = self.screen.textinput("Modo de juego", "¿Desea activar modo desarrollador? (s/n)")
        if resp and resp.lower() == 's':
            self.modo_desarrollador = True
            print("Modo desarrollador activado.")
        else:
            self.modo_desarrollador = False

    # ------------------------------------------------------------------------------
    # MÉTODO: detectar_clic
    # ------------------------------------------------------------------------------
    def detectar_clic(self, x, y):
        """
        Detecta clics en la pantalla y ejecuta la acción del botón si se hace clic en su área.

        Parámetros:
          x, y -- Coordenadas del clic.
        """
        if self.x_min < x < self.x_max and self.y_min < y < self.y_max:
            if self.modo_desarrollador:
                choice = self.screen.textinput("Modo desarrollador",
                                               "¿Desea ingresar movimiento manual (m) o tirar dados (d)?")
                if choice:
                    choice = choice.lower()
                    if choice == "m":
                        self.dice_mode = False
                        self.solicitar_movimiento_manual()
                    elif choice == "d":
                        self.dice_mode = True
                        self.lanzar_dados_normal()
                    else:
                        self.mostrar_error("Entrada no válida. Presiona 'm' o 'd'.")
            else:
                self.lanzar_dados()

    # ------------------------------------------------------------------------------
    # MÉTODO: lanzar_dados_normal
    # ------------------------------------------------------------------------------
    def lanzar_dados_normal(self):
        """
        Reinicia el modo manual y lanza los dados en modo normal.
        """
        self.manual_moves = []
        self.dice_mode = True
        self.lanzar_dados()

    # ------------------------------------------------------------------------------
    # MÉTODO: solicitar_movimiento_manual
    # ------------------------------------------------------------------------------
    def solicitar_movimiento_manual(self):
        """
        Solicita al usuario el movimiento manual para mover las fichas.
        """
        move1 = self.screen.numinput("Movimiento manual", "Ingrese movimiento para la primera ficha (1 a 12):",
                                     minval=1, maxval=12)
        if move1 is None:
            self.mostrar_error("Movimiento cancelado.")
            return
        move1 = int(move1)
        if move1 == 12:
            self.manual_moves = [12]
            self.pares_consecutivos = 0
        else:
            use_second = self.screen.textinput("Movimiento manual",
                                               "¿Desea ingresar movimiento para segunda ficha? (s/n)")
            if use_second and use_second.lower() == "s":
                max_second = 12 - move1
                if max_second < 1:
                    self.manual_moves = [move1]
                    self.pares_consecutivos = 0
                else:
                    move2 = self.screen.numinput("Movimiento manual",
                                                 f"Ingrese movimiento para la segunda ficha (1 a {max_second}):",
                                                 minval=1, maxval=max_second)
                    if move2 is None:
                        self.manual_moves = [move1]
                        self.pares_consecutivos = 0
                    else:
                        move2 = int(move2)
                        self.manual_moves = [move1, move2]
                        if move1 == move2:
                            self.pares_consecutivos += 1
                        else:
                            self.pares_consecutivos = 0
            else:
                self.manual_moves = [move1]
                self.pares_consecutivos = 0
        self.movimiento = int(self.manual_moves.pop(0))
        self.mostrar_tiro_actual(
            f"Movimiento manual: {self.movimiento}. Selecciona una ficha a mover (color: {self.jugadores[self.jugador_actual][1]})")
        self.seleccionar_ficha()

    # ------------------------------------------------------------------------------
    # MÉTODO: lanzar_dados
    # ------------------------------------------------------------------------------
    def lanzar_dados(self):
        """
        Lanza dos dados y muestra sus resultados, además de gestionar la extracción de fichas en la cárcel.
        """
        self.mostrar_jugador_actual()
        self.dado_1_valor = random.randint(1, 6)
        self.dado_2_valor = random.randint(1, 6)

        # Posicionar la tortuga para mostrar los resultados
        self.goto(-200, 205)
        print(f"{self.jugadores[self.jugador_actual][0]} lanzó: {self.dado_1_valor}, {self.dado_2_valor}")

        if self.dado_1_valor == self.dado_2_valor:
            self.pares_consecutivos += 1
        else:
            self.pares_consecutivos = 0

        self.usado1 = False
        self.usado2 = False

        color_1 = self.colores[self.dado_1_valor - 1]
        color_2 = self.colores[self.dado_2_valor - 1]
        dado_1_x = self.x_min - 55
        dado_2_x = self.x_max + 25
        dado_y = self.y_min

        self.dibujar_cuadro(self.dado_1_cuadro, dado_1_x, dado_y, color_1)
        self.dibujar_cuadro(self.dado_2_cuadro, dado_2_x, dado_y, color_2)
        self.mostrar_texto(self.dado_1_texto, dado_1_x + 10, dado_y + 5, self.dado_1_valor, "white")
        self.mostrar_texto(self.dado_2_texto, dado_2_x + 10, dado_y + 5, self.dado_2_valor, "white")

        # ------------------------------------------------------------------------------
        # Verificación de fichas en la cárcel
        # ------------------------------------------------------------------------------
        current_color = self.jugadores[self.jugador_actual][1]
        pieces_in_jail = [ficha for ficha in self.fichas_jugador[current_color].piezas if
                          hasattr(ficha, "en_carcel") and ficha.en_carcel]
        pieces_not_in_jail = [ficha for ficha in self.fichas_jugador[current_color].piezas if
                              not (hasattr(ficha, "en_carcel") and ficha.en_carcel)]

        # Si se saca un 5 (por dado individual o suma) se extraen fichas de la cárcel.
        if pieces_in_jail and (
                self.dado_1_valor == 5 or self.dado_2_valor == 5 or (self.dado_1_valor + self.dado_2_valor) == 5):
            self.mostrar_tiro_actual("¡Se obtuvo un 5! Se usará para extraer fichas de la cárcel.")
            self.extraer_de_carcel(current_color, pieces_in_jail)
            self.dado_1_cuadro.clear()
            self.dado_1_texto.clear()
            self.dado_2_cuadro.clear()
            self.dado_2_texto.clear()
            self.jail_attempts = 0
            self.solicitar_entrada()
            return

        # Si todas las fichas están en la cárcel y no se extrajo, se usan intentos.
        if len(pieces_not_in_jail) == 0 and pieces_in_jail:
            self.jail_attempts += 1
            if self.jail_attempts < 3:
                self.goto(-200, -250)
                self.mostrar_error(f"Intento {self.jail_attempts} de 3: No se obtuvo un 5 para salir de la cárcel.")
                self.screen.ontimer(self.lanzar_dados, 1000)
                return
            else:
                self.mostrar_error("Tres intentos fallidos para salir de la cárcel. Turno descartado.")
                self.finalizar_turno()
                return

        # Si hay al menos una ficha fuera de la cárcel, se permite mover.
        self.solicitar_entrada()

    # ------------------------------------------------------------------------------
    # MÉTODO: extraer_de_carcel
    # ------------------------------------------------------------------------------
    def extraer_de_carcel(self, current_color, pieces_in_jail):
        """
        Extrae fichas de la cárcel utilizando el valor 5.

        - Extrae como máximo 2 fichas, o 1 si ya hay una ficha aliada en la posición inicial.
        - Captura fichas enemigas en la posición inicial.

        Parámetros:
          current_color  -- Color del jugador actual.
          pieces_in_jail -- Lista de fichas en la cárcel.
        """
        starting_coord = paths[current_color][0]
        allied_here = [p for p in self.get_pieces_on_square(starting_coord) if p.propietario == current_color]
        allowed_extraction = 1 if allied_here else 2
        num_to_extract = min(allowed_extraction, len(pieces_in_jail))
        enemy_here = [p for p in self.get_pieces_on_square(starting_coord) if p.propietario != current_color]
        for enemy in enemy_here:
            enemy.volver_a_carcel()
            print(f"{current_color} captura ficha enemiga en la posición inicial.")
        for i in range(num_to_extract):
            ficha = pieces_in_jail[i]
            ficha.pos_index = 0
            ficha.goto(starting_coord)
            ficha.en_carcel = False
            print(f"Ficha de {current_color} extraída de la cárcel.")

    # ------------------------------------------------------------------------------
    # MÉTODO: get_valid_moves
    # ------------------------------------------------------------------------------
    def get_valid_moves(self):
        """
        Retorna una lista de movimientos válidos basados en los valores de los dados.
        """
        if not self.usado1 and not self.usado2:
            return [self.dado_1_valor, self.dado_2_valor, self.dado_1_valor + self.dado_2_valor]
        elif not self.usado1:
            return [self.dado_1_valor]
        elif not self.usado2:
            return [self.dado_2_valor]
        else:
            return []

    # ------------------------------------------------------------------------------
    # MÉTODO: solicitar_entrada
    # ------------------------------------------------------------------------------
    def solicitar_entrada(self):
        """
        Solicita el movimiento al usuario, ya sea en modo dados o manual.
        """
        current_color = self.jugadores[self.jugador_actual][1]
        # Modo DADOS
        if self.dice_mode:
            if self.manual_moves:
                self.movimiento = int(self.manual_moves.pop(0))
                self.mostrar_tiro_actual(
                    f"Movimiento restante: {self.movimiento}. Selecciona una ficha a mover (color: {current_color})")
                self.seleccionar_ficha()
                return
            valid_moves = self.get_valid_moves()
            if not valid_moves:
                self.finalizar_turno()
                return
            prompt = f"Turno {self.jugadores[self.jugador_actual][0]}: Ingresa movimiento {valid_moves}"
            while True:
                entrada = self.screen.textinput("Movimiento", prompt)
                if entrada is None:
                    continue
                try:
                    move = int(entrada)
                    if move in valid_moves:
                        self.movimiento = move
                        break
                    else:
                        self.mostrar_error(f"Movimiento {move} no es válido. Permitidos: {valid_moves}")
                except ValueError:
                    self.mostrar_error(f"Entrada no válida. Permitidos: {valid_moves}")
            self.mostrar_tiro_actual(f"Selecciona una ficha a mover (color: {current_color})")
            self.seleccionar_ficha()
        # Modo MANUAL
        else:
            if self.manual_moves:
                self.movimiento = int(self.manual_moves.pop(0))
                pieces_in_jail = [f for f in self.fichas_jugador[current_color].piezas if
                                  hasattr(f, "en_carcel") and f.en_carcel]
                if pieces_in_jail and self.movimiento == 5:
                    self.mostrar_tiro_actual("¡Se obtuvo un 5! Se usará para extraer fichas de la cárcel.")
                    self.extraer_de_carcel(current_color, pieces_in_jail)
                    self.solicitar_entrada()
                    return
                else:
                    self.mostrar_tiro_actual(
                        f"Movimiento manual: {self.movimiento}. Selecciona una ficha a mover (color: {current_color})")
                    self.seleccionar_ficha()
            else:
                self.finalizar_turno()

    # ------------------------------------------------------------------------------
    # MÉTODO: seleccionar_ficha
    # ------------------------------------------------------------------------------
    def seleccionar_ficha(self):
        """
        Permite seleccionar una ficha a mover, verificando que sea válida.
        """
        current_color = self.jugadores[self.jugador_actual][1]
        fichas_validas = self.fichas_jugador.get(current_color)
        if not fichas_validas:
            self.mostrar_error("No hay fichas asignadas para este jugador.")
            return
        for ficha in fichas_validas.piezas:
            if hasattr(ficha, "en_carcel") and ficha.en_carcel:
                continue
            ficha.onclick(lambda x, y, ficha=ficha: self.manejar_ficha_click(ficha))

    # ------------------------------------------------------------------------------
    # MÉTODO: safe_positions
    # ------------------------------------------------------------------------------
    def safe_positions(self):
        """
        Retorna un diccionario con las posiciones seguras y los colores permitidos.
        """
        return {
            5: "blue",
            12: None,
            17: None,
            22: "red",
            29: None,
            34: None,
            46: "gold",
            49: None,
            51: None,
            56: "green",
            63: None,
            68: None
        }

    # ------------------------------------------------------------------------------
    # MÉTODO: manejar_ficha_click
    # ------------------------------------------------------------------------------
    def manejar_ficha_click(self, ficha):
        """
        Maneja el evento de clic en una ficha, moviéndola según el movimiento ingresado
        y gestionando bloqueos o capturas.
        """
        global coordenadas, paths
        current_color = self.jugadores[self.jugador_actual][1]
        if ficha.propietario != current_color:
            self.mostrar_error("Ficha no válida para este jugador.")
            return
        if hasattr(ficha, "en_carcel") and ficha.en_carcel:
            self.mostrar_error("No se puede mover una ficha en la cárcel.")
            return
        if not hasattr(ficha, "pos_index"):
            ficha.pos_index = 0
        path_local = full_paths[current_color]
        start_index = ficha.pos_index
        computed_target = start_index + int(self.movimiento)
        print(
            f"DEBUG: start_index: {start_index}, movimiento: {self.movimiento}, computed_target: {computed_target}, len(path_local): {len(path_local)}")

        final_index = len(path_local) - 1

        # Verifica que el movimiento no exceda la última casilla.
        if computed_target > final_index:
            self.mostrar_error("No se puede avanzar más allá de la última casilla.")
            return

        target_index = computed_target
        new_coord = path_local[target_index]

        for idx in range(start_index + 1, target_index):
            coord_inter = path_local[idx]
            pieces_inter = self.get_pieces_on_square(coord_inter)
            if len(pieces_inter) == 2:
                bloqueo_color = pieces_inter[0].propietario
                self.mostrar_cartel(f"Bloqueo en la posición {coord_inter}", bloqueo_color)
                self.mostrar_error("Movimiento bloqueado por un bloqueo en el camino.")
                return

        pieces_target = self.get_pieces_on_square(new_coord)
        is_safe = False
        for pos, allowed_color in self.safe_positions().items():
            safe_coord = coordenadas[pos]
            if round(new_coord[0], 2) == round(safe_coord[0], 2) and round(new_coord[1], 2) == round(safe_coord[1], 2):
                is_safe = True
                break

        if pieces_target:
            if is_safe:
                if len(pieces_target) >= 2:
                    self.mostrar_cartel(f"Bloqueo en casilla segura en la posición {new_coord}",
                                        pieces_target[0].propietario)
                    self.mostrar_error("Movimiento no permitido: la casilla segura ya contiene 2 fichas.")
                    return
            else:
                friendly = [p for p in pieces_target if p.propietario == current_color]
                enemy = [p for p in pieces_target if p.propietario != current_color]
                if enemy:
                    if len(enemy) == 1:
                        enemy[0].volver_a_carcel()
                        print(f"{self.jugadores[self.jugador_actual][0]} captura una ficha enemiga.")
                    else:
                        self.mostrar_cartel(f"Bloqueo enemigo en la posición {new_coord}", enemy[0].propietario)
                        self.mostrar_error("Movimiento no permitido: bloqueo enemigo.")
                        return
                else:
                    if len(friendly) >= 2:
                        self.mostrar_cartel(f"Bloqueo propio en la posición {new_coord}", current_color)
                        self.mostrar_error("Movimiento no permitido: ya existe un bloqueo en esa casilla.")
                        return

        if self.dice_mode:
            if not self.usado1 and not self.usado2:
                if int(self.movimiento) == self.dado_1_valor + self.dado_2_valor:
                    self.usado1 = True
                    self.usado2 = True
                    self.dado_1_cuadro.clear()
                    self.dado_1_texto.clear()
                    self.dado_2_cuadro.clear()
                    self.dado_2_texto.clear()
                elif int(self.movimiento) == self.dado_1_valor:
                    self.usado1 = True
                    self.manual_moves = [self.dado_2_valor]
                    self.dado_1_cuadro.clear()
                    self.dado_1_texto.clear()
                elif int(self.movimiento) == self.dado_2_valor:
                    self.usado2 = True
                    self.manual_moves = [self.dado_1_valor]
                    self.dado_2_cuadro.clear()
                    self.dado_2_texto.clear()
                else:
                    self.mostrar_error("Movimiento inválido en modo dados.")
                    return
            elif not self.usado1:
                if int(self.movimiento) == self.dado_1_valor:
                    self.usado1 = True
                    self.dado_1_cuadro.clear()
                    self.dado_1_texto.clear()
                else:
                    self.mostrar_error("Movimiento inválido.")
                    return
            elif not self.usado2:
                if int(self.movimiento) == self.dado_2_valor:
                    self.usado2 = True
                    self.dado_2_cuadro.clear()
                    self.dado_2_texto.clear()
                else:
                    self.mostrar_error("Movimiento inválido.")
                    return
        else:
            pass

        ficha.pos_index = target_index
        ficha.goto(new_coord)

        # Si la ficha llega a la última casilla, se elimina y se verifica el fin del juego.
        if target_index == final_index:
            self.mostrar_tiro_actual(f"¡Ficha de {current_color} completó la ruta!")
            self.fichas_jugador[current_color].piezas.remove(ficha)
            ficha.hideturtle()
            if not self.fichas_jugador[current_color].piezas:
                self.mostrar_tiro_actual(f"¡{self.jugadores[self.jugador_actual][0]} ha ganado!")
                self.terminar_juego()
                return

        self.ultima_ficha_movida = ficha
        for ficha_valida in self.fichas_jugador[current_color].piezas:
            ficha_valida.onclick(None)
        self.tiro_texto.clear()
        coord_key = (round(new_coord[0], 2), round(new_coord[1], 2))
        friendly_count = len([p for p in self.fichas_jugador[current_color].piezas if
                              round(p.xcor(), 2) == coord_key[0] and round(p.ycor(), 2) == coord_key[1]])
        if friendly_count == 2:
            if coord_key not in self.block_markers:
                marker = Turtle()
                marker.hideturtle()
                marker.penup()
                marker.goto(new_coord[0] + 10, new_coord[1] + 10)
                marker.color("white")
                marker.write("2", font=("Arial", 8, "normal"))
                self.block_markers[coord_key] = marker
        else:
            if coord_key in self.block_markers:
                self.block_markers[coord_key].clear()
                del self.block_markers[coord_key]
        if self.dice_mode:
            if self.manual_moves:
                self.movimiento = int(self.manual_moves.pop(0))
                self.mostrar_tiro_actual(
                    f"Movimiento restante: {self.movimiento}. Selecciona otra ficha (color: {current_color})")
                self.seleccionar_ficha()
            elif self.get_valid_moves():
                self.solicitar_entrada()
            else:
                self.finalizar_turno()
        else:
            if self.manual_moves:
                self.movimiento = int(self.manual_moves.pop(0))
                self.mostrar_tiro_actual(
                    f"Movimiento manual: {self.movimiento}. Selecciona la ficha a mover (color: {current_color})")
                self.seleccionar_ficha()
            else:
                self.finalizar_turno()

    # ------------------------------------------------------------------------------
    # MÉTODO: terminar_juego
    # ------------------------------------------------------------------------------
    def terminar_juego(self):
        """
        Finaliza el juego desactivando la interacción.
        """
        self.mostrar_tiro_actual("Juego terminado. ¡Gracias por jugar!")
        self.screen.onclick(None)

    # ------------------------------------------------------------------------------
    # MÉTODO: finalizar_turno
    # ------------------------------------------------------------------------------
    def finalizar_turno(self):
        """
        Finaliza el turno actual limpiando los dados y otorgando bonus si corresponde.
        """
        self.dado_1_cuadro.clear()
        self.dado_1_texto.clear()
        self.dado_2_cuadro.clear()
        self.dado_2_texto.clear()
        self.jail_attempts = 0
        if self.dice_mode:
            if self.dado_1_valor == self.dado_2_valor and self.pares_consecutivos < 3:
                print(f"{self.jugadores[self.jugador_actual][0]} obtiene bonus por par!")
                self.lanzar_dados()
                return
        else:
            if self.pares_consecutivos > 0 and self.pares_consecutivos < 3:
                print(f"{self.jugadores[self.jugador_actual][0]} obtiene bonus por doble manual!")
                self.solicitar_movimiento_manual()
                return
            elif self.pares_consecutivos >= 3:
                if self.ultima_ficha_movida:
                    self.ultima_ficha_movida.volver_a_carcel()
                    print("Tres dobles consecutivos. La última ficha movida vuelve a la cárcel.")
        self.pasar_turno()

    # ------------------------------------------------------------------------------
    # MÉTODO: pasar_turno
    # ------------------------------------------------------------------------------
    def pasar_turno(self):
        """
        Pasa el turno al siguiente jugador y reinicia los contadores.
        """
        self.pares_consecutivos = 0
        self.jugador_actual = (self.jugador_actual + 1) % len(self.jugadores)
        self.manual_moves = []
        self.mostrar_jugador_actual()

    # ------------------------------------------------------------------------------
    # MÉTODO: mostrar_error
    # ------------------------------------------------------------------------------
    def mostrar_error(self, mensaje):
        """
        Muestra un mensaje de error centrado en la pantalla.

        Parámetros:
          mensaje -- Texto del error.
        """
        self.error_texto.clear()
        self.error_texto.goto(0, -250)
        self.error_texto.color("red")
        self.error_texto.write(mensaje, align="center", font=("Arial", 12, "bold"))
        self.screen.ontimer(self.error_texto.clear, 2000)

    # ------------------------------------------------------------------------------
    # MÉTODO: mostrar_tiro_actual
    # ------------------------------------------------------------------------------
    def mostrar_tiro_actual(self, mensaje):
        """
        Muestra el mensaje actual del tiro en una posición fija.

        Parámetros:
          mensaje -- Texto a mostrar.
        """
        self.tiro_texto.clear()
        self.tiro_texto.goto(-250, 175)
        self.tiro_texto.color("black")
        self.tiro_texto.write(mensaje, font=("Arial", 14, "bold"))

    # ------------------------------------------------------------------------------
    # MÉTODO: mostrar_jugador_actual
    # ------------------------------------------------------------------------------
    def mostrar_jugador_actual(self):
        """
        Muestra el turno del jugador actual.
        """
        self.jugador_texto.clear()
        nombre, color = self.jugadores[self.jugador_actual]
        self.jugador_texto.goto(self.x_min - 10, self.y_max + 5)
        self.jugador_texto.color(color)
        self.jugador_texto.write(f"Turno: {nombre}", font=("Arial", 16, "bold"))

    # ------------------------------------------------------------------------------
    # MÉTODO: dibujar_cuadro
    # ------------------------------------------------------------------------------
    def dibujar_cuadro(self, turtle_obj, x, y, color):
        """
        Dibuja un cuadro en la posición especificada.

        Parámetros:
          turtle_obj -- Objeto Turtle a utilizar.
          x, y       -- Coordenadas donde dibujar el cuadro.
          color      -- Color de relleno del cuadro.
        """
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.color("black", color)
        turtle_obj.begin_fill()
        for _ in range(4):
            turtle_obj.forward(30)
            turtle_obj.left(90)
        turtle_obj.end_fill()
        turtle_obj.penup()

    # ------------------------------------------------------------------------------
    # MÉTODO: mostrar_texto
    # ------------------------------------------------------------------------------
    def mostrar_texto(self, turtle_obj, x, y, texto, color):
        """
        Muestra un texto en la posición y color especificados.

        Parámetros:
          turtle_obj -- Objeto Turtle a utilizar.
          x, y       -- Coordenadas para mostrar el texto.
          texto      -- Texto a mostrar.
          color      -- Color del texto.
        """
        turtle_obj.goto(x, y)
        turtle_obj.color(color)
        turtle_obj.write(f"{texto}", font=("Arial", 14, "bold"))

    # ------------------------------------------------------------------------------
    # MÉTODO: mostrar_cartel
    # ------------------------------------------------------------------------------
    def mostrar_cartel(self, mensaje, color):
        """
        Imprime en consola un cartel con el mensaje y el color asociado.

        Parámetros:
          mensaje -- Texto del cartel.
          color   -- Color relacionado.
        """
        print(f"Cartel [{color}]: {mensaje}")

    # ------------------------------------------------------------------------------
    # MÉTODO: get_pieces_on_square
    # ------------------------------------------------------------------------------
    def get_pieces_on_square(self, coord):
        """
        Retorna una lista de fichas que se encuentran en una casilla determinada.

        Parámetros:
          coord -- Coordenadas de la casilla.

        Retorna:
          Lista de fichas presentes en esa posición.
        """
        piezas_en_casilla = []
        for fichas in self.fichas_jugador.values():
            for ficha in fichas.piezas:
                if round(ficha.xcor(), 2) == round(coord[0], 2) and round(ficha.ycor(), 2) == round(coord[1], 2):
                    piezas_en_casilla.append(ficha)
        return piezas_en_casilla
