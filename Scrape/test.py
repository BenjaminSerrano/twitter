import asyncio
import tracemalloc
import pandas as pd
import os
from tweety import TwitterAsync

# Iniciar tracemalloc para depuración de memoria
tracemalloc.start()

# Definir el tamaño del bloque de usuarios por ejecución
BLOQUE_USUARIOS = 60
MAX_USUARIOS = 13540
ruta_salida = r"/Users/benjaminserranobarba/Desktop/Trabajo/Twitter/Scrape/tweets_info224.xlsx"

async def main(inicio_usuario=0):
    app = TwitterAsync("session")

    try:
        # Iniciar sesión en Twitter
        #await app.sign_in("BarBenjaTaza", "19154492-7", extra="jamon_1996@hotmail.com")
        await app.sign_in("LaniBSide", "ajidi280116", extra="anaita0247@gmail.com")
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return

    # Ruta del archivo de Excel de entrada
    nombresExcel = r"/Users/benjaminserranobarba/Desktop/Trabajo/Twitter/Conjunto 2020-2023.xlsx"
    try:
        # Cargar el archivo de Excel con los nombres de usuario
        dataFrameNombres = pd.read_excel(nombresExcel, sheet_name="2020")

        # Verificar que la columna "ScreenName" existe y tiene datos
        if not dataFrameNombres.empty and "ScreenName" in dataFrameNombres.columns:
            # Obtener el total de usuarios disponibles
            total_usuarios = len(dataFrameNombres)

            # Determinar el rango de usuarios en esta ejecución
            fin_usuario = min(inicio_usuario + BLOQUE_USUARIOS, total_usuarios, MAX_USUARIOS)
            screen_names = dataFrameNombres["ScreenName"][inicio_usuario:fin_usuario].tolist()

            if not screen_names:
                print("No hay más usuarios para procesar.")
                return

            print(f"📊 Procesando usuarios {inicio_usuario} a {fin_usuario}...")

            all_users_data = []

            for screen_name in screen_names:
                try:
                    # Obtener tweets del usuario actual
                    all_tweets = await app.get_tweets(screen_name)

                    # Si el usuario tiene perfil privado o no se pueden obtener tweets
                    if not all_tweets:
                        print(f"🔒 Usuario {screen_name} tiene perfil privado o sin tweets visibles.")
                        tweet_info = {
                            "Usuario": screen_name,
                            "Estado": "Perfil privado"
                        }
                    else:
                        # Crear un diccionario con los datos del usuario
                        tweet_info = {"Usuario": screen_name, "Estado": "Público"}

                        for i, tweet in enumerate(all_tweets[:5]):
                            tweet_info[f"{i+1}° Tweet"] = tweet.text
                            tweet_info[f"¿Es Retweet el {i+1}° Tweet?"] = tweet.is_retweet  # Verifica si es un retweet

                        # Obtener la fecha de creación del primer tweet si existe
                        fecha_primer_tweet = all_tweets[0].created_on if all_tweets else "No disponible"
                        tweet_info["Fecha de creación del primer tweet"] = fecha_primer_tweet

                    # Agregar la fila al conjunto de datos
                    all_users_data.append(tweet_info)

                    # Esperar 30 segundos entre consultas para evitar bloqueos
                    #await asyncio.sleep(5)

                except Exception as e:
                    print(f"⚠️ Error al obtener tweets de {screen_name}: {e}")
                    tweet_info = {
                        "Usuario": screen_name,
                        "Estado": "Error al obtener tweets"
                    }
                    all_users_data.append(tweet_info)

            # Crear el DataFrame con los datos de los usuarios procesados
            df_nuevo = pd.DataFrame(all_users_data)
            df_nuevo["Fecha de creación del primer tweet"] = df_nuevo["Fecha de creación del primer tweet"].dt.tz_localize(None)
            # Si el archivo Excel ya existe, cargarlo y agregar nuevos datos
            if os.path.exists(ruta_salida):
                df_existente = pd.read_excel(ruta_salida)
                df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
            else:
                df_final = df_nuevo

            # Guardar el DataFrame actualizado en el archivo Excel
            df_final.to_excel(ruta_salida, index=False)

            print(f"✅ Datos guardados en: {ruta_salida}")
            print(f"🔄 Listo para la próxima ejecución desde el usuario {fin_usuario}")

        else:
            print("No hay datos válidos en la columna 'ScreenName'.")

    except Exception as e:
        print(f"Error al leer el archivo o procesar datos: {e}")

# Definir desde qué usuario empezar (ajustar manualmente en cada ejecución)
INICIO_USUARIO = 13500 # Cambiar a 60, 120, 180, ... en cada ejecución

try:
    asyncio.run(main(INICIO_USUARIO))
except Exception as e:
    print(f"Ocurrió un error general: {e}")
