#!/usr/bin/python3
""" top_ten module """


import requests


def top_ten(subreddit):
    """ top_ten function """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'CustomAgent/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))
    else:
        print(None)
