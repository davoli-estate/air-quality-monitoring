import uos, urequests, secrets, network, time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.wifi_ssid, secrets.wifi_password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    print(wlan.ifconfig())


if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print("Wi-Fi connected")
    status = wlan.ifconfig()
    print( 'IP Address = ' + status[0] )
    print( status )


# URL of the RAW file to clone
script_url = "https://raw.githubusercontent.com/kelseyhightower/nocode/master/Dockerfile"

while True:

    # Pull script from URL
    script_content = urequests.get(script_url).content
    print(script_content)

    # Write content of script to a file
    f = open("run.py", "w")
    f.write(script_content)
    f.close()

    # Read and print the script
    f = open("run.py", "r")
    print(f.read())
    f.close()
    time.sleep(2)

    # Run the script