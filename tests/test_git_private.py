import urequests
import json

# Set up the basic auth credentials
username = "your_github_username"
password = "your_github_password"

# Set up the repository URL
url = "https://github.com/kelseyhightower/nocode/archive/refs/tags/1.0.0.zip"

# Set up the headers
#headers = {
#    "Accept": "application/vnd.github.v3+json",
#    "Authorization": "Basic " + str(urequests.put(username + ':' + password).encode('base64'))[:-1]
#}

# Send the GET request
response = urequests.get(url, headers=headers)

# Write the zipball to a file
with open("repo.zip", "wb") as f:
    f.write(response.content)