import requests
from flask import render_template
from bevyframe import Request, Page, Widget


def get(r: Request) -> Page:
    repos = requests.get('https://api.github.com/users/islekcaganmert/repos').json()
    return Page(
        title='Çağan Mert İŞLEK',
        description='',
        selector='body_green',
        icon={
            'href': '/static/favicon.png',
            'type': 'image/x-icon'
        },
        childs=[
            Widget('a', rel='me', href='https://islekcaganmert.vercel.app/', innertext=''),
            Widget(
                'div',
                selector='h-card',
                childs=[
                    Widget(
                        'img',
                        src='/static/banner.jpg',
                        selector='u-banner',
                        style={
                            'object-fit': 'cover',
                            'width': '100vw',
                            'height': '300px',
                            'margin-top': '-10px',
                            'margin-left': '-10px'
                        }
                    ),
                    Widget(
                        'div',
                        style={
                            'max-width': '600px',
                            'width': 'calc(100vw - 60px)',
                            'margin': 'auto',
                            'margin-top': '-55px'
                        },
                        childs=[
                            Widget(
                                'img',
                                src='/static/favicon.png',
                                selector='u-photo',
                                style={
                                    'height': '100px',
                                    'width': '100px',
                                    'border-radius': '50px',
                                    'background-color': '#ffffff'
                                }
                            ),
                            Widget(
                                'h1',
                                selector='p-name',
                                innertext='Çağan Mert İŞLEK'
                            ),
                            Widget(
                                'p',
                                selector='p-url',
                                href='https://islekcaganmert.vercel.app',
                                innertext='@islekcaganmert.vercel.app',
                                style={'margin-top': '-30px'}
                            ),
                            Widget(
                                'p',
                                selector='p-note',
                                childs=[f'{i}<br>' for i in [
                                    'Inventor of <a href="/projects/theprotocols">TheProtocols</a>',
                                    'Full-Stack Software Developer',
                                    'Philosopher',
                                    'BLINK'
                                ]]
                            ),
                            Widget(
                                'table',
                                style={
                                    'margin-left': '-3px'
                                },
                                childs=[
                                    Widget(
                                        'tr',
                                        childs=[
                                            Widget('td', childs=[Widget('b', innertext=i[0])]),
                                            Widget('td', innertext=f'&nbsp; &nbsp;{i[1]}')
                                        ]
                                    ) for i in [
                                        ['Work', 'Founder @ HereUS'],
                                        ['Education', 'Sophomore @ High School'],
                                        ['Pronouns', 'he/him']
                                    ]
                                ]
                            ),
                            Widget(
                                'div',
                                style={
                                    'width': '100vw',
                                    'max-width': '600vw',
                                    'margin-left': '-30px',
                                    'overflow-x': 'scroll'
                                },
                                childs=[
                                    Widget(
                                        'div',
                                        style={
                                            'overflow-y': 'hidden',
                                            'overflow-x': 'scroll',
                                            'white-space': 'nowrap',
                                            'width': '600px',
                                            'margin-top': '10px'
                                        },
                                        childs=[
                                            Widget(
                                                'div',
                                                style={
                                                    'margin-left': '30px',
                                                    'margin-right': '-25px',
                                                    'float': 'left',
                                                    'display': 'inline-block'
                                                },
                                                childs=[
                                                    Widget(
                                                        'a',
                                                        href=i[1],
                                                        target='_blank',
                                                        rel="me",
                                                        childs=[
                                                            Widget(
                                                                'button',
                                                                selector='button mini',
                                                                innertext=i[0],
                                                                style={
                                                                    'width': 'max-content',
                                                                    'padding-left': '10px',
                                                                    'padding-right': '10px'
                                                                }
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                            for i in [
                                                ['✉️', 'mailto:islekcaganmert@gmail.com'],
                                                ['LinkedIn', 'https://linkedin.com/in/islekcaganmert'],
                                                ['Fediverse', 'https://pebble.social/@islekcaganmert'],
                                                ['Instagram', 'https://instagram.com/islekcaganmert'],
                                                ['Lemmy', 'https://lemmy.today/u/islekcaganmert'],
                                                ['Discord', 'https://discordapp.com/users/983767367135932466']
                                            ]
                                        ]
                                    )
                                ]
                            ),
                            Widget(
                                'div',
                                id='button_bar',
                                style={
                                    'position': 'sticky',
                                    'top': '0px',
                                    'padding-top': '10px',
                                    'padding-bottom': '10px'
                                },
                                childs=[
                                    Widget(
                                        'div',
                                        style={
                                            'font-size': '1.6em',
                                            'display': 'inline-block',
                                            'width': 'calc(100% / 3)',
                                            'text-align': 'center',
                                            'cursor': 'pointer'
                                        },
                                        id=f"{i.lower()}_button",
                                        selector='tab_button',
                                        onclick=f"chooseTab('{i.lower()}')",
                                        childs=[
                                            Widget(
                                                'a',
                                                innertext=i
                                            )
                                        ]
                                    )
                                    for i in ['Posts', 'Repositories', 'Videos']
                                ]
                            ),
                            Widget(
                                'div',
                                style={
                                    'visibility': 'hidden',
                                    'height': '1px',
                                    'overflow-y': 'hidden'
                                },
                                id='posts_feed',
                                childs=[
                                    ''
                                    for i in repos
                                ]
                            ),
                            Widget(
                                'div',
                                style={
                                    'visibility': 'hidden',
                                    'height': '1px',
                                    'overflow-y': 'hidden'
                                },
                                id='repositories_feed',
                                childs=[
                                    Widget(
                                        'a',
                                        href=repo['html_url'],
                                        target='_blank',
                                        childs=[
                                            Widget(
                                                'div',
                                                selector='the_box',
                                                style={'margin-bottom': '10px'},
                                                childs=[
                                                    Widget('h3', innertext=repo['full_name']),
                                                    (
                                                        Widget('p', innertext=repo['description'], style={'margin-top': '-20px'})
                                                        if repo['description'] is not None else ''
                                                    ),
                                                    Widget('p', childs=[
                                                        f"{i.render()} &nbsp; &nbsp; " for i in [
                                                            Widget('i', innertext=repo['language']),
                                                            Widget('a', innertext=f"★ {repo['stargazers_count']}"),
                                                            Widget('a', innertext=f"◉ {repo['watchers_count']}"),
                                                            Widget('a', innertext=f"⑃ {repo['forks_count']}")
                                                        ]
                                                    ], style={'margin-top': '-10px'})
                                                ]
                                            )
                                        ]
                                    )
                                    for repo in repos
                                ]
                            ),
                            Widget(
                                'div',
                                style={
                                    'visibility': 'hidden',
                                    'height': '1px',
                                    'overflow-y': 'hidden'
                                },
                                id='videos_feed',
                                childs=[
                                    ''
                                    for i in repos
                                ]
                            )
                        ]
                    )
                ]
            ),
            Widget('script', innertext=open('__init__.js', 'r').read())
        ]
    )
