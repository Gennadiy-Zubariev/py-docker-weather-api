import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    city = "Paris"

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        {"key": api_key, "q": city}
    )

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f"Performing request to Weather API for city {city}...")
    print(
        f'{location["name"]}/{location["country"]} '
        f'{location["localtime"]} '
        f'Weather: {current["temp_c"]} Celsius, '
        f'{current["condition"]["text"]}'
    )


if __name__ == "__main__":
    get_weather()
