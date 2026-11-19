import datetime as dt
import os
import threading
import time
import uuid

from flask import Flask

PORT = int(os.getenv("PORT") or "8001")
app = Flask(__name__)

RANDOM_STRING = uuid.uuid4()

@app.get("/")
def home():
    return status_string()


def status_string():
    timestamp = dt.datetime.now().isoformat(timespec="milliseconds")
    return f"{timestamp}: {RANDOM_STRING}"


def log_loop():
    while True:
        time.sleep(5)
        print(status_string(), flush=True)


if __name__ == "__main__":
    threading.Thread(target=log_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)
