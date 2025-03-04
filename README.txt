--------------------------------------------------
         Instrucciones y Reglas del Juego "Parques"
--------------------------------------------------

Objetivo del Juego:
-------------------
El objetivo es llevar todas tus fichas desde la cárcel hasta la meta, completando la ruta asignada a tu color. 
El primer jugador en lograrlo es declarado ganador.

Preparación:
------------
1. Cada jugador elige un color (Azul, Rojo, Amarillo o Verde).
2. Las fichas de cada jugador se colocan en su posición inicial (la cárcel).
3. Se configura el tablero, que muestra las rutas principales y los carriles exclusivos para cada jugador.
4. Se selecciona el modo de juego:
   - Modo Normal: El movimiento se determina mediante el lanzamiento automático de dados.
   - Modo Desarrollador: Permite ingresar movimientos manualmente para pruebas o ajustes.
     * Nota Importante: Aunque el modo desarrollador permite ingresar movimientos de forma manual,
       la extracción de fichas de la cárcel **solo** se puede realizar utilizando el lanzamiento
       de dados del modo normal.

Reglas Básicas:
---------------
1. Turnos:
   - Los jugadores se turnan de forma cíclica.
   - En cada turno, el jugador debe lanzar los dados o ingresar el movimiento, según el modo de juego seleccionado.

2. Lanzamiento de Dados:
   - Se lanzan dos dados que generan números aleatorios del 1 al 6.
   - Los posibles movimientos son:
     * El valor del primer dado.
     * El valor del segundo dado.
     * La suma de ambos dados (si ninguno ha sido usado aún).
   - Si ambos dados muestran el mismo número (doble), se otorga un movimiento extra (bonus), siempre que no se consigan tres dobles consecutivos.

3. Movimiento de Fichas:
   - Tras definir el movimiento, el jugador selecciona la ficha que desea mover.
   - La ficha se desplaza a lo largo de la ruta definida para su color.
   - No se permite un movimiento que exceda la última casilla de la ruta.
   - Durante el movimiento se verifica:
     * Bloqueos: No se puede avanzar si existe un bloqueo (dos fichas, propias o enemigas) en el trayecto.
     * Casillas Seguras: Algunas casillas (definidas como “seguras”) restringen capturas cuando están ocupadas por dos fichas.
     * Capturas: Si la ficha se mueve a una casilla ocupada por una sola ficha enemiga, ésta se captura y se devuelve a la cárcel.

4. Extracción de Fichas de la Cárcel:
   - Las fichas comienzan en la cárcel y no pueden moverse hasta ser extraídas.
   - Si en el lanzamiento se obtiene un 5 (ya sea individualmente o por la suma de ambos dados), se permite extraer fichas de la cárcel.
   - Se pueden extraer hasta dos fichas, o solo una si ya existe una ficha aliada en la posición de salida.
   - **Importante:** La extracción de fichas de la cárcel **solo se puede realizar en el modo normal** de lanzamiento de dados,
     no estando habilitada en el modo desarrollador.

5. Finalización del Movimiento y Turno:
   - Si al mover la ficha aún queda un movimiento pendiente (por ejemplo, cuando se usa uno de los dados), el jugador puede continuar moviendo otra ficha.
   - Cuando ya no quedan movimientos válidos, el turno finaliza y se pasa al siguiente jugador.
   - Si se lanza doble y se cumplen las condiciones, el jugador obtiene un turno adicional.

6. Fin del Juego:
   - Una vez que un jugador logra que todas sus fichas completen la ruta y alcancen la casilla final de su carril exclusivo, se declara ganador.
   - El juego muestra un mensaje de felicitación y finaliza la interacción.

Modo Desarrollador:
-------------------
- El modo desarrollador permite que el jugador ingrese manualmente los movimientos mediante cuadros de diálogo.
- Este modo es útil para pruebas y para entender en detalle la mecánica de movimiento de las fichas.
- **Sin embargo, recuerde que aunque se puedan ingresar movimientos manualmente en este modo,
  la acción de extraer fichas de la cárcel (salir de la cárcel) requiere obtener un 5 a través del lanzamiento
  de dados, lo que solo se activa en el modo normal.**

Consejos:
---------
- Presta atención a los mensajes en pantalla, ya que indican errores o acciones especiales (como capturas o la extracción de fichas de la cárcel).
- Planifica tus movimientos considerando la posición de las fichas enemigas y posibles bloqueos.
- Utiliza el modo desarrollador para practicar y comprender mejor la mecánica, pero recuerda que algunas acciones
  (como salir de la cárcel) requieren el lanzamiento de dados en modo normal.

¡Disfruta del juego y buena suerte!
--------------------------------------------------