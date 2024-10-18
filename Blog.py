from TheProtocols import User
from bevyframe import *
import requests


def get(con: Context) -> (Page, Response):
    article = requests.get(f"https://articles.hereus.net/Api/Read.py?id={con.query.get('id')}").json()
    u = User(con.env['user'])
    print(article.keys())
    if article['author'] != con.env['user']:
        return ''
    return Page(
        title=f"{article['title']} - Blog de {u}",
        description=article['date'],
        color=con.env["theme"],
        OpenGraph={
            'title': article['title'],
            'description': article['date'],
            'image': '',
            'url': f"https://{con.headers['Host']}/Blog.py?id={article['id']}",
            'type': 'article',
            'site_name': f'Blog de {u}',
            'article:published_time': article['date'],
            'article:author': str(u),
        },
        icon={
            'href': u.profile_photo,
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
                            Italic(f"Posted by {u} on {article['date']}"),
                        ]
                    ),
                    Title(article['title']),
                    Label(article['content']),
                    '''
<p>&nbsp;</p><p xmlns:cc="https://creativecommons.org/ns#" >This work is licensed under <a href="https://creativecommons.org/licenses/by-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;color:blue;text-decoration:underline">CC BY-ND 4.0</a></p>
                    ''',  # CreativeCommons
                    Line([Link('Read on HereUS', f"https://articles.hereus.net/Read.py?id={article['id']}", style={
                        'color': 'blue',
                        'text-decoration': 'underline'
                    })])
                ]
            )
        ]
    )
