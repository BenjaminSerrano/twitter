import pandas as pd
import tweepy
from datetime import datetime

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKUjnwEAAAAAkxYlI0EnfNv6ysCykgyrYpwYRGc%3DkWWH28PP6YXEauMXiZ2sbqtqtA1QQeY5cerlb9OI7vitBZeXy9'

client = tweepy.Client(BEARER_TOKEN)

archivo = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\[2023] far-right\Teremarinovic_Actual.xlsx'

df = pd.read_excel(archivo, sheet_name='Followees')

date_tweets = []

for i in range (800):
    print(i)
    if(df['protected'][i] == False):
        tweets = client.get_users_tweets(id=df["id_str"][i], max_results=5, tweet_fields=['created_at'])
        if(tweets.data != None):
            invalid_format = tweets.data[0].created_at
            format = invalid_format.strftime("%Y-%m-%d %H:%M:%S")
            date_tweets.append(format)
        else:
            data = 'No data'
            date_tweets.append(data)
    if(df['protected'][i] == True):
        protected = 'Protected'
        date_tweets.append(protected)

final = pd.DataFrame(date_tweets, columns=['last_activity'])
final.to_excel("dates1.xlsx")