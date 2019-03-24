#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys


def parse_city():
    city = sys.argv[1]
    return city


def request_city_info(city):
    request_params = {
        "q": city,
        "APPID": "729dbab702cdab927012e098fc175809",
        "units": "metric",
    }
    api_response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=request_params)
    return api_response


def validate_api_response(response):
    if response.status_code == 200:
        return True
    else:
        return False


def parse_data(data):
    temp = data["main"]["temp"]
    return temp


def main():
    city = parse_city() if len(sys.argv) > 1 else print("No city input")
    data = request_city_info(city)
    if validate_api_response(data):
        temp = parse_data(data.json())
        print(str(temp) + "°C")
    else:
        print("Error while connecting to API, check your input city or internet connection")


main()
