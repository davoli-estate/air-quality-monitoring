import machine # GPIO
import time    # Sleep

led = machine.Pin(25, machine.Pin.OUT)

# Turn the light on during execution
led.on()
time.sleep(3)
led.off()
#led.on() # Turned off in case I exit the script mid-loop and it doesn't shut off at the end


####################################
##    RP2040 Temperature sensor   ##
#################################### 
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
 
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    time.sleep(1)

# Turn the light off at the end of execution
led.off()
