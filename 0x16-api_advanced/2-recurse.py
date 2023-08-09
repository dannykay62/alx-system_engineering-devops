#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit
    """
    real = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_str = '?show="all"&limit=100&after={}&count={}'.format(after, count)
    url = real + endpoint + query_str
    headers = {'User-Agent': 'Python/3.0(Alx 0x16 task 2)'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        if len(hot_list) == 0:
            return None
        else:
            return hot_list

    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        recurse(subreddit, hot_list, count + dist, after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list
