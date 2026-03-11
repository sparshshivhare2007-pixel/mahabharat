import time

def cooldown(last,seconds):

    now = time.time()

    if now-last > seconds:
        return True

    return False
