import secrets, urequests

token = secrets.influxdb_token
host = secrets.influxdb_host
org_id = secrets.influxdb_org_id
bucket = secrets.influxdb_bucket
url = "https://" + host + "/api/v2/write?org=" + org_id +"&bucket=" + bucket


def send_timeseries_data(data: str):
    headers = {
        "Content-Type": "application/octet-stream",
        "Authorization": "Token " + token,
        "Accept": "application/json"
    }

    print("Timeseries data = \n", data)
    print("headers = \n", headers)
    print("Sending timeseries data to InfluxDB at:", url)

    response = urequests.post(url, data=data, headers=headers)
    print(response.status_code, response.reason)
    print(response.headers)
    response.close()
