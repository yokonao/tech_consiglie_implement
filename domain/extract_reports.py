import re
import datetime
from modules.slack.to_user import to_user, users


def extract_reports(messages):
    regex = "[0-9]+:[0-9]+"
    pattern = re.compile(regex)

    reports = {}
    for user in users.values():
        reports[user] = []

    for message in messages:
        text = message['text']
        if ('作業' in text):
            matchObjects = pattern.findall(text)
            if len(matchObjects) >= 2:
                date = datetime.date.fromtimestamp(float(message['ts']))
                user = to_user(message['user'])
                start = matchObjects[0]
                end = matchObjects[1]
                reports[user].append({"date": date.strftime('%Y/%m/%d'),
                                      "user": user, "start": start, "end": end})

    return reports
