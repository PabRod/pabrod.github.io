Title: Documentos RNE, buscable otra vez
Category: Blog
Lang: es
Tags: hacks
Slug: documentos-rne
Authors: Pablo Rodríguez-Sánchez
Summary: La nueva interfaz de RTVE que hizo llorar al que esto escribe, y una solución improvisada.
Comments: True
Translation: False
Status: hidden

## TL;DR
[Aquí](https://github.com/PabRod/tabla_documentos_rne) tienes la lista de episodios.

Pero sigue leyendo si quieres saber más.

## Obsesiones mías...

Documentos RNE (Radio Nacional de España) es uno de mis programas de radio favoritos.
Cada episodio se centra en un asunto, en el que profundiza durante cerca de una hora.

Hasta hace poco, el archivo de RNE tenía una interfaz minimalista y eficaz que permitía hacer búsquedas de manera sencilla.
Desde hace un par de años, ya no es el caso.
Siguiendo la moda de la [mierdificación](https://en.wikipedia.org/wiki/Enshittification) de Internet, la nueva interfaz obliga literalmente a pulsar "atrás" hasta llegar al año deseado.
Documentos RNE comenzó a emitirse en 2001, a razón de aproximadamente un episodio por semana, de modo que existen un montón de ellos disponibles en los extensísimos archivos de RNE.
Esto supone clicar "atrás" muchas, muchas veces.

Los audios, además, se guardan en formato `.mp3` con un nombre numérico único que nada tiene que ver con el título del programa ni del episodio, y que parece ser aleatorio (con la única restricción de que no se repitan números).

En resumen, que RNE tiene un archivo enorme y de una calidad inmensa... sin manera realmente decente de buscar y listar resultados.

No les sorprenderá saber que el que esto escribe se puso en contacto con ellos para hacerles ver este problema, pero no logró respuesta satisfactoria.
Y no diré que no lo entiendo, tienen cosas mejores que hacer, como producir el programa.

## Un anónimo benefactor

El caso es que, de pura casualidad, me he topado con alguien que se tomó la molestia de pulsar "atrás" decenas de veces, guardar artesanalmente los resultados, y compartirlos.
Casualidad, o no, este encuentro ha sucedido [en Mastodon](https://mapstodon.space/@jorgesanz/113362099721007397), una red en la que parece que 2010 nunca ha acabado.

Su archivo, fruto de un trabajo heroico, no tiene un aspecto demasiado legible.
Dejo aquí una muestra del aspecto que tenía:

```sh
ffmpeg -i 31872.mp3 -i 31872.jpg -c copy -map 0a -map 1 -metadata title="Mirada joven a la Generación del 27" -metadata album="Documentos RNE" -metadata date="2008" -metadata genre="Documentary" -metadata language="esp" '2008-04-13 Mirada joven a la Generación del 27.mp3'
ffmpeg -i 1345146.mp3 -i 1345146.jpg -c copy -map 0a -map 1 -metadata title="80 años de Radio Exterior" -metadata album="Documentos RNE" -metadata date="2022" -metadata genre="Documentary" -metadata language="esp" '2022-03-17 80 años de Radio Exterior.mp3'
...
```

Y así hasta casi 800 líneas.

## Las buenas acciones merecen una recompensa

El caso es que me ha dado tanta alegría poder recuperar mi costumbre (de abuelete, lo sé), de escucharme un episodio durante mis paseos, o en el tren, o en el gimnasio, que me he propuesto republicar esto de una manera más práctica.

[Aquí](https://github.com/PabRod/tabla_documentos_rne) pueden acceder a la lista completa[^1], incluyendo el código que he utilizado para limpiarla.
Ojalá lo disfruten tanto como yo.

[^1]: a falta de los 12 audios listados [aquí](https://github.com/PabRod/tabla_documentos_rne/blob/main/data/fallos.txt), que ya meteré a mano cuando tenga un rato. 12 de 784, añado.