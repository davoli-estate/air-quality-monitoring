import urequests, time
from libs import wifi

wifi.connect()

# URL of the RAW file to clone
script_url = "https://raw.githubusercontent.com/Marcvd316/air-quality-monitoring/main/air_quality_monitor.py"

while True:

    try:
        # Pull the Python script from URL
        script_content = urequests.get(script_url).content
    except:
        print("Fatal error: Unable to retrieve script content.")
        quit()
    

    # Write content of script to a .py file
    f = open("air_quality_monitor.py", "w")
    f.write(script_content)
    f.close()

    # Execute the Python script
    print("Executing script air_quality_monitor.py...")
    exec(open('air_quality_monitor.py').read())

    # Watchdog
    # https://raspberrypi.github.io/pico-sdk-doxygen/group__hardware__watchdog.html