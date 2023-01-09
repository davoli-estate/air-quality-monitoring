from machine import Pin
import utime
led = Pin(25, Pin.OUT)
led.low()
while True:
    led.toggle()
    print("Toggle")
    utime.sleep(1)