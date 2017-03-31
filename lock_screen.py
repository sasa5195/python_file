

#Run the script below in the background, and it will lock the screen after an arbitrary number of minutes:
#!/usr/bin/env python3
import subprocess
import time
import sys

t = 0; max_t = int(sys.argv[1])

while True:
    # check runs once per minute
    time.sleep(60)
    # check the lock status, add 1 to current time if not locked, else t = 0
    try:
        subprocess.check_output(["pgrep", "-cf", "lockscreen-mode"]).decode("utf-8").strip()
        t = 0
    except subprocess.CalledProcessError:
        t += 1
    # if unlocked status time exceeds set time (in minutes), lock screen
    if t >= max_t:
        subprocess.Popen(["gnome-screensaver-command",  "-l"])
        t = 0
"""
How to use

    Copy the script into an empty file, save it as lock_screen.py

    Test- run it from a terminal with the lock- time as an argument (minutes)

    python3 /path/to/lock_screen.py 30

    (Although for the test, I'd take a shorter time)

    If all works fine, add it to Startup Applications Dash > Startup Applications > Add. Add the command:

    python3 /path/to/lock_screen.py 30

"""
