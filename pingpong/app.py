import logging
import os

from flask import Flask

PORT = int(os.getenv("PORT") or "8002")
logger = logging.getLogger(__name__)
app = Flask(__name__)

requests_counter = 0


@app.get("/pingpong")
def count():
    global requests_counter
    requests_counter += 1
    return f"pong {requests_counter}"


@app.get("/pings")
def get_pings():
    return f"{requests_counter}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
