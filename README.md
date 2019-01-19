# #10YearsChallenge

## Twitter

El script va a descargar las fotos de los Tweets para la query `10 year challenge` excluyendo retweets.

Va a generar una carpeta `files/twitter` que contiene:

* archivo `Tweets.json` con los tweets que tuviesen imágenes.
* subdirectorio `pictures` con las imágenes identificadas por el _id_ del tweet y con un guión bajo el número de imagen.

### Configuración

Se deben completar las key de Twitter en el archivo `config.json`.

## Instagram

Basado en [https://medium.com/@h4t0n/instagram-data-scraping-550c5f2fb6f1](https://medium.com/@h4t0n/instagram-data-scraping-550c5f2fb6f1)

El script va a descargar las fotos para el hashtag `#10yearschallenge` sin restricciones.

Va a generar una carpeta `files/instagram` que contiene:

* archivo `Instagram.json` con los nodos correspondientes para bajar las imágenes.
* subdirectorio `pictures` con las imágenes identificadas por el _shortcode_ del post y con un guión bajo el número de imagen.