import logging
import os
import random
import time
import urllib.request
from pathlib import Path

import requests
from flask import Flask, render_template, send_file

PORT = int(os.getenv("PORT") or "8000")
PIC_TTL_SECONDS = 600
SHARED_FILES_PATH = "files"
PIC_FILE = "placeholder.jpg"
PIC_PATH = os.path.join(SHARED_FILES_PATH, PIC_FILE)
TODOS_BACKEND_URL = os.getenv("TODOS_BACKEND_URL") or "/todos"

logger = logging.getLogger(__name__)
app = Flask(__name__)


def download_random_sized_pic() -> bytes:
    x = 100 * random.randint(1, 10)
    y = x * 3 // 4
    url = f"https://placebear.com/{x}/{y}"
    r = requests.get(url, timeout=3)
    r.raise_for_status()
    return r.content


def check_and_update_placeholder_pic():
    if (
        not Path(PIC_PATH).is_file()
        or time.time() > Path(PIC_PATH).stat().st_mtime + PIC_TTL_SECONDS
    ):
        with open(PIC_PATH, "wb") as f:
            f.write(download_random_sized_pic())

def get_todos():
    try:
        r = requests.get(TODOS_BACKEND_URL, timeout=3)
        r.raise_for_status()
        return r.json()
    except Exception:
        logger.exception("Failed to get_todos")
        return []

@app.get("/")
def home():
    check_and_update_placeholder_pic()
    return render_template("index.html", todos=get_todos())


@app.get("/files/<filename>")
def shared_file(filename):
    return send_file(os.path.join(SHARED_FILES_PATH, filename))


if __name__ == "__main__":
    print(f"Server started in port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)
