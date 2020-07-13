from modules.slack.message_lists import message_lists
from domain.extract_reports import extract_reports
from domain.to_csv import to_csv
import json
import os


def main():
    os.makedirs('json', exist_ok=True)
    os.makedirs('csv', exist_ok=True)

    channel_id = os.getenv("CHANNEL_ID")
    messages = message_lists(channel_id)
    reports = extract_reports(messages)

    with open('json/daily_reports.json', 'w') as fw:
        json.dump(reports, fw)

    to_csv(reports)


if __name__ == "__main__":
    main()
