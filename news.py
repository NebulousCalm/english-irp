import http.client
import urllib.parse
import json


def get_google_news_urls(query, location):
    query = urllib.parse.quote(query)
    location = urllib.parse.quote(location)

    conn = http.client.HTTPSConnection("api.scrape-it.cloud")

    headers = {
        'x-api-key': "39da1cc8-3c36-451b-a538-08aede68d42b",
        'Content-Type': "application/json"
    }

    conn.request("GET", f"""/scrape/google/serp?q={query}&location={location}&tbm=nws&deviceType=desktop""",

                 headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    return data['newsResults']
