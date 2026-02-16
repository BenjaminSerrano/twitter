import pandas as pd
import glob

# Patrón de los archivos Excel a leer (ajusta según la ruta específica o extensión)
excel_files = glob.glob('tweets_fix*.xlsx')

# Lista para almacenar los DataFrames
dfs = []

# Leer cada archivo Excel y añadirlo a la lista
for file in excel_files:
    df = pd.read_excel(file)
    dfs.append(df)

# Concatenar todos los DataFrames en uno solo
df_consolidado = pd.concat(dfs, ignore_index=True)

# Exportar el DataFrame consolidado a un nuevo archivo Excel
df_consolidado.to_excel('tweets_info_consolidado.xlsx', index=False)

print("Archivos combinados exitosamente en 'tweets_info_consolidado.xlsx'")
