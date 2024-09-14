from bevyframe import *
import hereus_ui_3_2

app = Frame(
    package='me.islekcaganmert.www',
    developer='islekcaganmert@hereus.net',
    administrator=None,
    secret=open('./secret').read(),
    style=hereus_ui_3_2,
    icon='/static/favicon.png',
    keywords=['Test'],
    permissions=[]
)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
