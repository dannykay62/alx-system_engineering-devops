#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, hot_list=[], viewed_count=0, after=''):
    """queries the Reddit API, parses the title of all hot articles, and 
    prints a sorted count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript, but java should not).
    """
    base_url = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_str = '?show="all"&limit=100&after={}&count={}'.format(after,
            viewed_count)
    url = base_url + endpoint + query_str
    headers = {'User-Agent': 'Python/3.0(Alx 0x16 task 3)'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        return
    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        count_words(subreddit, [], hot_list, viewed_count + dist, after)

    if viewed_count == 0:
        result = {}
        word_list = [word.lower() for word in word_list]
        hot_words = ' '.join(hot_list).lower().split(' ')
        for hot_word in hot_words:
            for search_word in word_list:
                if hot_word == search_word:
                    result.setdefault(search_word, 0)
                    result[search_word] += 1

        for word, count in sorted(sorted(result.items()), key=lambda x: x[1],
                reverse=True):
            print("{}: {}".format(word, count))
