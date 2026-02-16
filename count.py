import pandas as pd

archivo2023 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\[2023] far-right\Teremarinovic_Actual.xlsx'

#region de variables

i = 0
cont_boric = 0
cont_burric = 0
cont_merluzo = 0
cont_fraude = 0
cont_arbolitos = 0
cont_woke = 0
cont_onu = 0
cont_2030 = 0
cont_vallejo = 0
cont_loncon = 0
cont_progre = 0
cont_esi = 0
cont_dios = 0
cont_patria = 0
cont_familia = 0
cont_libertad = 0
cont_libertario = 0
cont_ffaa = 0
cont_carabineros = 0
cont_chilenos = 0
cont_chile = 0
cont_62 = 0
cont_rechazo = 0
cont_zurdo = 0
cont_zurderio = 0
cont_izquierda = 0
cont_comunista = 0
cont_comunismo = 0
cont_comunacho = 0
cont_pinochet = 0
cont_patriota = 0
cont_facho = 0
cont_derecha = 0
cont_derecho = 0
cont_conservador = 0
cont_nacionalista = 0
cont_globalista = 0
cont_plandemia = 0
cont_antiboric = 0
cont_antiburric = 0
cont_antimerluzo = 0
cont_antifraude = 0
cont_antiarbolitos = 0
cont_antionu = 0
cont_antiwoke = 0
cont_antivallejo = 0
cont_antiprogre = 0
cont_antizurdo = 0
cont_antizurderio = 0
cont_antiizquierda = 0
cont_anticomunista = 0
cont_anticomunismo = 0
cont_antiglobalista = 0
cont_ninguna = 0

#endregion


df2023 = pd.read_excel(archivo2023, sheet_name='Followers')
df_palabras = pd.DataFrame()

