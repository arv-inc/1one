import requests


def get_weather(point: str) -> str:
    payload = {"nMqT": "", "lang": "ru"}
    weather_url = f'https://wttr.in/{point}'
    result_weather = ""

    response = requests.get(weather_url, params=payload)
    response.raise_for_status()
    result_weather += "{}\n{}".format("=" * 64, response.text)

    return result_weather


if __name__ == "__main__":
    request_places = ["London", "svo", "Cherepovets"]
    try:
        for place in request_places:
            weather_data = get_weather(place)
            print(weather_data)
    except requests.exceptions.HTTPError:
        print(f"{'!'*50}\nData for {place} not found\n{'!'*50}")
