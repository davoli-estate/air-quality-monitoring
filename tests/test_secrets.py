import secrets

f = open("secrets.py", "r")
print("Print by reading file: \n", f.read())

print("Print by reference:", secrets.wifi_ssid)