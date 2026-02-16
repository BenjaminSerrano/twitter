import pandas as pd

archivo2020 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\[2022] far-right in Twitter\datos\Far-Rigth\TereMarinovic.xlsx'
archivo2023 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\[2023] far-right\Teremarinovic_Actual.xlsx'

df2020 = pd.read_excel(archivo2020, sheet_name='Followees')
df2023 = pd.read_excel(archivo2023, sheet_name='Followees')

nombres_antiguos = []
i = 0

def busqueda_pasado(arroba2023):
    j = 0
    while(len(df2020) > j):
        arroba2020 = df2020['Screen Name'][j]
        if(arroba2020 == arroba2023):
            nombre2020 = df2020['Name'][j]
            nombres_antiguos.append(nombre2020)
            break;
        j = j + 1
    return;

while(len(df2023) > i):
    print("valor i: ", i)
    flag = False
    arroba2023 = df2023['screen_name'][i]
    busqueda_pasado(arroba2023)
    i = i + 1

final = pd.DataFrame(nombres_antiguos, columns=['name_before'])
final.to_excel("names.xlsx")