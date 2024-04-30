import requests
import string


def get_aqi_by_location(api, city, state):
    wind_direction_dict = {
        1: 'N',
        2: 'N',
        3: 'N',
        4: 'N',
        5: 'N',
        6: 'N',
        7: 'N',
        8: 'N',
        9: 'N',
        10: 'N',
        360: 'N',
        359: 'N',
        358: 'N',
        357: 'N',
        356: 'N',
        355: 'N',
        354: 'N',
        353: 'N',
        352: 'N',
        351: 'N',
        350: 'N',
        20: 'N/NE',
        21: 'N/NE',
        22: 'N/NE',
        23: 'N/NE',
        24: 'N/NE',
        25: 'N/NE',
        26: 'N/NE',
        27: 'N/NE',
        28: 'N/NE',
        29: 'N/NE',
        30: 'N/NE',
        31: 'N/NE',
        32: 'N/NE',
        33: 'N/NE',
        34: 'N/NE',
        35: 'N/NE',
        36: 'N/NE',
        37: 'N/NE',
        38: 'N/NE',
        39: 'N/NE',
        40: 'NE',
        50: 'NE',
        60: 'E/NE',
        70: 'E/NE',
        80: 'E',
        90: 'E',
        100: 'E',
        110: 'E/SE',
        120: 'E/SE',
        130: 'SE',
        140: 'SE',
        150: 'S/SE',
        160: 'S/SE',
        170: 'S',
        180: 'S',
        190: 'S',
        200: 'S/SW',
        210: 'S/SW',
        220: 'SW',
        230: 'SW',
        240: 'W/SW',
        250: 'W/SW',
        260: 'W',
        270: 'W',
        280: 'W',
        290: 'W/NW',
        300: 'W/NW',
        310: 'NW',
        320: 'NW',
        330: 'N/NW',
        340: 'N/NW'
    }

    city = string.capwords(city)
    state = string.capwords(state)

    url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country=USA&key={api}"
    response = requests.get(url)
    resp = response.json()

    wind_direction = wind_direction_dict[resp.get('data', {}).get('current', {}).get('weather', {}).get('wd')]
    print(wind_direction)

    results = {
        'city': resp.get('data', {}).get('city'),
        'state': resp.get('data', {}).get('state'),
        'country': resp.get('data', {}).get('country'),
        'location': resp.get('data', {}).get('location'),
        'current': {
            'pollution': resp.get('data', {}).get('current', {}).get('pollution'),
            'weather': resp.get('data', {}).get('current', {}).get('weather')
        },
        'full_resp': resp,
        'wind_direction': wind_direction
    }

    return results
