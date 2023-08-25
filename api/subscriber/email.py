from api.event.event import subscribe
from utils.email import send_email


def handle_user_registered_event(**kwargs):
    to = kwargs["mail"]
    subject = "Thank you for registering"
    body = f"Hello {kwargs['username']} and welcome!."
    send_email(to, subject, body)


def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
