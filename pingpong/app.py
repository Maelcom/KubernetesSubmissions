import os

from flask import Flask

PORT = int(os.getenv("PORT") or "8002")
app = Flask(__name__)

requests_counter = 0


@app.get("/pingpong")
def count():
    global requests_counter
    response = f"pong {requests_counter}"
    requests_counter += 1
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
