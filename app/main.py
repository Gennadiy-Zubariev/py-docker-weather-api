import os
import requests

API_KEY = os.environ.get("API_KEY")  # noqa: N806
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        {"key": API_KEY, "q": CITY}
    )

    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f'{location["name"]}/{location["country"]} '
        f'{location["localtime"]} '
        f'Weather: {current["temp_c"]} Celsius, '
        f'{current["condition"]["text"]}'
    )


if __name__ == "__main__":
    get_weather()
