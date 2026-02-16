from tweety import Twitter
  
app = Twitter("session")

app.sign_in("BarBenjaTaza", "19154492-7")

# assuming app is authenticated class instance
  
all_tweets = app.get_tweets("elonmusk")
for tweet in all_tweets:
  print(tweet)