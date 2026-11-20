import os

from flask import Flask, Response

PORT = int(os.getenv("PORT") or "8001")
LOG_FILE = os.getenv("LOG_FILE", "log.txt")
app = Flask(__name__)


@app.get("/")
def home():
    with open(LOG_FILE, "r") as f:
        return Response(f.read(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
