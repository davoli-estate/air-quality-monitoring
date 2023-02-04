import urequests, ujson, secrets

def get_current_weather_conditions():
    
    url = secrets.weather_api_url

    headers = {
        "X-RapidAPI-Key": secrets.weather_api_key,
        "X-RapidAPI-Host": secrets.weather_api_host
    }
    
    print("URL:", url)
    print("Headers:", headers)
    response = urequests.get(url, headers=headers)

    print(response.content)
    print(response.status_code, response.reason)
    print(response.headers)
    
    json = ujson.loads(response.content)

    return json