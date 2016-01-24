Welcome to `weathercli`, a simple program to display today's weather.

summary:

This program uses 2 services for getting the weather:
* ip-api.com - geolcation lookup API
* api.openweathermap.org - weather forecast API

The program makes a call to a geolcation lookup API to get the latitude/longitude coordinates of your current IP address (technically, your NAT'ed public IP).  It can also take an IP address as an argument, if you want to do a lookup for a different IP.  Then sends your laitude/longitude to the weather forecast API and retrieves today's weather.  The weather data is then formatted and displayed to the user.

usage:

clone the repo, activate a virtualenv, install requirements, and run!

$ git clone https://github.com/cgoldberg/weathercli
$ cd weathercli
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python weathercli.py
