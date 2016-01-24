#!/usr/bin/env python

import argparse
import sys

import requests
import requests.exceptions


# IP Geolocation API will automatically ban any IP addresses doing
# over 150 requests per minute. If blocked, visit http://ip-api.com/docs/unban
GEO_ENDPOINT = 'http://ip-api.com/json'
WEATHER_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
WEATHER_API_KEY = '4a4446cce56aa27a6cd85eaa0e2bb7af'


def fetch_geo_coordinates(ip=None):
    """retrieve geo coordinates from ip-api.com API.

    returns a dict (decoded JSON response)
    """
    if ip is None:
        url = GEO_ENDPOINT
    else:
        url = '{}/{}'.format(GEO_ENDPOINT, ip)
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise RuntimeError('Unable to get response from geo location service')
    data = r.json()
    if data['status'] == 'fail':
        raise RuntimeError('Unable to find geographic location')
    return data


def fetch_weather(lat, lon, api_key=WEATHER_API_KEY):
    """retrieve weather information from api.openweathermap.org API.

    returns a dict (decoded JSON response)
    """
    payload = dict(lat=lat, lon=lon, APPID=api_key)
    try:
        r = requests.get(WEATHER_ENDPOINT, params=payload)
    except requests.exceptions.RequestException as e:
        raise RuntimeError('Unable to get response from weather service')
    data = r.json()
    if data['cod'] != 200:
        raise RuntimeError('Unable to get valid weather report')
    return data


def convert_to_fahrenheit(kelvin_temp):
    """convert temperature from kelvin to degrees fahrenheit.

    returns a float (degrees fahrenheit)
    """
    return 1.8 * (273.15 - kelvin_temp) + 32


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', nargs='?', default=None, help='ip address')
    args = parser.parse_args()
    try:
        geo_data = fetch_geo_coordinates(args.ip)
        weather_data = fetch_weather(geo_data['lat'], geo_data['lon'])
    except Exception as e:
        sys.exit(e)
    print "Today's Weather for {}".format(weather_data['name'])
    print ('-' * 40)
    temp = convert_to_fahrenheit(weather_data['main']['temp'])
    print 'Temp (F): {:.1f}'.format(temp)
    forecast = weather_data['weather'][0]['main'].lower()
    description = weather_data['weather'][0]['description'].lower()
    print 'Forecast: {} ({})'.format(forecast, description)
