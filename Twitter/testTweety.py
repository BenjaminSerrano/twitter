from tweety import Twitter, exceptions_
import pandas as pd

app = Twitter("session")

app.sign_in("BarBenjaTaza", "19154492-7")

#app.sign_in("LaniBSide", "ajidi280116")

nombresExcel = r'C:\Users\jamon\Desktop\Trabajo\Twitter\Twitter\Conjunto 2020-2023.xlsx'

resultados = pd.DataFrame()

dataFrameNombres = pd.read_excel(nombresExcel, sheet_name='2020')
###el users124 llega hasta el 80620
i = 13490 #aumento de 70 en 70

while(i < 13540): #el while tiene que llegar a 13.541
    print(i)
    try: 
        user = app.get_user_info(dataFrameNombres["ScreenName"][i])
        userDataframe = [{"id":user.id, "Created at":user.created_at, "Description":user.description, "Likes of all time":user.favourites_count, "Followers":user.followers_count, "Friends":user.friends_count, "Name in header":user.name, "@":user.username, "IDK":user.screen_name}]
        df_users = pd.DataFrame(userDataframe)
        df_users["Created at"] = df_users["Created at"].dt.tz_localize(None)
        resultados = (pd.concat([resultados, df_users]))
    except exceptions_.UserNotFound:
        print("No se encontro")
    except exceptions_.UserProtected:
        print("Protegido")
    except exceptions_.UnknownError:
        resultados = (pd.concat([resultados, df_users]))
    i = i + 1

resultados.to_excel("users193.xlsx")