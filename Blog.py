from bevyframe import Request, Page, Widget, Response
from datetime import datetime
import json


class Super:
    def __init__(self, data):
        self.data = data

    def activity(self, r: Request) -> Response:
        return Response(json.dumps({
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": "Note",
            "id": f"https://islekcaganmert.me/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "published": self.data['datetime'].strftime('%Y-%m-%dT%H:%M:00Z'),
            "attributedTo": "https://islekcaganmert.me/ap/Actor.py",
            "content": "<p>" + self.data['title'] + '</p><p><a href="https://islekcaganmert.me/Blog/' + self.data['datetime'].strftime('%Y%m%d%H%M') + '_' + self.data['id'] + '.py">Read it on web</a></p>',
        }), headers={'Content-Type': r.headers.get('Accept')})

    def get(self, r: Request) -> (Page, Response):
        if 'application/activity+json' in r.headers.get('Accept'):
            return self.activity(r)
        else:
            return Page(
                title=f"{self.data['title']} - Blog de Çağan Mert İŞLEK",
                description=self.data['content'][:100],
                selector='body_blank',
                OpenGraph={
                    'title': self.data['title'],
                    'description': self.data['content'][:100],
                    'image': (
                        self.data['content'].split('<img')[1].split('src="')[1].split('"')[0]
                        if '<img' in self.data['content'] else ''
                    ),
                    'url': f"https://islekcaganmert.me/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
                    'type': 'article',
                    'site_name': 'Blog de Çağan Mert İŞLEK',
                    'article:published_time': self.data['datetime'].strftime('%B %d, %Y'),
                    'article:author': 'Çağan Mert İŞLEK'
                },
                icon={
                    'href': '/static/favicon.png',
                    'type': 'image/x-icon'
                },
                childs=[
                    Widget(
                        'div',
                        style={
                            'position': 'absolute',
                            'top': '10px',
                            'right': '30px',
                            'left': '30px',
                            'bottom': '0px',
                            'y-overflow': 'scroll'
                        },
                        childs=[
                            Widget('p', childs=[Widget('a', href='/', innertext='Turn to homepage', style={
                                'color': 'blue',
                                'text-decoration': 'underline'
                            })]),
                            Widget('p', style={
                                'font-size': '0.8em',
                                'color': '#80808080'
                            }, childs=[Widget('i', childs=[
                                'Posted by Çağan Mert İŞLEK on ',
                                self.data['datetime'].strftime('%B %d, %Y')
                            ])]),
                            Widget('h1', innertext=self.data['title']),
                            Widget('p', innertext=self.data['content']),
                            '''
<p>&nbsp;</p><p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="https://creativecommons.org/licenses/by-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;color:blue;text-decoration:underline">CC BY-ND 4.0</a></p>
                            '''  # CreativeCommons
                        ]
                    )
                ]
            )
