import tweepy
import pandas as pd

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "WEg02Z8LzGMJBToJQRr2wgVuJ"
consumer_secret = "9UTprE7IOu8Z6j3ua7RRxHZAzEonBkY7TKbPlPXEt7Fhy5yDlX"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "446462897-f64v0FqKPmC4dtg0lMTfBbpzMLFOs0vWzgU8L24s"
access_token_secret = "xDG33DsCrsXMH6uKXhYXPUlnxMY6GYQLG6ImRynDNnNSt"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

#archivo2023 = r'C:\Users\jamon\OneDrive\Escritorio\Trabajo\Twitter\conjunto.xlsx'

#df2 = pd.read_excel(archivo2023, sheet_name='2020')

screen_name = 'maelosh'

user = api.lookup_users(screen_name=screen_name);

print(user)
