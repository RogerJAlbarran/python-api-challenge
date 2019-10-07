#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
get_ipython().run_line_magic('run', './api_keys.ipynb')

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
new_lats = []
new_longs = []
cities = []
countries = []
temp = []
# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    country = citipy.nearest_city(lat_lng[0], lat_lng[1]).country_code
    #countries.append(country)
    # If the city is unique, then add it to a our cities list
   #if country not in countries:
     #   countries.append(country)
    if city not in cities:
        cities.append(city)
        countries.append(country)
        new_lats.append(lat_lng[0])
        new_longs.append(lat_lng[1])
   # Print the city count to confirm sufficient count

print(len(cities))
print(len(countries))
print(len(new_lats))
print(len(new_longs))


# In[3]:


# Use citipy to define city and country from coordinates
# Create a new df

Weather_now_df = pd.DataFrame({"Latitude": new_lats, "Longitude": new_longs, "City":cities})


# In[4]:


Weather_now_df.head() 


# In[ ]:




