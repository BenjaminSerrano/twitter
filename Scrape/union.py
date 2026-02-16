import pandas as pd

# Cargar ambos archivos Excel
tweets_df = pd.read_excel('Tweets.xlsx')
conjunto_df = pd.read_excel('users.xlsx')
resultado = pd.DataFrame()

i = 0
 
while(len(conjunto_df))> i:
    j = 0
    while(len(tweets_df) > j):
        if(conjunto_df["@"][i] == tweets_df["Usuario"][j]):
            userDataframe = [{"id":conjunto_df['id'][i], 
                              "Name in header":conjunto_df['Name in header'][i], 
                              "Description":conjunto_df['Description'][i], 
                              "Protected": conjunto_df['Protected'][i],
                              "Verified": conjunto_df['Verified'][i], 
                              "Likes of all time":conjunto_df['Likes of all time'][i], 
                              "Followers":conjunto_df['Followers'][i], 
                              "Friends":conjunto_df['Friends'][i], 
                              "Location": conjunto_df['Location'][i], 
                              "@":conjunto_df['@'][i], 
                              "Location": conjunto_df['Location'][i], 
                              "Sensitive content": conjunto_df['Sensitive content'][i], 
                              "Created at":conjunto_df['Created at'][i],
                              "Usuario": tweets_df["Usuario"][j],
                              "Estado": tweets_df["Estado"][j],
                              "1° Tweet": tweets_df["1° Tweet"][j],
                              "¿Es Retweet el 1° Tweet?": tweets_df["¿Es Retweet el 1° Tweet?"][j],
                              "2° Tweet": tweets_df["2° Tweet"][j],
                              "¿Es Retweet el 2° Tweet?": tweets_df["¿Es Retweet el 2° Tweet?"][j],
                              "3° Tweet": tweets_df["3° Tweet"][j],
                              "¿Es Retweet el 3° Tweet?": tweets_df["¿Es Retweet el 3° Tweet?"][j],
                              "4° Tweet": tweets_df["4° Tweet"][j],
                              "¿Es Retweet el 4° Tweet?": tweets_df["¿Es Retweet el 4° Tweet?"][j],
                              "5° Tweet": tweets_df["5° Tweet"][j],
                              "¿Es Retweet el 5° Tweet?": tweets_df["¿Es Retweet el 5° Tweet?"][j],
                              "Fecha de creación del primer tweet": tweets_df["Fecha de creación del primer tweet"][j]}]
            df_temp = pd.DataFrame(userDataframe)
            resultado = (pd.concat([resultado, df_temp]))
            break
        j = j + 1
    i = i + 1
    print(i)

resultado.to_excel("Final.xlsx")