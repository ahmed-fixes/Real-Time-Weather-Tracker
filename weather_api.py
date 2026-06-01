import requests
from config import API_KEY, BASE_URL, FORECAST_URL


def get_weather(city):
    try:
        parameters = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=parameters)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"],
                "main_condition": data["weather"][0]["main"]
            }

            return weather_info

        else:
            return None

    except:
        return None


def get_forecast(city):
    try:
        parameters = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(FORECAST_URL, params=parameters)
        data = response.json()

        if response.status_code == 200:
            forecast_list = []

            for item in data["list"]:
                if "12:00:00" in item["dt_txt"]:
                    forecast = {
                        "date": item["dt_txt"].split(" ")[0],
                        "temp": round(item["main"]["temp"], 1),
                        "condition": item["weather"][0]["description"]
                    }

                    forecast_list.append(forecast)

            return forecast_list

        else:
            return None

    except:
        return None