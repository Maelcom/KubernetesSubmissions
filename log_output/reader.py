import os

from flask import Flask, Response

PORT = int(os.getenv("PORT") or "8001")
LOG_FILE = os.getenv("LOG_FILE", "log.txt")
PINGPONG_COUNTER_FILE = os.getenv("PINGPONG_COUNTER_FILE", "pong-count.txt")
app = Flask(__name__)


@app.get("/")
def home():
    with open(LOG_FILE, "r") as log, open(PINGPONG_COUNTER_FILE, "r") as pong:
        resp = f"{log.read()}\nPing / Pongs: {pong.read()}"
        return Response(resp, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
