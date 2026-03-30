listeners = []

def register_listener(fn):
    listeners.append(fn)

def emit_event(message):
    for fn in listeners:
        fn(message)