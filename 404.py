from bevyframe import *


def get(r: Request) -> Page:
    return Page(
        title="Not Found",
        childs=[
            Widget('h1', innertext='404 Not Found')
        ]
    )
