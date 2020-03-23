# %% GET NAMES OF PERSONS WINNING AWARDS

import json
import re

from names_dataset import NameDataset
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import twitter

# defining object for names_dataset
m = NameDataset()

# defining of stopwords
stop_words = set(stopwords.words('english'))

# passing keys
key = "key"
secret_key = "secret_key"
access_token_key = "access_token_key"
access_token_secret = "access_token_secret"

# authenication
api = twitter.Api(consumer_key=key, consumer_secret=secret_key, access_token_key=access_token_key,
                  access_token_secret=access_token_secret)
count = 100
search_query = "congratulations winner"

# passing query to twitter api
results = api.GetSearch(raw_query="q=" + search_query + "&result_type=top&count=" + str(count))
tweets = []
# getting only text from tweets
for tweet in results:
    tweets.append(json.loads(str(tweet))['text'])  # all the tweets text

cleaned_tweets = []
# cleaning the tweets keeping only alphabets
for tweet in tweets:
    clean_tweet = re.sub('[^A-Za-z ]+', '', tweet)
    cleaned_tweets.append(clean_tweet)

tokenized_tweets = []
for tweet in cleaned_tweets:
    # tokenizing
    tokenized_tweets.append(word_tokenize(tweet))

names_list = []
# removing stopwords from tokenized tweets
stop_words.update(
    ["congratulations", "winner", "oscar", "oscars", "last", "night", "rt", "sent", "dm", "big", "best", "new", "tweet",
     "happy"])

for tweet in tokenized_tweets:
    temp = []
    for word in set(tweet):
        if word.lower() not in stop_words:
            # checking if that word is a name of person
            if m.search_first_name(word.lower()) or m.search_last_name(word.lower()):
                temp.append(word.lower())
                # joining first name and last name
                if len(temp) > 1:
                    temp = [" ".join(temp)]
    # adding name in list if present
    if len(temp) != 0:
        if temp not in names_list:
            if isinstance(temp, list):
                names_list.append(temp[0])
            else:
                names_list.append(temp)

print("Names of winners: ")
print(set(names_list))
