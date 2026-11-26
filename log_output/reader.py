import logging
import os

import requests
from flask import Flask, Response

PORT = int(os.getenv("PORT") or "8001")
LOG_FILE = os.getenv("LOG_FILE", "log.txt")
PONG_COUNT_URL = os.getenv("PONG_COUNT_URL", "")
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.get("/")
def home():
    pong_count = None
    try:
        pong_count = requests.get(PONG_COUNT_URL, timeout=2).text
    except requests.RequestException:
        logger.exception("failed to get pong count")

    with open(LOG_FILE, "r") as log:
        resp = f"{log.read()}\nPing / Pongs: {pong_count}"
        return Response(resp, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
