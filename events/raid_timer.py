import time

def raid_ready(last_time):

    now = time.time()

    if now - last_time > 3600:
        return True

    return False
