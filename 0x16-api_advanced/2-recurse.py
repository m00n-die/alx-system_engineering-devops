#!/usr/bin/python3
"""ecursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """return list containing titles of all hot articles"""
    headers = {"User-Agent": "0x16. API_advanced-m00n-die"}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    params = {"limit": 50, "next_page": next_page, "count": count}

    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)

    if res.status_code != 200:
        return None
    json_res = res.json().get("data")
    next_page = json_res.get("next_page")
    count += json_res.get("dist")
    children = json_res.get("children")

    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)
        return hot_list
