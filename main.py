from tkinter import *
from tkinter import messagebox
from weather_api import get_weather, get_forecast


def get_weather_icon(condition):
    condition = condition.lower()

    if "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "haze" in condition or "mist" in condition or "fog" in condition:
        return "🌫️"
    elif "thunder" in condition:
        return "⛈️"
    else:
        return "🌤️"


def change_background(condition):
    condition = condition.lower()

    if "clear" in condition:
        root.config(bg="#FFF3B0")
    elif "cloud" in condition:
        root.config(bg="#D3D3D3")
    elif "rain" in condition:
        root.config(bg="#A7C7E7")
    elif "haze" in condition or "mist" in condition or "fog" in condition:
        root.config(bg="#E5E5E5")
    else:
        root.config(bg="white")


def search_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    weather = get_weather(city)

    if weather is None:
        messagebox.showerror("Error", "Weather data not found. Check city name or API key.")
        return

    icon = get_weather_icon(weather["description"])
    change_background(weather["description"])

    result_label.config(
        text=
        f"{icon}\n"
        f"City: {weather['city']}, {weather['country']}\n"
        f"Temperature: {weather['temperature']} °C\n"
        f"Feels Like: {weather['feels_like']} °C\n"
        f"Humidity: {weather['humidity']}%\n"
        f"Pressure: {weather['pressure']} hPa\n"
        f"Wind Speed: {weather['wind_speed']} m/s\n"
        f"Condition: {weather['description']}"
    )

    forecast = get_forecast(city)

    if forecast is not None:
        forecast_text = "5-Day Forecast:\n\n"

        for day in forecast:
            forecast_text += f"{day['date']}  |  {day['temp']} °C  |  {day['condition']}\n"

        forecast_label.config(text=forecast_text)


root = Tk()
root.title("Real-Time Weather Tracker")
root.geometry("500x600")
root.resizable(False, False)

title_label = Label(root, text="Weather Tracker", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

city_entry = Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

search_button = Button(root, text="Search Weather", font=("Arial", 12), command=search_weather)
search_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

forecast_label = Label(root, text="", font=("Arial", 11), justify="left")
forecast_label.pack(pady=10)

root.bind("<Return>", lambda event: search_weather())

root.mainloop()