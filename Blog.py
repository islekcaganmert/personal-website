from bevyframe import *


class Super:
    def __init__(self, data):
        self.data = data

    def get(self, _: Context) -> (Page, Response):
        return Page(
            title=f"{self.data['title']} - Blog de Çağan Mert İŞLEK",
            description=self.data['content'][:100],
            selector='body_blank',
            OpenGraph={
                'title': self.data['title'],
                'description': '',
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
                Container(
                    style={
                        'position': 'absolute',
                        'top': '10px',
                        'right': '30px',
                        'left': '30px',
                        'bottom': '0px',
                        'y-overflow': 'scroll'
                    },
                    childs=[
                        Line([
                            Link('Turn to homepage', '/', color='#0000ff', text_decoration='underline', style={
                                'color': 'blue',
                                'text-decoration': 'underline'
                            })
                        ]),
                        Line(
                            font_size=Size.Relative.font(0.8),
                            color='#80808080',
                            childs=[
                                Italic('Posted by Çağan Mert İŞLEK on ' + self.data['datetime'].strftime('%B %d, %Y'))
                            ]
                        ),
                        Title(self.data['title']),
                        Label(self.data['content']),
                        '''
<p>&nbsp;</p><p xmlns:cc="https://creativecommons.org/ns#" >This work is licensed under <a href="https://creativecommons.org/licenses/by-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;color:blue;text-decoration:underline">CC BY-ND 4.0</a></p>
                        '''  # CreativeCommons
                    ]
                )
            ]
        )
