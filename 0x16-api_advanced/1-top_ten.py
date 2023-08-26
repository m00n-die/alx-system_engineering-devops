#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    headers = {"User-Agent": "0x16. API_advanced-m00n-die"}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    params = {"limit": 10}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return
    json_res = res.json().get("data")

    for child in json_res.get("children"):
        print(child.get("data").get("title"))
