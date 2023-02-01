import time, secrets
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE # https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/breakout_bme68x
from pimoroni_i2c import PimoroniI2C
from libs import influxdb, weather_api

i2c = PimoroniI2C(sda=0, scl=1)
sensor = BreakoutBME68X(i2c)
influxdb_tags = f"sensor_id={secrets.sensor_id},location={secrets.sensor_location}"

# Collect data from BME688 sensor and format into InfluxDB Line Protocol Timeseries
def collect_sensor_data():
    heater = "Unstable" # This ensures the while loop below runs at least twice on execution, to help the heater can stabilize

    while heater is "Unstable":
        # Collect metrics
        temperature, pressure, humidity, gas, status, _, _ = sensor.read()
        heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"

        # Print raw one-liner
        #print("{:0.2f}c, {:0.2f}Pa, {:0.2f}%, {:0.2f} Ohms, Heater: {}".format(temperature, pressure, humidity, gas, heater))
        
        # Print metrics - one value per line with adjusted measures
        print("Temperature:", "{:0.2f}C".format(temperature))
        print("Pressure:", "{:0.2f}kPa".format(pressure/1000))
        print("Humidity:", "{:0.2f}%".format(humidity))
        print("Gas:", "{:0.2f} kOhms".format(gas/1000))
        print("CO2 equivalent: {:.2f} ppm".format(gas/56.1))
        print("Heater:", heater)

        time.sleep(3)
    
    # Format metrics into timeseries data - Reference: https://docs.influxdata.com/influxdb/cloud/reference/syntax/line-protocol/
    ts_temperature = f"temperature," + influxdb_tags + " value={temperature}"
    ts_humidity = f"humidity," + influxdb_tags + " value={humidity}"
    ts_pressure= f"pressure," + influxdb_tags + " value={pressure/1000}"
    ts_gas= f"gas," + influxdb_tags + " value={gas/1000}"
    ts_co2eq= f"co2eq," + influxdb_tags + " value={gas/56.1}"

    timeseries_data = "\n".join([ts_temperature,ts_humidity,ts_pressure,ts_gas,ts_co2eq])
    print(f"Printing timeseries data: \n{timeseries_data}")

    return timeseries_data

# Collect JSON data from weatherapi.com and format into InfluxDB Line Protocol Timeseries
def collect_weather_data():
    
    # Collect metrics
    data = weather_api.get_current_weather_conditions()
    outside_temperature = data["current"]["temp_c"]
    outside_humidity = data["current"]["humidity"]
    atmospheric_pressure = data["current"]["pressure_mb"]
    wind_kph = data["current"]["wind_kph"]
    feelslike = data["current"]["feelslike_c"]

    # Print metrics
    print("Outside Temperature:", outside_temperature)
    print("Feels like:", feelslike)
    print("Outside Humidity:", outside_humidity)
    print("Atmospheric Pressure:", atmospheric_pressure)
    print("Wind speed:", wind_kph)
    
    # Format metrics into timeseries data - Reference: https://docs.influxdata.com/influxdb/cloud/reference/syntax/line-protocol/
    ts_outside_temperature = f"outside_temperature," + influxdb_tags + " value={outside_temperature}"
    ts_outside_humidity = f"outside_humidity," + influxdb_tags + " value={outside_humidity}"
    ts_atmospheric_pressure = f"atmospheric_pressure," + influxdb_tags + " value={atmospheric_pressure}"
    ts_wind_kph = f"wind_kph," + influxdb_tags + " value={wind_kph}"
    ts_feelslike = f"feelslike," + influxdb_tags + " value={feelslike}"
    
    timeseries_data = "\n".join([ts_outside_temperature,ts_outside_humidity,ts_atmospheric_pressure,ts_wind_kph,ts_feelslike])
    print(f"Printing timeseries data: \n{timeseries_data}")
    
    return timeseries_data

# Combine timeseries data
timeseries_data = "\n".join([collect_sensor_data(), collect_weather_data()])

# Send timeseries data to InfluxDB
influxdb.send_timeseries_data(timeseries_data)