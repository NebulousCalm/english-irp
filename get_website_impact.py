import requests


def get_website_impact(website_url):
    website_url = f'https://api.websitecarbon.com/site?url={website_url}'
    req = requests.get(website_url)
    resp = req.json()
    results = {
        'url': resp.get('url'),
        'green': resp.get('green'),
        'cleanerThan': resp.get('cleanerThan'),
        'rating': resp.get('rating'),
        'carbon-grams': resp.get('statistics', {}).get('co2', {}).get('grid', {}).get('grams'),
        'full_resp': resp
    }
    return results
