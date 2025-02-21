#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the top 10 hot posts of a given subreddit.

    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:top_ten_script:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False, timeout=5
        )

        # Check if subreddit exists (Reddit returns 302 or 404 for invalid subreddits)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"].get("title", "No Title"))

    except (requests.RequestException, ValueError, KeyError):
        print(None)
