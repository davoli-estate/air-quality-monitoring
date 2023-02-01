import time, secrets
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE # https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/breakout_bme68x
from pimoroni_i2c import PimoroniI2C
from libs import influxdb, weather_api

i2c = PimoroniI2C(sda=0, scl=1)
sensor = BreakoutBME68X(i2c)

def collect_sensor_data():
    heater = "Unstable" # This ensures the while loop below runs at least twice on execution, to help the heater can stabilize

    while heater is "Unstable":
        # Gather data
        temperature, pressure, humidity, gas, status, _, _ = sensor.read()
        heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"

        # Print raw one-liner
        #print("{:0.2f}c, {:0.2f}Pa, {:0.2f}%, {:0.2f} Ohms, Heater: {}".format(temperature, pressure, humidity, gas, heater))
        
        # Print one value per line with adjusted measures
        print("Temperature:", "{:0.2f}C".format(temperature))
        print("Pressure:", "{:0.2f}kPa".format(pressure/1000))
        print("Humidity:", "{:0.2f}%".format(humidity))
        print("Gas:", "{:0.2f} kOhms".format(gas/1000))
        print("CO2 equivalent: {:.2f} ppm".format(gas/56.1))
        print("Heater:", heater)

        time.sleep(3)
    
    # Format timeseries data - Reference: https://docs.influxdata.com/influxdb/cloud/reference/syntax/line-protocol/
    ts_temperature = f"temperature,sensor_id={secrets.sensor_id},location={secrets.sensor_location} value={temperature}"
    ts_humidity = f"humidity,sensor_id={secrets.sensor_id},location={secrets.sensor_location} value={humidity}"
    ts_pressure= f"pressure,sensor_id={secrets.sensor_id},location={secrets.sensor_location} value={pressure/1000}"
    ts_gas= f"gas,sensor_id={secrets.sensor_id},location={secrets.sensor_location} value={gas/1000}"
    ts_co2eq= f"co2eq,sensor_id={secrets.sensor_id},location={secrets.sensor_location} value={gas/56.1}"

    timeseries_data = "\n".join([ts_temperature,ts_humidity,ts_pressure,ts_gas,ts_co2eq])
    print(f"Printing timeseries data: \n{timeseries_data}")

    return timeseries_data

def collect_weather_data():
    return str(weather_api.get_current_weather_conditions())

# Combine timeseries data
timeseries_data = "\n".join([collect_sensor_data(), collect_weather_data()])

# Send timeseries data to InfluxDB
influxdb.send_timeseries_data(timeseries_data)