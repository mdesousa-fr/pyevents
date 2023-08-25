import json

from faker import Faker

from api.subscriber.email import setup_email_event_handlers
from api.subscriber.slack import setup_slack_event_handlers
from api.user import register_user
from utils.database import db


def main():
    setup_slack_event_handlers()
    setup_email_event_handlers()

    fake = Faker()
    for _ in range(10):
        profile = fake.simple_profile()
        register_user(profile["username"], profile["name"], profile["mail"])

    print(json.dumps(db, indent=2))


if __name__ == "__main__":
    main()
