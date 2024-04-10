#!/usr/bin/python3
""" top_ten module """


import requests


def top_ten(subreddit):
    """ top_ten function """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'CustomAgent/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get('data').get('children')[i]
                  .get('data').get('title'))
    else:
        print(None)
