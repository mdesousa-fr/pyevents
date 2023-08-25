subscribers = {}


def subscribe(event_type: str, func: callable):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(func)


def post_event(event_type: str, **kwargs):
    if not event_type in subscribers:
        return
    for func in subscribers[event_type]:
        func(**kwargs)
