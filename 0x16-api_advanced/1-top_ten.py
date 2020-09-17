#!/usr/bin/python3
""" Get subscribers count from existing subreddit"""

import requests


def top_ten(subreddit):
    """ Request about.json to subredit"""
    DOMAIN = 'https://www.reddit.com/'
    USER_AGENT = 'linux:subredditscript:v1 (by /u/sancagar)'
    h = {'User-Agent': USER_AGENT}
    URL = DOMAIN + 'r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(URL, headers=h)
    data = req.json().get('data')
    if data is None:
        print('None')
        return
    posts = data.get('children')
    if len(posts) == 0:
        print('None')
        return
    for post in posts:
        print(post.get('data')['title'])
    return
