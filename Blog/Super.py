from bevyframe import Request, Page, Widget
from datetime import datetime, UTC


class Super:
    def __init__(self, data):
        self.data = {
            'id': '',
            'title': '',
            'content': '',
            'datetime': datetime.now(UTC)
        }

    def activity(self, r: Request) -> dict:
        return {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                {
                    "ostatus": "http://ostatus.org#",
                    "atomUri": "ostatus:atomUri",
                    "inReplyToAtomUri": "ostatus:inReplyToAtomUri",
                    "conversation": "ostatus:conversation",
                    "sensitive": "as:sensitive",
                    "toot": "http://joinmastodon.org/ns#",
                    "votersCount": "toot:votersCount",
                    "Hashtag": "as:Hashtag"
                }
            ],
            "id": f"https://islekcaganmert.vercel.app/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "type": "Note",
            "summary": None,
            "inReplyTo": None,
            "published": "2024-06-06T14:55:49Z",
            "url": f"https://islekcaganmert.vercel.app/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "attributedTo": "https://islekcaganmert.vercel.app/activitypub.json",
            "to": [
                "https://www.w3.org/ns/activitystreams#Public"
            ],
            "cc": [
                "https://islekcaganmert.vercel.app/ap/Followers.py"
            ],
            "sensitive": False,
            "atomUri": f"https://islekcaganmert.vercel.app/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "inReplyToAtomUri": None,
            "conversation": f"tag:islekcaganmert.vercel.app,{self.data['datetime'].strftime('%Y-%m-%d')}:objectId={self.data['datetime'].strftime('%Y%m%d%H%M')}:objectType=Conversation",
            "content": "<p>" + self.data['title'] + '</p><p><a href="https://islekcaganmert.vercel.app/Blog/' + self.data['datetime'].strftime('%Y%m%d%H%M') + '_' + self.data['id'] + '.py">Read it on web</a></p>',
            "contentMap": {
                "en": "<p>" + self.data['title'] + '</p><p><a href="https://islekcaganmert.vercel.app/Blog/' + self.data['datetime'].strftime('%Y%m%d%H%M') + '_' + self.data['id'] + '.py">Read it on web</a></p>'
            },
            "attachment": [],
            "tag": [],
            "replies": {
                "id": f"https://islekcaganmert.vercel.app/ap/Replies/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}",
                "type": "Collection",
                "first": {
                    "type": "CollectionPage",
                    "next": f"https://islekcaganmert.vercel.app/ap/Replies/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}",
                    "partOf": f"https://islekcaganmert.vercel.app/ap/Replies/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}",
                    "items": []
                }
            }
        }

    def get(self, r: Request) -> (Page, dict):
        if 'application/activity+json' in r.headers.get('Accept'):
            return self.activity(r)
        else:
            return Page(
                title=f"{self.data['title']} - Blog de Çağan Mert İŞLEK",
                description=self.data['content'][:100],
                selector='body_blank',
                icon={
                    'href': '/static/favicon.png',
                    'type': 'image/x-icon'
                },
                childs=[
                    Widget(
                        'div',
                        style={
                            'position': 'fixed',
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
                            Widget('h1', innertext=self.data['title']),
                            Widget('p', childs=[Widget('i', childs=[
                                'Posted by ',
                                Widget('img', style={'height': '1em', 'border-radius': '50%'},
                                       src='/static/favicon.png', innertext=''),
                                ' on ',
                                self.data['datetime'].strftime('%B %d, %Y')
                            ])]),
                            Widget('p', innertext=self.data['content'])
                        ]
                    )
                ]
            )
