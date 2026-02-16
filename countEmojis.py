import pandas as pd

archivo2023 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\[2023] far-right\TereMarinovic_Actual.xlsx'

df2023 = pd.read_excel(archivo2023, sheet_name='Followees')
df_emojis = pd.DataFrame()

i = 0
cont_bandera = 0
cont_hacha = 0
cont_arbol = 0
cont_nada = 0

def conteo_palabras(frase_mayuscula, i):
    j  = 0
    cadena = frase_mayuscula.split(' ')
    while (j < len(cadena)):
        match (cadena[j]):
            case '🇨🇱':
                global cont_bandera
                cont_bandera = cont_bandera + 1
            case '🌳':
                global cont_arbol
                cont_arbol = cont_arbol + 1
            case '🪓':
                global cont_hacha
                cont_hacha = cont_hacha + 1
            case _:
                global cont_nada
                cont_nada = cont_nada + 1
        j = j + 1
    user_emojis = [{"Bandera De Chile":cont_bandera, "Emoji Arbolito":cont_arbol, "Emoji Hacha":cont_hacha}]
    global df_user_emojis
    df_user_emojis = pd.DataFrame(user_emojis)

def reseteo_contador():
    global cont_bandera
    cont_bandera = 0
    global cont_hacha
    cont_hacha = 0
    global cont_arbol
    cont_arbol = 0
    global cont_nada
    cont_nada = 0

while(len(df2023) > i):
    print("valor i: ", i)
    frase = str(df2023['description'][i])
    conteo_palabras(frase, i)
    df_emojis = pd.concat([df_emojis, df_user_emojis])
    reseteo_contador()
    i = i + 1

df_emojis.to_excel("emojis.xlsx", sheet_name='emojis')