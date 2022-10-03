import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#climatechange) lang:en until:2022-08-30 since:2022-02-25"
tweets = []
limit = 1000000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('tweets_climatechange.csv')