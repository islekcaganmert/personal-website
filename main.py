from bevy2flask import Frame
from bevyframe import Request, redirect, Response
import requests

app = Frame(
    package='dev.islekcaganmert.www',
    developer='islekcaganmert@hereus.net',
    administrator=True,
    secret=open('./secret', 'r').read(),
    style='https://github.com/hereus-pbc/HereUS-UI-3.1/raw/master/HereUS-UI-3.1.json',
    icon='/static/favicon.png',
    keywords=['Test']
)


@app.route('/.well-known/web-meta')
def web_meta(r: Request):
    return redirect('https://web.brid.gy/.well-known/web-meta')


@app.route('/.well-known/webfinger')
def webfinger(r: Request):
    return Response('', status_code=302, headers={'location': f"https://web.brid.gy/{r.path}"})
# redirect(f"https://web.brid.gy{r.path}")


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, True, True)
