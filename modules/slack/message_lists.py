import os
import requests

slack_token = os.getenv("SLACK_TOKEN")


def message_lists(channel_id):
    url = 'https://slack.com/api/conversations.history'
    params = {"token": slack_token, "channel": channel_id}
    res = requests.get(url, params=params)
    jsonData = res.json()

    if not jsonData['ok']:
        raise Exception(jsonData['error'])
        return

    messages = jsonData['messages']
    return messages
