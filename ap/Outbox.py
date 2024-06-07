import os


def get(r):
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams"
        ],
        "id": "https://islekcaganmert.vercel.app/ap/Outbox.py",
        "type": "OrderedCollection",
        "totalItems": len(os.listdir('./Blog')) - 1
    }