from bevyframe import Request, Response
import json


def get(r: Request) -> Response:
    d = {
      "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1",
        {
          "featuredTags": {
            "@id": "toot:featuredTags",
            "@type": "@id"
          }
        }
      ],
      "type": "Person",
      "id": "https://islekcaganmert.vercel.app/ap/Actor.py",
      "name": "Çağan Mert İŞLEK",
      "preferredUsername": "islekcaganmert.vercel.app",
      "summary": "<p>Inventor of TheProtocols<br/>Full-Stack Software Developer<br/>Philosopher<br/>BLINK</p>",
      "inbox": "https://islekcaganmert.vercel.app/ap/Inbox.py",
      "outbox": "https://islekcaganmert.vercel.app/ap/Outbox.py",
      "followers": "https://islekcaganmert.vercel.app/ap/Followers.py",
      "following": "https://islekcaganmert.vercel.app/ap/Following.json",
      "featuredTags": "https://islekcaganmert.vercel.app/ap/FeaturedTags.json",
      "endpoints":{
        "sharedInbox": "https://islekcaganmert.vercel.app/ap/Inbox.py"
      },
      "url": "https://islekcaganmert.vercel.app/",
      "icon": {
        "type": "Image",
        "mediaType": "image/png",
        "url": "https://islekcaganmert.vercel.app/static/favicon.png"
      },
      "image": {
        "type": "Image",
        "mediaType": "image/jpg",
        "url": "https://islekcaganmert.vercel.app/static/banner.jpg"
      },
      "publicKey": {
        "id": "https://islekcaganmert.vercel.app/ap/Actor.py#main-key",
        "owner": "https://islekcaganmert.vercel.app/ap/Actor.py",
        "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsW47BbWdM1JVGaLWmenF\nd6hGHkgsuGQoTqUbhxRg1WoBVouo4uMHisBl5prQTjhDCzovOmoxwRubBXZKHgWx\nDkJjTH/7AIanwM/z33NnN2ibaw/IKxv14FN+EJ4M+KOKCZt2dWokdk9oaio/ULE8\nzbaF+2NtCHNvS1J/dpMIcTIpsdrrX4U6EXyOtROxeXMraKCTwx/RFhqX9KJIIChy\n7AatFzTys5CoFW198psWqmJZ1XUo5iYtvZ4LeVaZgC8X1ivKlkHy551g1A3BKg+I\nLQq0CEP6FY0Xx3b0sECTOLDwnR5OAkd7V3sGlqSDp7sfHMGMyMuWdiEZJrPl8Q4X\nEwIDAQAB\n-----END PUBLIC KEY-----"
      }
    }
    return Response(json.dumps(d), headers={'Content-Type': 'application/activity+json'})
