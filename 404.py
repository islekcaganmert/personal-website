from bevyframe import *


def get(context: Context) -> Response:
    return context.create_response(Page(
        title="Not Found",
        style=context.app.style,
        childs=[
            Widget('h1', innertext='404 Not Found')
        ]
    ), status_code=404)
