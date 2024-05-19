from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def catcher() -> str:
    return render_template('index.html')
