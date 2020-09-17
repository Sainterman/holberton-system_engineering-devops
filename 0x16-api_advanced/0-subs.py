#!/usr/bin/python3
""" Get subscribers count from existing subreddit"""

import requests
import json


DOMAIN = 'https://www.reddit.com/'

USER_AGENT = 'linux:subredditscript:v1 (by /u/sancagar)'


def number_of_subscribers(subreddit):
    h = requests.utils.default_headers()
    h.update({'User-Agent': USER_AGENT})
    req = requests.get(DOMAIN + 'r/{}/about.json'.format(subreddit), headers=h)
    data = req.json()['data']
    if data.get('subscribers') is None:
        return(0)
    return(data.get('subscribers'))
