import pandas as pd

archivo2023 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\conjunto.xlsx'

df1 = pd.read_excel(archivo2023, sheet_name='2023') 
df2 = pd.read_excel(archivo2023, sheet_name='2020')

ids_nuevos = []
i = 0


def busqueda_pasado(id2020):
    j = 0
    flag = False
    while(len(df1) > j):
        id2023 = df1['id_str'][j]
        if(id2023 == id2020):
            idExcel = df1['created_at'][j]
            ids_nuevos.append(idExcel)
            flag = True
            break;
        j = j + 1
    if(flag == False):
        data = 'No data'
        ids_nuevos.append(data)

while(len(df2) > i):
    print("valor i: ", i)
    id2020 = df2['IdStr'][i]
    busqueda_pasado(id2020)
    i = i + 1

final = pd.DataFrame(ids_nuevos, columns=['name_before'])
final.to_excel("names.xlsx")