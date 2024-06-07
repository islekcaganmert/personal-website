from bevyframe import Request, Page, Widget


class Super:
    def __init__(self, data):
        self.data = data

    def activity(self, r: Request) -> dict:
        return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": f"https://islekcaganmert.vercel.app/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "type": "Note",
            "published": "2024-06-06T14:55:49Z",
            "url": f"https://islekcaganmert.vercel.app/Blog/{self.data['datetime'].strftime('%Y%m%d%H%M')}_{self.data['id']}.py",
            "attributedTo": "https://islekcaganmert.vercel.app/activitypub.json",
            "content": "<p>" + self.data['title'] + '</p><p><a href="https://islekcaganmert.vercel.app/Blog/' + self.data['datetime'].strftime('%Y%m%d%H%M') + '_' + self.data['id'] + '.py">Read it on web</a></p>',
            "contentMap": {
                "en": "<p>" + self.data['title'] + '</p><p><a href="https://islekcaganmert.vercel.app/Blog/' + self.data['datetime'].strftime('%Y%m%d%H%M') + '_' + self.data['id'] + '.py">Read it on web</a></p>'
            },
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
