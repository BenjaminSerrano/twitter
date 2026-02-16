import pandas as pd
import os
from tweety import Twitter

info = pd.read_excel("Final.xlsx")
ruta_salida = r"/Users/benjaminserranobarba/Desktop/Trabajo/Twitter/Scrape/tweets_fix40.xlsx"
archivo_posicion = "posicion_actual.txt"

app = Twitter("session")
#app.sign_in("BarBenjaTaza", "19154492-7")
app.sign_in("LaniBSide", "ajidi280116", extra="anaita0247@gmail.com")

# Leer la posición actual o inicializar en 0
if os.path.exists(archivo_posicion):
    with open(archivo_posicion, "r") as file:
        posicion_actual = int(file.read().strip())
else:
    posicion_actual = 0

all_users_data = []
usuarios_procesados = 0

i = posicion_actual
while i < len(info) and usuarios_procesados < 60:
    usuario = info.loc[i, 'Usuario']
    if info.loc[i, 'Estado'] == 'Error al obtener tweets':
        try:
            all_tweets = app.get_tweets(usuario)
            tweet_info = {"Usuario": usuario, "Estado": "Público"}

            for j, tweet in enumerate(all_tweets[:5]):
                tweet_info[f"{j+1}° Tweet"] = tweet.text
                tweet_info[f"¿Es Retweet el {j+1}° Tweet?"] = tweet.is_retweet

            fecha_primer_tweet = all_tweets[0].created_on if all_tweets else "No disponible"
            tweet_info["Fecha de creación del primer tweet"] = fecha_primer_tweet
            
            all_users_data.append(tweet_info)
            usuarios_procesados += 1

        except Exception as e:
            print(f"⚠️ Error al obtener tweets de {usuario}: {e}")
            tweet_info = {"Usuario": usuario, "Estado": str(e)}
            all_users_data.append(tweet_info)
            usuarios_procesados += 1

    i += 1

# Guardar la posición actual para la próxima ejecución
with open(archivo_posicion, "w") as file:
    file.write(str(i))

if all_users_data:
    df_nuevo = pd.DataFrame(all_users_data)

    # Comprobar si existe la columna antes de convertirla
    if "Fecha de creación del primer tweet" in df_nuevo.columns:
        df_nuevo["Fecha de creación del primer tweet"] = pd.to_datetime(
            df_nuevo["Fecha de creación del primer tweet"], errors='coerce'
        ).dt.tz_localize(None)

    if os.path.exists(ruta_salida):
        df_existente = pd.read_excel(ruta_salida)
        df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
    else:
        df_final = df_nuevo

    df_final.to_excel(ruta_salida, index=False)
else:
    print("No hubo usuarios para procesar.")

print(f"Posición actual guardada en {i}")
