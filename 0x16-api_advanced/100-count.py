#!/usr/bin/python3
"""count"""


import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """count words"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyUserAgent/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
    if after is None:
        if not len(word_dict) > 0:
            print()
            return
        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(key, value))
    else:
        return count_words(subreddit, word_list, after, word_dict)
