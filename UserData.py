# import the module
import tweepy
import pandas as pd
#from UserObject import * 

# assign the values accordingly
Api_Key = 'pMFZTdFIwJJE8VkZNBIN7Ehly'
Api_Key_Secret = 'LjFj8S7XojspkzIXOerz7MELZFuol1dBsYp6Rp6xED6x3JVrso'
Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAALzrFgEAAAAAzGr7mDLK0SVjrSKvej7i7lzz8dM%3Dp6kJE6sQvuC24SisN4xPh1UEJCrMh4DTwJtyZbmCTYPGU1AkIs'
Access_Token = '446462897-Oi0mmOfXlNJj8h2CFeRi5qzeCMeg73E68ZQYkffQ'
Access_Token_Secret = 'oIO5TrOltMYpSjWY2ot6PktPfi9QjY9v4dT1pwyr8CXsC'
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(Api_Key, Api_Key_Secret)
  
# set access to user's access key and access secret 
auth.set_access_token(Access_Token, Access_Token_Secret)
  
# calling the api 
api = tweepy.API(auth)
  
# using get_user with id
_id = "993632161382174721"
name = "LaniBSide"

#_id = "993632161382174721"
#name = "Leviata02126425"

#_id = "1192515485801340930"
#name = "CA56752127"


user = api.get_user(user_id = _id, screen_name = name)
#user = api.get_user(user_id = name)
  
# printing the name of the user
#print(user.id)
#print(user.id, user.id_str, user.name, user.url, user.protected, user.verified, user.favourites_count, user.statuses_count, user.friends_count, user.screen_name, user.followers_count, user.location, user.created_at)

userObject = [{"id":user.id, "id_str": user.id_str, "name": user.name, "url": user.url, "description": user.description, "protected": user.protected, "verified": user.verified, "favourites_count": user.favourites_count, "statuses_count": user.statuses_count, "friends_count": user.friends_count, "screen_name": user.screen_name, "followers_count": user.followers_count, "location": user.location, "created_at": user.created_at}]

#print(userObject)

df = pd.DataFrame(userObject)

df["created_at"] = df["created_at"].dt.tz_localize(None)

#print(df)

df.to_excel("dataUser.xlsx")