import urequests, ujson, secrets

def get_current_weather_conditions():
    
    url = secrets.weather_api_url

    headers = {
        "X-RapidAPI-Key": secrets.weather_api_key,
        "X-RapidAPI-Host": secrets.weather_api_url
    }
    
    print("URL:", url)
    print("Headers:", headers)
    response = urequests.get(url, headers=headers)

    print(response.content)
    
    # Cleanup Response Data
    ts_weather_data = format_data(response.content)
    print("Cleaned up weather data:", ts_weather_data)
    return ts_weather_data

# Cleanup Received Weather Data and format into InfluxDB Line Protocol Timeseries
def format_data(data: str):
    json = ujson.loads(data)
    temperature = json["current"]["temp_c"]
    print(temperature)
    return