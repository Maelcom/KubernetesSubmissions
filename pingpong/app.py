import logging
import os

from flask import Flask

PORT = int(os.getenv("PORT") or "8002")
PINGPONG_COUNTER_FILE = os.getenv("PINGPONG_COUNTER_FILE", "pong-count.txt")
logger = logging.getLogger(__name__)
app = Flask(__name__)

requests_counter = 0


@app.get("/pingpong")
def count():
    global requests_counter
    response = f"pong {requests_counter}"

    try:
        with open(PINGPONG_COUNTER_FILE, "w") as f:
            f.write(str(requests_counter))
    except OSError:
        logger.exception(f"Failed to write counter to {PINGPONG_COUNTER_FILE}")

    requests_counter += 1
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
