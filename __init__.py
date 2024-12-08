from bevyframe import *
from TheProtocols import *
from datetime import datetime
import requests
import os


def get(context: Context) -> Page:
    repos = requests.get(f'https://api.github.com/users/{context.env["github"]}/repos').json()
    articles = requests.get(f'https://articles.hereus.net/Api/Profile.py?addr={context.env["user"]}').json()['articles']
    articles.reverse()
    u = User(context.env['user'])
    return Page(
        title=u,
        color=context.env["theme"],
        OpenGraph={
            'title': str(u),
            'description': ', '.join(context.env['bio']),
            'image': context.env['banner'],
            'url': f"https://{context.env['domain']}/",
            'type': 'profile'
        },
        childs=[
            Widget('a', rel='me', href=f'https://{context.env["domain"]}/', innertext=''),
            Widget('a', rel='me', href=f'https://{context.env["social"]["fediverse"].split("@")[2]}/@{context.env["social"]["fediverse"].split("@")[1]}', innertext=''),
            Container(
                childs=[
                    Image(
                        context.env['banner'],
                        'Banner',
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
                                u.profile_photo,
                                'Avatar',
                                width=Size.pixel(100),
                                height=Size.pixel(100),
                                border_radius=Size.pixel(50),
                                background_color='white',
                            ),
                            Title(str(u)),
                            Label(
                                Link(f'@{context.env["domain"]}', f'https://{context.env["domain"]}').render(),
                                margin=Margin(top=Size.pixel(-30))
                            ),
                            Line([f'{i}<br>' for i in context.env['bio']]),
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
                                        ['Job', f"{context.env['job']['title']} @ {context.env['job']['company']}"],
                                        ['Education', f"{context.env['education']['degree']} @ {context.env['education']['school']}"],
                                        ['Location', context.env['location']],
                                        ['Pronouns', {
                                            'Male': 'he/him',
                                            'Female': 'she/her',
                                            'Gay': 'he/him',
                                            'Lesbian': 'she/her',
                                        }.get(u.gender, 'they/them')],
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
                                                    onclick=context.start_redirect(f"mailto:{context.env['email']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='𝕏',
                                                    onclick=context.start_redirect(f"https://x.com/{context.env['social']['x']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='LinkedIn',
                                                    onclick=context.start_redirect(
                                                        f"https://linkedin.com/in/{context.env['social']['linkedin']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Instagram',
                                                    onclick=context.start_redirect(
                                                        f"https://instagram.com/{context.env['social']['instagram']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Discord',
                                                    onclick=context.start_redirect(
                                                        f"https://discordapp.com/users/{context.env['social']['discord']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                ),
                                                Button(
                                                    'mini',
                                                    innertext='Reddit',
                                                    onclick=context.start_redirect(
                                                        f"https://reddit.com/u/{context.env['social']['reddit']}"),
                                                    width=Size.max_content,
                                                    padding=Padding(left=Size.pixel(10), right=Size.pixel(10))
                                                )
                                            ]
                                        ]
                                    )
                                ]
                            ),
                            Container(
                                id='button_bar',
                                selector=f'body_{context.env["theme"]}',
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
                                        onclick=context.start_redirect(f"/Blog.py?id={article['id']}"),
                                        cursor=Cursor.pointer,
                                        childs=[
                                            Heading(article['title']),
                                            Label(
                                                innertext=article['date'],
                                                margin=Margin(top=Size.pixel(-20))
                                            )
                                        ]
                                    ) for article in articles
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
        