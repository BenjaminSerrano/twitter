from tweety import Twitter, exceptions_
import pandas as pd

app = Twitter("session")


app.sign_in("BarBenjaTaza", "19154492-7")
#app.sign_in("LaniBSide", "ajidi280116", extra="anaita0247@gmail.com")

nombresExcel = r"/Users/benjaminserranobarba/Desktop/Trabajo/Twitter/Conjunto 2020-2023.xlsx"

resultados = pd.DataFrame()

dataFrameNombres = pd.read_excel(nombresExcel, sheet_name='2020')

i = 13516 #aumento de 70 en 70

while(i < 13540): #13540
    print(i)
    try: 
        user = app.get_user_info(dataFrameNombres["ScreenName"][i])
        userDataframe = [{"id":user.id, "Name in header":user.name, "Description":user.description, "Protected": user.protected, "Verified": user.verified, "Likes of all time":user.favourites_count, "Followers":user.followers_count, "Friends":user.friends_count, "Location": user.location, "@":user.username, "Location": user.location, "Sensitive content": user.possibly_sensitive, "Created at":user.created_at}]
        df_users = pd.DataFrame(userDataframe)
        df_users["Created at"] = df_users["Created at"].dt.tz_localize(None)
        resultados = (pd.concat([resultados, df_users]))
    except exceptions_.UserNotFound:
        userDataframe_notFound = [{"id": "Esta cuenta no existe", "Name in header": "", "Description": "", "Protected": "", "Verified": "", "Likes of all time": "", "Followers": "", "Friends": "", "Location": "", "@": dataFrameNombres["ScreenName"][i], "Location": "", "Sensitive content": "", "Created at": ""}]
        df_users = pd.DataFrame(userDataframe_notFound)
        resultados = (pd.concat([resultados, df_users]))
    except exceptions_.UserProtected:
        userDataframe_protected = [{"id": "Protegido", "Name in header": "", "Description": "", "Protected": "", "Verified": "", "Likes of all time": "", "Followers": "", "Friends": "", "Location": "", "@": dataFrameNombres["ScreenName"][i], "Location": "", "Sensitive content": "", "Created at": ""}]
        df_users = pd.DataFrame(userDataframe_protected)
        resultados = (pd.concat([resultados, df_users]))
    except exceptions_.UnknownError:
        resultados = (pd.concat([resultados, df_users]))
    i = i + 1

resultados.to_excel("usersfix.xlsx")