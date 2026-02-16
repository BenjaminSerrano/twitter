import pandas as pd

# Rutas de los archivos
archivo_base = "archivo_sin_duplicados_2023.xlsx"
archivo_comparar = "./Scrape/Final_final_ahora_si_que_si.xlsx"

# Leer ambos archivos Excel
df_base = pd.read_excel(archivo_base)
df_comparar = pd.read_excel(archivo_comparar)

# Identificar filas de df_comparar que no están en df_base
df_diferencia = df_comparar.merge(df_base.drop_duplicates(), how='outer', indicator=True)
df_unicas = df_diferencia[df_diferencia['_merge'] == 'left_only'].drop(columns=['_merge'])

# Guardar resultado en nuevo archivo
archivo_resultado = "filas_no_encontradas_2025.xlsx"
df_unicas.to_excel(archivo_resultado, index=False)

print(f"Filas únicas del segundo archivo guardadas en '{archivo_resultado}'")
