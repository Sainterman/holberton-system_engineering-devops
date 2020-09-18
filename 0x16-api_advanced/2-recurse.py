#!/usr/bin/python3
""" Get subscribers count from existing subreddit"""

import requests


def recurse(subreddit, after=None, hot_list=[]):
    """ """
    DOMAIN = 'https://www.reddit.com/'
    USER_AGENT = 'linux:subredditscript:v1 (by /u/sancagar)'
    h = {'User-Agent': USER_AGENT}
    URL = DOMAIN + 'r/{}/hot.json'.format(subreddit)
    if after:
        URL += '?after={}'.format(after)
    req = requests.get(URL, headers=h)
    data = req.json().get('data')
    try:
        posts = data.get('children')
    except KeyError:
        return None
    for post in posts:
        hot_list.append(post.get('data')['title'])
    if data['after']:
        return recurse(subreddit, data['after'], hot_list)
    else:
        return hot_list