def conteo_palabras(frase_mayuscula, i):
    j  = 0
    cadena = frase_mayuscula.split(' ')
    while (j < len(cadena)):
        match (cadena[j]):
            case 'BORIC':
                global cont_boric
                cont_boric = cont_boric + 1
            case 'BURRIC':
                global cont_burric
                cont_burric = cont_burric + 1
            case 'MERLUZO':
                global cont_merluzo
                cont_merluzo = cont_merluzo + 1
            case 'FRAUDE':
                global cont_fraude
                cont_fraude = cont_fraude + 1
            case 'FRAUDES':
                cont_fraude = cont_fraude + 1
            case 'ARBOLITO':
                global cont_arbolitos
                cont_arbolitos = cont_arbolitos + 1
            case 'ARBOLITOS':
                cont_arbolitos = cont_arbolitos + 1 
            case 'WOKE':
                global cont_woke
                cont_woke = cont_woke + 1
            case 'WOKISMO':
                cont_woke = cont_woke + 1
            case 'ONU':
                global cont_onu
                cont_onu = cont_onu + 1
            case '2030':
                global cont_2030
                cont_2030 = cont_2030 + 1
            case 'VALLEJO':
                global cont_vallejo
                cont_vallejo = cont_vallejo + 1
            case 'LONCON':
                global cont_loncon
                cont_loncon = cont_loncon + 1
            case 'PROGRE':
                global cont_progre
                cont_progre = cont_progre + 1
            case 'PROGRES':
                cont_progre = cont_progre + 1 
            case 'ESI':
                global cont_esi
                cont_esi = cont_esi + 1
            case 'DIOS':
                global cont_dios
                cont_dios = cont_dios + 1
            case 'PATRIA':
                global cont_patria
                cont_patria = cont_patria + 1
            case 'FAMILIA':
                global cont_familia
                cont_familia = cont_familia + 1
            case 'LIBERTAD':
                global cont_libertad
                cont_libertad = cont_libertad + 1
            case 'LIBERTARIO':
                global cont_libertario
                cont_libertario = cont_libertario + 1
            case 'LIBERTARIOS':
                cont_libertario = cont_libertario + 1
            case 'FFAA':
                global cont_ffaa
                cont_ffaa = cont_ffaa + 1
            case 'CARABINEROS':
                global cont_carabineros
                cont_carabineros = cont_carabineros + 1
            case 'CHILENOS':
                global cont_chilenos
                cont_chilenos = cont_chilenos + 1
            case 'CHILE':
                global cont_chile
                cont_chile = cont_chile + 1
            case '62%':
                global cont_62
                cont_62 = cont_62 + 1
            case '63%':
                cont_62 = cont_62 + 1
            case 'RECHAZO':
                global cont_rechazo
                cont_rechazo = cont_rechazo + 1
            case 'ZURDO':
                global cont_zurdo
                cont_zurdo = cont_zurdo + 1
            case 'ZURDOS':
                cont_zurdo = cont_zurdo + 1
            case 'ZURDERIO':
                global cont_zurderio
                cont_zurderio = cont_zurderio + 1
            case 'IZQUIERDA':
                global cont_izquierda
                cont_izquierda = cont_izquierda + 1
            case 'COMUNISTA':
                global cont_comunista
                cont_comunista = cont_comunista + 1
            case 'COMUNISTAS':
                cont_comunista = cont_comunista + 1
            case 'COMUNISMO':
                global cont_comunismo
                cont_comunismo = cont_comunismo + 1
            case 'COMUNACHO':
                global cont_comunacho
                cont_comunacho = cont_comunacho + 1
            case 'COMUNACHOS':
                cont_comunacho = cont_comunacho + 1
            case 'PINOCHET':
                global cont_pinochet
                cont_pinochet = cont_pinochet + 1
            case 'PATRIOTA':
                global cont_patriota
                cont_patriota = cont_patriota + 1
            case 'PATRIOTAS':
                cont_patriota = cont_patriota + 1
            case 'FACHO':
                global cont_facho
                cont_facho = cont_facho + 1
            case 'FACHOS':
                cont_facho = cont_facho + 1
            case 'DERECHA':
                global cont_derecha
                cont_derecha = cont_derecha + 1
            case 'DERECHO':
                global cont_derecho
                cont_derecho = cont_derecho + 1
            case 'CONSERVADOR':
                global cont_conservador
                cont_conservador = cont_conservador + 1
            case 'NACIONALISTA':
                global cont_nacionalista
                cont_nacionalista = cont_nacionalista + 1
            case 'NACIONALISTAS':
                cont_nacionalista = cont_nacionalista + 1
            case 'GLOBALISTA':
                global cont_globalista
                cont_globalista = cont_globalista + 1
            case 'GLOBALISTAS':
                cont_globalista = cont_globalista + 1
            case 'PLANDEMIA':
                global cont_plandemia
                cont_plandemia = cont_plandemia + 1
            case 'ANTIBORIC':
                global cont_antiboric
                cont_antiboric = cont_antiboric + 1
            case 'ANTIBURRIC':
                global cont_antiburric
                cont_antiburric = cont_antiburric + 1
            case 'ANTIMERLUZO':
                global cont_antimerluzo
                cont_antimerluzo = cont_antimerluzo + 1
            case 'ANTIFRAUDE':
                global cont_antifraude
                cont_antifraude = cont_antifraude + 1
            case 'ANTIARBOLITOS':
                global cont_antiarbolitos
                cont_antiarbolitos = cont_antiarbolitos + 1
            case 'ANTIONU':
                global cont_antionu
                cont_antionu = cont_antionu + 1
            case 'ANTIWOKE':
                global cont_antiwoke
                cont_antiwoke = cont_antiwoke + 1
            case 'ANTIVALLEJO':
                global cont_antivallejo
                cont_antivallejo = cont_antivallejo + 1
            case 'ANTIPROGRE':
                global cont_antiprogre
                cont_antiprogre = cont_antiprogre + 1
            case 'ANTIZURDO':
                global cont_antizurdo
                cont_antizurdo = cont_antizurdo + 1
            case 'ANTIZURDERIO':
                global cont_antizurderio
                cont_antizurderio = cont_antizurderio + 1
            case 'ANTIIZQUIERDA':
                global cont_antiizquierda
                cont_antiizquierda = cont_antiizquierda + 1
            case 'ANTICOMUNISTA':
                global cont_anticomunista
                cont_anticomunista = cont_anticomunista
            case 'ANTICOMUNISMO':
                global cont_anticomunismo
                cont_anticomunismo = cont_anticomunismo + 1
            case 'ANTIGLOBALISTA':
                global cont_antiglobalista
                cont_antiglobalista = cont_antiglobalista + 1
            case _:
                global cont_ninguna
                cont_ninguna = cont_ninguna + 1
        j = j + 1
    user_words = [{"Boric":cont_boric, "Burric":cont_burric, "Merluzo":cont_merluzo, "Fraude":cont_fraude, "Arbolitos":cont_arbolitos, "Woke":cont_woke, "ONU":cont_onu, "2030":cont_2030, "Vallejo":cont_vallejo, "Loncon":cont_loncon, "Progre":cont_progre, "ESI":cont_esi, "Dios":cont_dios, "Patria":cont_patria, "Familia":cont_familia, "Libertad":cont_libertad, "Libertario":cont_libertario, "FFAA":cont_ffaa, "Carabineros":cont_carabineros, "Chilenos":cont_chilenos, "Chile":cont_chile, "62%":cont_62, "Rechazo":cont_rechazo, "Zurdo":cont_zurdo, "Zurderio": cont_zurderio, "Izquierda":cont_izquierda, "Comunista":cont_comunista, "Comunismo":cont_comunismo, "Comunacho":cont_comunacho, "Pinochet":cont_pinochet, "Patriota":cont_patriota, "Facho":cont_facho, "Derecha":cont_derecha, "Derecho":cont_derecho, "Conservador":cont_conservador, "Nacionalista":cont_nacionalista, "Globalista":cont_globalista, "Plandemia":cont_plandemia, "AntiBoric":cont_antiboric, "AntiBurric":cont_antiburric, "AntiMerluzo":cont_antimerluzo, "AntiFraude":cont_antifraude, "AntiArbolitos":cont_antiarbolitos, "AntiOnu":cont_antionu, "AntiWoke":cont_antiwoke, "AntiVallejo":cont_antivallejo, "AntiProgre":cont_antiprogre, "AntiZurdo":cont_antizurdo, "AntiZurderio":cont_antizurderio, "AntiIzquierda":cont_antiizquierda, "AntiComunista":cont_anticomunista, "AntiComunismo":cont_anticomunismo, "AntiGlobalista":cont_antiglobalista}]
    global df_user_words
    df_user_words = pd.DataFrame(user_words)

