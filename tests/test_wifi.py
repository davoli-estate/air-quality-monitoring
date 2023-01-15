import secrets, network, time    # Sleep

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