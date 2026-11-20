import datetime as dt
import os
import time
import uuid

RANDOM_STRING = uuid.uuid4()
LOG_FILE = os.getenv("LOG_FILE", "log.txt")


def status_string():
    timestamp = dt.datetime.now().isoformat(timespec="milliseconds")
    return f"{timestamp}: {RANDOM_STRING}"


def log_loop():
    while True:
        time.sleep(5)
        with open(LOG_FILE, "a") as f:
            f.write(f"{status_string()}\n")


if __name__ == "__main__":
    log_loop()
