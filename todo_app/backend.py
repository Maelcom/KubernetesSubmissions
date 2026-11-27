import os

from flask import Flask, jsonify, redirect, request

PORT = int(os.getenv("PORT") or "8000")

app = Flask(__name__)
todos_storage = []


@app.get("/todos")
def get_todos_list():
    return jsonify(todos_storage)


@app.post("/todos")
def create_todo():
    text = request.form.get("todo-input", "").strip()
    if text:
        todos_storage.append(text)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
