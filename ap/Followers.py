import json


def get(r):
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams"
        ],
        "id": "https://islekcaganmert.vercel.app/ap/Followers.py",
        "type": "OrderedCollection",
        "totalItems": len(json.load(open('./DB/Followers.json')))
    }