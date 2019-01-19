#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler
import json
import time
import urllib.request
import os

with open('config.json') as f:
    config = json.load(f)

configTwitter = config['twitter']

auth = OAuthHandler(configTwitter['consumer_key'], configTwitter['consumer_secret'])
auth.set_access_token(configTwitter['access_token'], configTwitter['access_token_secret'])

api = tweepy.API(auth)

parametros={'q':'10%20year%20challenge%20-filter:retweets','count':100}

if os.path.exists(os.path.join('files','twitter')):
    if os.path.isfile(os.path.join('files','twitter','Tweets.json')):
        with open(os.path.join('files','twitter','Tweets.json'),'rt') as f:
            tweetsJSON = json.loads(f.read())
            parametros['min_id'] = str(max([x['id'] for x in tweetsJSON]))
    else:
        tweetsJSON = []
else:
    os.makedirs(os.path.join('files','twitter'))
    os.makedirs(os.path.join('files','twitter','pictures'))
    tweetsJSON = []

def downloadPics(parametros):
    tlen=0
    while tlen!=0:
        time.sleep(5)
        newTweets = api.search(**parametros)
        tlen = len(newTweets)
        if tlen>0:
            filtered = [x for x in [x._json for x in newTweets] if 'extended_entities' in x]
            tweetsJSON.extend(filtered)
            for tweet in filtered:
                i=1
                for m in tweet['extended_entities']['media']:
                    if m['type']=='photo':
                        urllib.request.urlretrieve(m['media_url'], os.path.join('files','twitter','pictures','{}_{}.{}'.format(tweet['id_str'],str(i),m['media_url'].split('.')[-1])) )
                        i+=1
            parametros['max_id']=min([int(x.id) for x in newTweets])-1

downloadPics(parametros)

with open(os.path.join('files','twitter','Tweets.json'),'wt') as f:
    json.dump(tweetsJSON,f,indent=2)

print("Fin del Proceso")