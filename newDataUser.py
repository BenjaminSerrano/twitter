import tweepy
import tweepy.errors
import pandas as pd

#region de autorizacion por parte de twitter

""" Api_Key = 'pMFZTdFIwJJE8VkZNBIN7Ehly'
Api_Key_Secret = 'LjFj8S7XojspkzIXOerz7MELZFuol1dBsYp6Rp6xED6x3JVrso'
Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAALzrFgEAAAAAzGr7mDLK0SVjrSKvej7i7lzz8dM%3Dp6kJE6sQvuC24SisN4xPh1UEJCrMh4DTwJtyZbmCTYPGU1AkIs'
Access_Token = '446462897-Oi0mmOfXlNJj8h2CFeRi5qzeCMeg73E68ZQYkffQ'
Access_Token_Secret = 'oIO5TrOltMYpSjWY2ot6PktPfi9QjY9v4dT1pwyr8CXsC'
 """
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKUjnwEAAAAAb0Grnhi5eoBP02KG6NFj0sS5lkQ%3DOOm2IEOUkL0sWWLba3WYao4akkHJRHcjGRjr9KfNSmsDpmjFSU'

client = tweepy.Client(BEARER_TOKEN)


# auth = tweepy.OAuthHandler(Api_Key, Api_Key_Secret)

# auth.set_access_token(Access_Token, Access_Token_Secret)

# api = tweepy.API(auth)

#endregion

archivo = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\conjunto.xlsx'

df = pd.read_excel(archivo, sheet_name='2020')

#contador de donde dejamos los followers
cantidad_cerradas = 0
cantidad_suspendidos = 0
result = pd.DataFrame()

for i in range (10):
    print(i)
    try:
        user = client.get_users(ids=df["IdStr"][i])
        userObject = [{"id":user.id, "id_str": user.id_str, "name": user.name, "url": user.url, "description": user.description, "protected": user.protected, "verified": user.verified, "favourites_count": user.favourites_count, "statuses_count": user.statuses_count, "friends_count": user.friends_count, "screen_name": user.screen_name, "followers_count": user.followers_count, "location": user.location, "created_at": user.created_at}]
        df_user = pd.DataFrame(userObject)
        df_user["created_at"] = df_user["created_at"].dt.tz_localize(None)
        result = (pd.concat([result, df_user]))
    except tweepy.errors.NotFound:
        cantidad_cerradas = cantidad_cerradas + 1
    except tweepy.errors.Forbidden:
        cantidad_suspendidos = cantidad_suspendidos + 1

result.to_excel("dataUser.xlsx", sheet_name='Followees')
print("Las cuentas suspendidas fueron: ", cantidad_suspendidos)
print("Las cuentas cerradas fueron: ", cantidad_cerradas)