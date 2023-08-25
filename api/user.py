from dataclasses import asdict, dataclass

import utils.database
from api.event.event import post_event


@dataclass
class User:
    username: str
    name: str
    mail: str


def register_user(username: str, name: str, mail: str):
    user = User(username, name, mail)
    utils.database.add_entry(username, asdict(user))
    post_event("user_registered", **asdict(user))
