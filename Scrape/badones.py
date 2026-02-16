import pandas as pd

# Cargar el archivo
archivo = "archivo_actualizado.xlsx"
df = pd.read_excel(archivo)

# Asegurar que Likes of all time es numérico
df["Likes of all time"] = pd.to_numeric(df["Likes of all time"], errors="coerce")

# Filtrar filas válidas (sin NaN en Usuario ni en Likes of all time)
df_valid = df.dropna(subset=["Usuario", "Likes of all time"])

# Obtener índices del mínimo de likes por usuario
idx_min_likes = df_valid.groupby("Usuario")["Likes of all time"].idxmin()

# Filtrar el DataFrame original con esos índices
df_limpio = df.loc[idx_min_likes]

# Guardar el resultado
df_limpio.to_excel("archivo_sin_duplicados.xlsx", index=False)
