from api.event.event import subscribe
from utils.slack import send_slack_message


def handle_user_registered_event(**kwargs):
    message = f"The user {kwargs['username']} have been registered."
    send_slack_message(message)


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
