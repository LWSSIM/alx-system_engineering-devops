#!/usr/bin/python3
"""recurse module"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """recurse function"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(subreddit, after)
    headers = {'User-Agent': 'CustomAgent/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
