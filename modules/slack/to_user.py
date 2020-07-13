from modules.slack.users import users


def to_user(user_id):
    try:
        user = users[user_id]
        return user
    except KeyError:
        return 'No User'
