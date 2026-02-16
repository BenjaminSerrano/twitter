import pandas as pd

# Ruta del archivo original
archivo_entrada = "Conjunto 2020-2023.xlsx"

# Leer la hoja '2023' del archivo Excel
df = pd.read_excel(archivo_entrada, sheet_name="2020")

# Eliminar filas duplicadas basadas en 'screen_name', manteniendo solo la primera ocurrencia
df_sin_duplicados = df.drop_duplicates(subset="ScreenName", keep="first")

# Guardar el nuevo DataFrame en un nuevo archivo Excel
archivo_salida = "archivo_sin_duplicados_2020.xlsx"
df_sin_duplicados.to_excel(archivo_salida, index=False)

print(f"Archivo sin duplicados guardado como '{archivo_salida}'")
