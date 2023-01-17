import secrets, urequests, json

token = secrets.influxdb_token
host = "us-east-1-1.aws.cloud2.influxdata.com"
org = "66f2c607131831e0" # "Home Assistant"
bucket = "air_quality"
url = "https://" + host + "/write?org=" + org +"&bucket=" + bucket

data = {"temperature": 25.3, "humidity": 50.2}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token " + token
}
print(token)
print("Connecting to", url)
response = urequests.post(url, data=json.dumps(data), headers=headers)
print(response.status_code)
response.close()