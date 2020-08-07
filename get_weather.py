import requests
import json
import datetime

API_KEY = '73f5368224eb5dc6ab4b96b6cfaa24a7'
CITY_ID = 6167865
url = f'http://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&appid={API_KEY}'


def main(alert=False):
    r = requests.get(url)
    data_json = r.json()
    most_recent = data_json['list'][0]

    # parse data
    dt = most_recent.get('dt')  # epoch datetime
    dt = datetime.datetime.fromtimestamp(dt).strftime('%c')[:-8]  # converted datetime

    feels_k = most_recent.get('main').get('feels_like')  # feels like in Kelvin
    feels_c = str(round(feels_k - 273.15, 1)) + "C"  # feels like in c
    w_descript = most_recent.get('weather')[0].get('description')
    pop = most_recent.get('pop')
    rain = most_recent.get('rain')
    if rain is not None:
        rain = rain.get('3h')

    text = f"""Weather for {dt}:
Feels like {feels_c} with {w_descript} and {pop}% chance of rain. \n
    """

    r_text = "" if rain is None else f"Expecting {rain}mm of rain in the next 3 hours"
    if not alert:
        return text + r_text
    elif alert is True and rain is not None:
        if rain > 5:
            return "Alert!\n" + r_text


if __name__ == '__main__':
    print(main())
