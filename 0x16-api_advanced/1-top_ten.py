#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Querries the reddit API and prints titles of 10 hottest posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
            subreddit)
    headers = {'User-Agent': 'Python/3.0(Alx 0016)'}
    response = requests.get(url, headers=headers)
    try:
        topten = response.json()['data']['children']
        for post in topten:
            print(post['data']['title'])
    except KeyError:
        print("None")
