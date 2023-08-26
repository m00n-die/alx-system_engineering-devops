#!/usr/bin/python3
"""
returns the total number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    headers = {"User-Agent": "0x16. API_advanced-m00n-die"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    subs = res.json().get("data").get("subscribers")
        return subs
