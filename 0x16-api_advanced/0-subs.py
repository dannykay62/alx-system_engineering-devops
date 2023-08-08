#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python/3.0 (ALX 0x16 task 0)"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0

    except requests.executions.RequestException as e:
        printf(f"Error: {e}")
        return 0

    subreddt_name = "python"
    subscribers = name_of_subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")