def reseteo_contador():
    global cont_boric
    cont_boric = 0
    global cont_burric
    cont_burric = 0
    global cont_merluzo
    cont_merluzo = 0
    global cont_fraude
    cont_fraude = 0
    global cont_arbolitos
    cont_arbolitos = 0
    global cont_woke
    cont_woke = 0
    global cont_onu
    cont_onu = 0
    global cont_2030
    cont_2030 = 0
    global cont_vallejo
    cont_vallejo = 0
    global cont_loncon
    cont_loncon = 0
    global cont_progre
    cont_progre = 0
    global cont_esi
    cont_esi = 0
    global cont_dios
    cont_dios = 0
    global cont_patria
    cont_patria = 0
    global cont_familia
    cont_familia = 0
    global cont_libertad
    cont_libertad = 0
    global cont_libertario
    cont_libertario = 0
    global cont_ffaa
    cont_ffaa = 0
    global cont_carabineros
    cont_carabineros = 0
    global cont_chilenos
    cont_chilenos = 0
    global cont_chile
    cont_chile = 0
    global cont_62
    cont_62 = 0
    global cont_rechazo
    cont_rechazo = 0
    global cont_zurdo
    cont_zurdo = 0
    global cont_zurderio
    cont_zurderio = 0
    global cont_izquierda
    cont_izquierda = 0
    global cont_comunista
    cont_comunista = 0
    global cont_comunismo
    cont_comunismo = 0
    global cont_comunacho
    cont_comunacho = 0
    global cont_pinochet
    cont_pinochet = 0
    global cont_patriota
    cont_patriota = 0
    global cont_facho
    cont_facho = 0
    global cont_derecha
    cont_derecha = 0
    global cont_derecho
    cont_derecho = 0
    global cont_conservador
    cont_conservador = 0
    global cont_nacionalista
    cont_nacionalista = 0
    global cont_globalista
    cont_globalista = 0
    global cont_plandemia
    cont_plandemia = 0
    global cont_antiboric
    cont_antiboric = 0
    global cont_antiburric
    cont_antiburric = 0
    global cont_antimerluzo
    cont_antimerluzo = 0
    global cont_antifraude
    cont_antifraude = 0
    global cont_antiarbolitos
    cont_antiarbolitos = 0
    global cont_antionu
    cont_antionu = 0
    global cont_antiwoke
    cont_antiwoke = 0
    global cont_antivallejo
    cont_antivallejo = 0
    global cont_antiprogre
    cont_antiprogre = 0
    global cont_antizurdo
    cont_antizurdo = 0
    global cont_antizurderio
    cont_antizurderio = 0
    global cont_antiizquierda
    cont_antiizquierda = 0
    global cont_anticomunista
    cont_anticomunista = 0
    global cont_anticomunismo
    cont_anticomunismo = 0
    global cont_antiglobalista
    cont_antiglobalista = 0

while(len(df2023) > i):
#while(5 > i):
    print("valor i: ", i)
    frase = str(df2023['description'][i])
    frase_mayuscula = frase.upper()
    conteo_palabras(frase_mayuscula, i)
    df_palabras = pd.concat([df_palabras, df_user_words])
    reseteo_contador()
    i = i + 1

df_palabras.to_excel("palabras.xlsx", sheet_name='palabra')