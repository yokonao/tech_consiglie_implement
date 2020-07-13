import os
import requests

slack_token = os.getenv("SLACK_TOKEN")


def channel_lists(channel_type):
    url = 'https://slack.com/api/users.conversations'
    params = {"token": slack_token, "types": channel_type}
    res = requests.get(url, params=params)
    jsonData = res.json()

    if not jsonData['ok']:
        raise Exception(jsonData['error'])
        return

    return jsonData['channels']
