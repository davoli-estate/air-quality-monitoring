import urequests, time
from libs import wifi

wait_time_in_minutes = 5
wifi.connect()

# URL of the RAW file to clone
script_url = "https://raw.githubusercontent.com/Marcvd316/air-quality-monitoring/main/air_quality_monitor.py"
retrieval_attempt = 0

while True:

    try:
        # Pull the Python script from URL
        print("Downloading script from", script_url)
        script_content = urequests.get(script_url).content
        print("Succesfully downloaded script content.")
    except:
        if retrieval_attempt == 5:
            print("Fatal error: Unable to retrieve script content after 5 attempts.")
            quit()
        else:
            print("Error: Unable to retrieve script content, will retry on next run.")
            retrieval_attempt += 1
    
    # Write content of script to a .py file
    f = open("air_quality_monitor.py", "w")
    f.write(script_content)
    f.close()

    # Execute the Python script
    print("Executing script air_quality_monitor.py...")
    exec(open('air_quality_monitor.py').read())

    # Wait for next run
    next_run_time_raw = time.localtime(time.time() + wait_time_in_minutes * 60)
    next_run_time = str(next_run_time_raw[3]) + ":" + str(next_run_time_raw[4])
    print("Waiting", wait_time_in_minutes, "minutes for next execution at", next_run_time)
    time.sleep(wait_time_in_minutes * 60)

    # Watchdog
    # https://raspberrypi.github.io/pico-sdk-doxygen/group__hardware__watchdog.html