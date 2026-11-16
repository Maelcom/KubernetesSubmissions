import os

from flask import Flask

PORT = int(os.getenv("PORT") or "8000")
app = Flask(__name__)


@app.get("/")
def home():
    return "Hello"


if __name__ == "__main__":
    print(f"Server started in port {PORT}", flush=True)
    app.run(host="0.0.0.0", port=PORT)
