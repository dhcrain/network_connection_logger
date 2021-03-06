# Internet Connection Test & Speed Logger

An attempt at creating a small utility to check internet connection. If there is connection present it will then check its ping, upload and download speed.

You can set the time between test by changing the value of ```sleeping``` in the `internet_test.py` file. (Default is 30 seconds)

### To Run

I recommend setting up a Python 3.5 virtual environment first.

1. `git clone https://github.com/dhcrain/network_connection_logger.git`
2. `pip install requirements.txt`
3. ` python internet_test.py`

This will create a file named `connection.log` with all the data in it, formatted like this:

`connection.log`  
>INFO: 10/04/2016 01:46:01 PM: Program started  
INFO: 10/04/2016 01:46:50 PM:  46.2  27.9   3.3  
ERROR: 10/04/2016 01:48:09 PM: internet is down!  
INFO: 10/04/2016 01:49:29 PM:  87.4  64.4   3.7  

Successful test are in this format:  
Ping (in ms), Download (in Mbit/s), Upload (in Mbit/s)


Tested in Python 3.5 and Mac OSX, the goal is to use this on a Raspberry Pi to test an internet connection over a period of time.  
