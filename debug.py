from bevyframe import Frame, Request, Response, redirect
import json

app = Frame(
    package='me.islekcaganmert.www',
    developer='islekcaganmert@hereus.net',
    administrator=True,
    secret=open('./secret', 'r').read(),
    style='https://github.com/hereus-pbc/HereUS-UI-3.1/raw/master/HereUS-UI-3.1.json',
    icon='/static/favicon.png',
    keywords=['Test']
)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
