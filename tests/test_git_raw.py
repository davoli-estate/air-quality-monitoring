import uos, urequests, secrets

print(secrets.git_username)

response = urequests.get("http://www.google.com")
# URL of the RAW file to clone
script_url = "https://raw.githubusercontent.com/kelseyhightower/nocode/master/Dockerfile"
response = urequests.get(script_url)
response.close()
print(response.content)

f = open("run.py", "w")
f.write(script_content)
f.close()

print(uos.listdir())

f = open("run.py", "r")
print(f.read())
f.close()