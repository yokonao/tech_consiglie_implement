import csv
from modules.slack.users import users


def to_csv(json_dict):
    for name in users.values():
        target_dicts = json_dict[name]

        with open('csv/' + name + '.csv', 'w', encoding="utf_8_sig") as f:
            csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
            writer = csv.DictWriter(f, fieldnames=target_dicts[0].keys(), dialect='dialect01')
            writer.writeheader()

            for target_dict in target_dicts:
                writer.writerow(target_dict)
