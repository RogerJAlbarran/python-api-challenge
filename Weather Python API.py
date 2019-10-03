#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import pyowm
# Import API key
owm = pyowm.OWM('08b2b3933f6b578b05842b04d5e18bfb')

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
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
   city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
   
   # If the city is unique, then add it to a our cities list
   if city not in cities:
       cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# In[ ]:




