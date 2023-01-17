import urequests, time
from libs import wifi

wifi.connect()

# URL of the RAW file to clone
script_url = "https://raw.githubusercontent.com/Marcvd316/air-quality-monitoring/main/run.py"

while True:

    # Pull the Python script from URL
    script_content = urequests.get(script_url).content

    # Write content of script to a .py file
    f = open("air_quality_monitor.py", "w")
    f.write(script_content)
    f.close()

    # Execute the Python script
    print("Executing script air_quality_monitor.py...")
    exec(open('air_quality_monitor.py').read())