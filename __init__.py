import os
from datetime import datetime

from bevyframe import *
import requests


def get(context: Context) -> Page:
    repos = requests.get('https://api.github.com/users/islekcaganmert/repos').json()
    return Page(
        title='Çağan Mert İŞLEK',
        description='',
        selector='body_blank',
        icon={
            'href': '/static/favicon.png',
            'type': 'image/x-icon'
        },
        childs=[
            Widget('a', rel='me', href='https://islekcaganmert.me/', innertext=''),
            Widget('a', rel='me', href='https://sharkey.world/@islekcaganmert', innertext=''),
            Container(
                selector='h-card',
                childs=[
                    Image(
                        '/static/banner.jpg',
                        'Banner',
                        selector='u-banner',
                        width=Size.Viewport.width(100),
                        height=Size.pixel(300),
                        margin=Margin(
                            top=Size.pixel(-10),
                            left=Size.pixel(-10),
                        ),
                        max_height=substract_style(Size.Viewport.height(100), Size.pixel(600)),
                        min_height=Size.pixel(100),
                        css={'object-fit': 'cover', }
                    ),
                    Container(
                        max_width=Size.pixel(600),
                        width=substract_style(Size.Viewport.width(100), Size.pixel(60)),
                        margin=Margin(
                            top=Size.pixel(-55),
                            left=Size.auto,
                            right=Size.auto,
                        ),
                        childs=[
                            Image(
                                '/static/favicon.png',
                                'Avatar',
                                selector='u-photo',
                                width=Size.pixel(100),
                                height=Size.pixel(100),
                                border_radius=Size.pixel(50),
                                background_color='white',
                            ),
                            Title('Çağan Mert İŞLEK', selector='p-name'),
                            Label(
                                Link('@islekcaganmert.me', 'https://islekcaganmert.me').render(),
                                margin=Margin(top=Size.pixel(-30))
                            ),
                            Line([f'{i[0]}<br>' for i in [
                                ['Inventor of TheProtocols', 'https://theprotocols.islekcaganmert.me/'],
                                ['Full-Stack Software Developer', '/About/Software.py'],
                                ['Philosopher', '/About/Philosophy.py'],
                                ['BLINK', '/About/Kpop.py']
                            ]]),
                            Widget(
                                'table',
                                margin=Margin(left=Size.pixel(-3)),
                                childs=[
                                    Widget(
                                        'tr',
                                        childs=[
                                            Widget('td', childs=[Bold(i[0])]),
                                            Widget('td', innertext=f'&nbsp; &nbsp;{i[1]}')
                                        ]
                                    ) for i in [
                                        ['Work', 'Founder @ HereUS'],
                                        ['Education', 'Junior @ High School'],
                                        ['Pronouns', 'he/him'],
                                        ['MBTI', 'ISTJ-A']
                                    ]
                                ]
                            ),
                            Container(
                                width=Size.Viewport.width(100),
                                max_width=Size.Viewport.width(600),
                                margin=Margin(left=Size.pixel(-30)),
                                css={'overflow-x': 'scroll'},
                                childs=[
                                    Container(
                                        width=Size.pixel(600),
                                        margin=Margin(top=Size.pixel(10)),
                                        css={'overflow-y': 'hidden', 'overflow-x': 'scroll', 'white-space': 'nowrap'},
                                        childs=[
                                            Container(
                                                margin=Margin(left=Size.pixel(30), right=Size.pixel(-25)),
                                                css={'display': 'inline-block', 'float': 'left'},
                                                childs=[i]
                                            )
                                            for i in [
                                                Button(
                                                    'mini',
                                                    innertext='✉️',
                                                    onclick=context.start_redirect("mailto:islekcaganmert@gmail.com"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='𝕏',
                                                    onclick=context.start_redirect("https://x.com/islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(12), right=Size.pixel(8)),
                                                    css={'border-bottom-right-radius': '2px', 'border-top-right-radius': '2px'}
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='⁂',
                                                    onclick=context.start_redirect("https://sharkey.world/@islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(8), right=Size.pixel(12)),
                                                    margin=Margin(left=Size.pixel(-3)),
                                                    css={'border-bottom-left-radius': '2px', 'border-top-left-radius': '2px'}
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='LinkedIn',
                                                    onclick=context.start_redirect("https://linkedin.com/in/islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Instagram',
                                                    onclick=context.start_redirect("https://instagram.com/islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Discord',
                                                    onclick=context.start_redirect("https://discordapp.com/users/983767367135932466"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Reddit',
                                                    onclick=context.start_redirect("https://reddit.com/u/islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(12), right=Size.pixel(8)),
                                                    css={'border-bottom-right-radius': '2px', 'border-top-right-radius': '2px'}
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Lemmy',
                                                    onclick=context.start_redirect("https://lemmy.today/u/islekcaganmert"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(8), right=Size.pixel(12)),
                                                    margin=Margin(left=Size.pixel(-3)),
                                                    css={'border-bottom-left-radius': '2px', 'border-top-left-radius': '2px'}
                                                ),
                                            ]
                                        ]
                                    )
                                ]
                            ),
                            Container(
                                id='button_bar',
                                selector='body_blank',
                                position=Position.sticky(top=Size.pixel(0)),
                                padding=Padding(top=Size.pixel(10), bottom=Size.pixel(10)),
                                childs=[
                                    Container(
                                        font_size=Size.Relative.font(1.6),
                                        width=divide_style(Size.percent(100), 3),
                                        text_align='center',
                                        cursor=Cursor.pointer,
                                        css={'display': 'inline-block'},
                                        id=f"{i.lower()}_button",
                                        selector='tab_button',
                                        onclick=f"chooseTab('{i.lower()}')",
                                        childs=[i]
                                    ) for i in ['Posts', 'Repositories', 'Videos']
                                ]
                            ),
                            Container(
                                height=Size.pixel(1),
                                css={
                                    'visibility': 'hidden',
                                    'overflow-y': 'hidden'
                                },
                                id='posts_feed',
                                childs=[
                                    Box(
                                        margin=Margin(bottom=Size.pixel(10)),
                                        onclick=context.start_redirect(f"/Blog/{i}"),
                                        childs=[
                                            Heading('h3', innertext=open(f"Blog/{i}").read().split("'title': '")[1].split("'")[0]),
                                            Label(
                                                innertext=datetime.strptime(os.path.basename(i).split('_')[0].split('/')[-1], '%Y%m%d%H%M').strftime('%B %d, %Y'),
                                                margin=Margin(top=Size.pixel(-20))
                                            )
                                        ]
                                    ) if os.path.isfile(f"Blog/{i}") else ''
                                    for i in [i for i in sorted(os.listdir('Blog'))[::-1] if i not in ['Super.py', '__pycache__']]
                                ]
                            ),
                            Container(
                                height=Size.pixel(1),
                                css={
                                    'visibility': 'hidden',
                                    'overflow-y': 'hidden'
                                },
                                id='repositories_feed',
                                childs=[
                                    Widget(
                                        'a',
                                        href=repo['homepage'] if repo['homepage'] else repo['html_url'],
                                        target='_blank',
                                        childs=[
                                            Box(
                                                margin=Margin(bottom=Size.pixel(10)),
                                                childs=[
                                                    Heading(repo['full_name']),
                                                    (
                                                        Label(repo['description'], style={'margin-top': '-20px'})
                                                        if repo['description'] is not None else ''
                                                    ),
                                                    Line([
                                                        f"{i} &nbsp; &nbsp; " for i in [
                                                            f"<i>{repo.get('language', 'Custom')}</i>",
                                                            f"★ {repo['stargazers_count']}",
                                                            f"◉ {repo['watchers_count']}",
                                                            f"⑃ {repo['forks_count']}"
                                                        ]
                                                    ], margin=Margin(top=Size.pixel(-10)))
                                                ]
                                            )
                                        ]
                                    )
                                    for repo in repos
                                ]
                            ),
                            Container(
                                height=Size.pixel(1),
                                css={
                                    'visibility': 'hidden',
                                    'overflow-y': 'hidden'
                                },
                                id='videos_feed',
                                childs=[
                                    ''
                                    for _ in []
                                ]
                            )
                        ]
                    )
                ]
            ),
            Widget('script', innertext=open('__init__.js').read())
        ]
    )
