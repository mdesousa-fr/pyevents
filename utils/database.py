db = {}


def add_entry(entry_id: str, data: dict) -> bool:
    if entry_id in db:
        return False
    db.update({entry_id: data})
    return True


def del_entry(entry_id: str) -> bool:
    if entry_id not in db:
        return False
    db.pop(entry_id)
    return True


def get_entry(entry_id: str) -> dict:
    if entry_id not in db:
        return {}
    return db[entry_id]
