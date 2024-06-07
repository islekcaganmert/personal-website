from bevyframe import Response, Request
import json


def get(r: Request) -> dict:
    return Response(json.dumps({
        "subject": "acct:islekcaganmert.vercel.app@islekcaganmert.vercel.app",
        "aliases": [
            "https://islekcaganmert.vercel.app/ap/Actor.py",
            "https://islekcaganmert.vercel.app/"
        ],
        "links": [
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": "https://islekcaganmert.vercel.app/ap/Actor.py"
            },
            {
                "rel": "http://webfinger.net/rel/profile-page",
                "type": "text/html",
                "href": "https://islekcaganmert.vercel.app/"
            }
        ]
    }), headers={'Content-Type': 'application/json'})