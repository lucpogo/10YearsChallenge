#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import os

if os.path.exists(os.path.join('files','instagram')):
    if os.path.isfile(os.path.join('files','instagram','Instagram.json')):
        with open(os.path.join('files','instagram','Instagram.json'),'rt') as f:
            instagramJSON = json.loads(f.read())
    else:
        instagramJSON = []
else:
    os.makedirs(os.path.join('files','instagram'))
    os.makedirs(os.path.join('files','instagram','pictures'))
    instagramJSON = []

has_next_page = True
queryOriginal = "https://www.instagram.com/explore/tags/10yearschallenge/?__a=1"
query = queryOriginal

while has_next_page:
    with urllib.request.urlopen(query) as url:
        front = json.loads(url.read().decode())
    instagramJSON.extend(front['graphql']['hashtag']['edge_hashtag_to_media']['edges'])
    for edge in front['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
        shortcode = edge['node']['shortcode']
        try:
            with urllib.request.urlopen("https://www.instagram.com/p/"+shortcode+"/?__a=1") as url:
                data = json.loads(url.read().decode())
            if 'edge_sidecar_to_children' in data['graphql']['shortcode_media']:
                i=1
                for e in data['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
                    urllib.request.urlretrieve(e['node']['display_resources'][-1]['src'],os.path.join('files','instagram','pictures',shortcode+'_'+str(i)+'jpg'))
                    i+=1
            else:
                urllib.request.urlretrieve(data['graphql']['shortcode_media']['display_resources'][-1]['src'],os.path.join('files','instagram','pictures',shortcode+'_1.jpg'))
        except:
            pass
    has_next_page = front['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    query = queryOriginal + "&max_id=" + front['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']

with open(os.path.join('files','instagram','Instagram.json'),'wt') as f:
    json.dump(instagramJSON,f,indent=2)

print("Fin del Proceso")
