from bevyframe import *
from TheProtocols import User
import os

app = Frame(
    package="me.islekcaganmert.www",
    developer="islekcaganmert@hereus.net",
    secret=os.environ.get('SECRET'),
    style="https://static.hereus.net/hereus_ui_4_0.css",
    icon=User(os.environ.get('USER', 'demo@hereus.net')).profile_photo,
    keywords=[],
    permissions=[],
    environment={
        'user': os.environ.get('USER', 'demo@hereus.net'),
        'github': os.environ.get('GITHUB', '').removeprefix('@'),
        'domain': os.environ.get('DOMAIN'),
        'social': {
            'fediverse': os.environ.get('FEDIVERSE', '@@'),
            'x': os.environ.get('TWITTER', '').removeprefix('@'),
            'linkedin': os.environ.get('LINKEDIN', '').removeprefix('@'),
            'instagram': os.environ.get('INSTAGRAM', '').removeprefix('@'),
            'youtube': os.environ.get('YOUTUBE', '').removeprefix('@'),
            'discord': os.environ.get('DISCORD', ''),
            'reddit': os.environ.get('REDDIT', '').removeprefix('/').removeprefix('u/'),
        },
        'banner': os.environ.get('BANNER', ''),
        'bio': os.environ.get('BIO', '').replace('\\n', '\n').strip('\n').strip().split('\n'),
        'job': {
            'title': os.environ.get('JOB_TITLE', ''),
            'company': os.environ.get('COMPANY', '')
        },
        'education': {
            'degree': os.environ.get('DEGREE', ''),
            'school': os.environ.get('SCHOOL', '')
        },
        'mbti': os.environ.get('MBTI', ''),
        'location': os.environ.get('LOCATION', ''),
        'email': os.environ.get('EMAIL', ''),
        'theme': os.environ.get('THEME', 'blank'),
    }
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
            