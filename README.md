# weathercli

### display today's weather


##### Corey Goldberg, 2016

----

#### Development:

* https://github.com/cgoldberg/weathercli

#### Usage:

* `weathercli.py [-h] [ip]`

#### Instructions:

* clone the repo, activate a virtualenv, install requirements, and run!

	```
	$ git clone https://github.com/cgoldberg/weathercli
	$ cd weathercli
	$ virtualenv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt
	$ python weathercli.py
	```

#### Summary:

`weathercli` uses 2 services to get today's weather:
* ip-api.com - geolcation lookup API
* api.openweathermap.org - weather forecast API

The program makes a call to the geolocation lookup API to get latitude/longitude coordinates of your current IP address (technically, your NAT'ed public IP). If you want to do a lookup for a different IP, supply the address as an argument when invoking the program.

Once location is retrieved, coordinates are sent to the weather forecast API to retrieve today's weather conditions.

The weather data is then formatted and displayed to the user.

---
