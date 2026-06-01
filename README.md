# Real-Time Weather Tracker

A Python-based weather tracking application that retrieves real-time weather and forecast data using the OpenWeather API. The application provides current weather conditions, a 5-day forecast, and a user-friendly graphical interface built with Tkinter.

## Features

* Real-time weather information for any city
* Current temperature and "feels like" temperature
* Humidity, pressure, and wind speed monitoring
* Weather condition descriptions
* 5-day weather forecast
* Simple and interactive Tkinter GUI
* API integration with OpenWeather
* JSON data processing and error handling

## Technologies Used

* Python
* Tkinter
* Requests Library
* OpenWeather API
* JSON

## Project Structure

```text
WeatherTracker/
│
├── main.py
├── weather_api.py
├── config.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Real-Time-Weather-Tracker.git
```

2. Navigate to the project directory:

```bash
cd Real-Time-Weather-Tracker
```

3. Install required dependencies:

```bash
pip install requests
```

## API Setup

1. Create a free account at OpenWeather.
2. Generate an API key.
3. Open `config.py`.
4. Replace the placeholder API key with your own:

```python
API_KEY = "YOUR_API_KEY"
```

## Running the Application

Execute the following command:

```bash
python main.py
```

## How It Works

1. The user enters a city name.
2. The application sends a request to the OpenWeather API.
3. The API returns weather information in JSON format.
4. The application processes the response and extracts relevant weather data.
5. Current weather conditions and forecast information are displayed in the graphical interface.

## Sample Output

```text
City: Lahore, PK
Temperature: 31.0 °C
Feels Like: 32.2 °C
Humidity: 48%
Pressure: 1004 hPa
Wind Speed: 1.03 m/s
Condition: Haze

5-Day Forecast:
2026-06-02 | 35.0 °C | Clear Sky
2026-06-03 | 34.0 °C | Scattered Clouds
```

## Learning Outcomes

This project demonstrates:

* REST API Integration
* HTTP Requests Handling
* JSON Data Processing
* GUI Development with Tkinter
* Error Handling
* Modular Python Programming
* Real-Time Data Retrieval

## Future Enhancements

* Weather charts and visualizations
* Temperature trend analysis
* Weather history storage
* Export weather reports to CSV
* Enhanced user interface
* Air Quality Index (AQI) integration

## Author

Ahmed Amir

---

Developed as a Python API Integration and GUI Development project.
