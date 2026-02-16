# Twitter Far-Right Analysis (Chile, 2020-2023)

Proyecto de investigaci&oacute;n acad&eacute;mica que analiza el discurso y las redes de la ultraderecha chilena en Twitter (X), comparando datos entre 2020 y 2023.

## Objetivo

Estudiar c&oacute;mo han evolucionado las redes de seguidores, la ret&oacute;rica pol&iacute;tica y la actividad en Twitter de figuras prominentes de la ultraderecha chilena:

- Jos&eacute; Antonio Kast
- Tere Marinovic
- Sergio Melnick
- Jorge Err&aacute;zuriz
- Gonzalo de la Carrera

## Estructura del repositorio

```
.
├── Scrape/                          # Scripts de recolecci&oacute;n de datos
│   ├── userInfoTwitter.py           # Scraper de perfiles de usuario (tweety)
│   ├── fixError.py                  # Scraper as&iacute;ncrono de tweets
│   ├── recolect.py                  # Consolidaci&oacute;n de datos scrapeados
│   ├── union.py                     # Merge de datos de usuario y tweets
│   └── badones.py                   # Limpieza de duplicados
│
├── [2022] far-right in Twitter/     # Estudio 2020 (#YoRechazo)
│   ├── datos/                       # Datos crudos (followers, followees, tweets)
│   ├── nubes de palabras/           # Visualizaciones (word clouds)
│   └── nota de prensa/              # Material de prensa
│
├── [2023] far-right/                # Datos actualizados 2023
│   └── Nubes/                       # Word clouds 2023
│
├── Tweets.py                        # Recolecci&oacute;n de tweets v&iacute;a Tweepy
├── UserData.py                      # Extracci&oacute;n de perfiles de usuario
├── count.py                         # Conteo de palabras de ret&oacute;rica pol&iacute;tica
├── countEmojis.py                   # An&aacute;lisis de emojis nacionalistas
├── newName.py                       # Rastreo de cambios de nombre de usuario
├── newDataUser.py                   # Extracci&oacute;n masiva de perfiles
├── calculos.py                      # An&aacute;lisis comparativo 2020 vs 2023
├── compare.py                       # Comparaci&oacute;n entre datasets
├── filter.py                        # Filtrado y deduplicaci&oacute;n
│
└── *.xlsx                           # Datasets y resultados
```

## Metodolog&iacute;a

1. **Identificaci&oacute;n** de figuras pol&iacute;ticas clave de la ultraderecha chilena
2. **Recolecci&oacute;n** de sus redes de seguidores/seguidos mediante la API de Twitter (Tweepy y Tweety)
3. **Limpieza** de datos: eliminaci&oacute;n de duplicados, manejo de cuentas protegidas/suspendidas
4. **An&aacute;lisis de perfiles**: metadatos, descripciones, verificaci&oacute;n, ubicaci&oacute;n
5. **An&aacute;lisis de contenido**:
   - Frecuencia de palabras de ret&oacute;rica pol&iacute;tica en descripciones de usuario
   - Uso de emojis nacionalistas
   - Seguimiento de cambios de nombre de cuenta
6. **An&aacute;lisis comparativo** de la evoluci&oacute;n de las redes entre 2020 y 2023
7. **Visualizaci&oacute;n** mediante nubes de palabras

## Herramientas

- **Python 3**
- **Pandas** - Manipulaci&oacute;n de datos
- **Tweepy** - API oficial de Twitter
- **Tweety** - Scraping alternativo de Twitter
- **openpyxl** - Lectura/escritura de archivos Excel
