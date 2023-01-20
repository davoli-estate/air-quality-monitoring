import secrets, network, time

def connect():
    print("Connecting to Wi-Fi...", end="")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.wifi_ssid, secrets.wifi_password)

    while not wlan.isconnected() and wlan.status() >= 0:
        print(".", end="")
        time.sleep(0.5)
        
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print("IP Address =", wlan.ifconfig()[0])
        print("Wi-Fi connected")