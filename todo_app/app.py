import os
import random
import time
import urllib.request
from pathlib import Path

from flask import Flask, render_template, send_file

PORT = int(os.getenv("PORT") or "8000")
PIC_TTL_SECONDS = 600
SHARED_FILES_PATH = "files"
PIC_FILE = "placeholder.jpg"
PIC_PATH = os.path.join(SHARED_FILES_PATH, PIC_FILE)

app = Flask(__name__)


def download_random_sized_pic() -> bytes:
    x = 100 * random.randint(1, 10)
    y = x * 3 // 4
    url = f"https://placebear.com/{x}/{y}"
    with urllib.request.urlopen(url, timeout=3) as r:
        return r.read()


def check_and_update_placeholder_pic():
    if (
        not Path(PIC_PATH).is_file()
        or time.time() > Path(PIC_PATH).stat().st_mtime + PIC_TTL_SECONDS
    ):
        with open(PIC_PATH, "wb") as f:
            f.write(download_random_sized_pic())


@app.get("/")
def home():
    check_and_update_placeholder_pic()
    return render_template("index.html")


@app.get("/files/<filename>")
def shared_file(filename):
    return send_file(os.path.join(SHARED_FILES_PATH, filename))


if __name__ == "__main__":
    print(f"Server started in port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)
