from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html')


@app.route('/.well-known/web-meta')
def web_meta():
    return redirect('https://web.brid.gy/.well-known/web-meta')


@app.route('/.well-known/webfinger')
def webfinger():
    return redirect(f'https://web.brid.gy/.well-known/webfinger?resource={request.args['resource']}')
