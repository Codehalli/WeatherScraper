# The purpose of this project was to create/implement web scraping
# I was able to use this method for practical purpose such a list of weather
# wscrape.py
# By Pranav Rao

import pandas as pd  # using pandas library
import requests      # request library
from bs4 import BeautifulSoup  # bs4 library

# Getting all the information from the website using request and parsing with BS4
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.0011&lon=-77.4555#.Xv0BAZNKjOQ')
soup = BeautifulSoup(page.content, 'html.parser')

# Helps us extract the proper html codes sections we are interested in
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

# Setting new variables name and using the get text just to get that exact string
period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]


# This is using the panda library which is powerful analytical tool to help organize
# data efficiently
weather_stuff = pd.DataFrame(
    {
        'period': period_name,
        'short_description': short_description,
        'temperature': temp,
    })

print(weather_stuff) # prints to the console

weather_stuff.to_csv('weather.csv') # This to_csv function will help convert/save it to an excel format
