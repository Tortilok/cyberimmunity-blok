# Политики безопасности
policies = (
    {"src": "con", "dst": "chipher"},
    {"src": "chipher", "dst": "con"},
    {"src": "chipher", "dst": "can"},
    {"src": "chipher", "dst": "trustCan"},
    {"src": "can", "dst": "chipher"},
    {"src": "can", "dst": "pri"},
    {"src": "can", "dst": "tskbm"},
    {"src": "can", "dst": "bi"},
    {"src": "can", "dst": "trustCan"},
    {"src": "tskbm", "dst": "can"},
    {"src": "iy", "dst": "can"},
    {"src": "saytp", "dst": "can"},
    {"src": "rpdp", "dst": "can"},

    {"src": "bvi", "dst": "trustCan"},
    {"src": "pir", "dst": "trustCan"},
    {"src": "oskp", "dst": "trustCan"},
    {"src": "trustCan", "dst": "rpdp"},
    {"src": "trustCan", "dst": "saytp"},
    {"src": "trustCan", "dst": "iy"}
)

def check_operation(id, details) -> bool:
    """ Проверка возможности совершения обращения. """
    src: str = details.get("source")
    dst: str = details.get("deliver_to")

    if not all((src, dst)):
        return False

    print(f"[info] checking policies for event {id}, {src}->{dst}")

    return {"src": src, "dst": dst} in policies
