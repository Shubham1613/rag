import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)


def save_message(session_id, role, content):

    key = f"chat:{session_id}"

    history = r.get(key)

    if history:
        history = json.loads(history)
    else:
        history = []

    history.append({"role": role, "content": content})

    r.set(key, json.dumps(history))


def get_history(session_id):

    key = f"chat:{session_id}"

    history = r.get(key)

    if history:
        return json.loads(history)

    return []