# Flappy Bird - Versión Modificada

Este repositorio contiene una versión modificada del clásico juego Flappy Bird, desarrollada en Python utilizando la librería `pygame`. El proyecto implementa una serie de ajustes específicos sobre la versión original para alterar la jugabilidad y la estética del juego.

## Modificaciones Realizadas

A continuación, se detallan las modificaciones clave implementadas en el código fuente, de acuerdo con los requisitos establecidos:

### 1. Velocidad del Pájaro

La velocidad de desplazamiento horizontal del juego, que afecta tanto a las tuberías como al suelo, se ha ajustado. En el código, la velocidad de movimiento de los objetos se ha establecido en 2 píxeles por fotograma, lo que representa una reducción a la mitad en comparación con una velocidad estándar de 4 píxeles por fotograma. Esto hace que el juego sea más lento.

•
Líneas de código relevantes: 21, 210

### 2. Dimensiones de la Pantalla

La ventana del juego ha sido redimensionada a 510 píxeles de ancho por 740 píxeles de alto. Todos los elementos visuales, incluyendo el pájaro, las tuberías, el fondo y los marcadores, han sido reposicionados y escalados para adaptarse correctamente a esta nueva resolución, asegurando una experiencia de juego cohesiva y bien presentada.

•
Línea de código relevante: 88

### 3. Recursos Gráficos y de Sonido

Se han reemplazado los recursos visuales y auditivos originales del juego. Esto incluye:

•
Un nuevo fondo de pantalla para dar al juego una apariencia visual única.

•
Nuevos efectos de sonido para las acciones principales del juego, como el aleteo del pájaro, la colisión y la puntuación.

Estos recursos personalizados se cargan desde los directorios `assets/` y `sound/`.

•
Líneas de código relevantes: 102, 139 a 141

### Requisitos

Para poder ejecutar el juego, es necesario tener Python y la librería pygame instalados en el sistema.

Bash

```
pip install pygame
```


### Ejecución

Para iniciar el juego, simplemente ejecuta el script de Python desde la terminal (en mi caso seria con index.py):

Bash

```
python index.py
```


### Demostración

Junto con el código fuente, se adjunta un video de demostración que muestra el juego en funcionamiento con todas las modificaciones aplicadas, evidenciando la correcta implementación de los cambios en la velocidad, dimensiones y personalización de recursos, este video es parte de el segundo parcial de Desarrollo de Software de el instituto ISRI.

[Ver video](https://www.loom.com/share/18b97396bf464175b6dc743b7219ce6b)

