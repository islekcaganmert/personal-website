from bevyframe import Response, Request
import json


def get(r: Request) -> dict:
    return Response(json.dumps({
        "subject": "acct:islekcaganmert.me@islekcaganmert.me",
        "aliases": [
            "https://islekcaganmert.me/ap/Actor.py",
            "https://islekcaganmert.me/"
        ],
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": "https://islekcaganmert.me/ap/Actor.py"
            },
            {
                "rel": "http://webfinger.net/rel/profile-page",
                "type": "text/html",
                "href": "https://islekcaganmert.me/"
            }
        ]
    }), headers={'Content-Type': 'application/json'})
