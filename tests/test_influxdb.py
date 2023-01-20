import secrets, urequests, ujson
from libs import wifi

token = secrets.influxdb_token
host = secrets.influxdb_host
org_id = secrets.influxdb_org_id
bucket = secrets.influxdb_bucket
url = "https://" + host + "/api/v2/write?org=" + org_id +"&bucket=" + bucket

#data = {"temperature": 29.3, "humidity": 50.2}
data='temperature,location=kitchen value=24.8'
headers = {
    "Content-Type": "application/octet-stream",
    "Authorization": "Token " + token,
    "Accept": "application/json"
}

wifi.connect()
print("data =", data)
print("headers =", headers)
print("Sending timeseries data to InfluxDB at:", url)

response = urequests.post(url, data=data, headers=headers)
print(response.status_code, response.reason)
print(response.headers)
response.close()
