from flask import Flask

app = Flask(__name__)


@app.route('/<path:path>', defaults={'path': ''})
def catcher(path: str) -> str:
    return path
