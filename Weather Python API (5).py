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


# In[5]:


api_key = "08b2b3933f6b578b05842b04d5e18bfb"


url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + api_key


# In[6]:


# Create empty lists to append the API data into lists 
city_name = []
cloudiness = []
country = []
date = []
humidity = []
lat = []
lng = []
max_temp = []
wind_speed = []

# Start the call counter 
record = 1

# Log file print statement
print(f"Beginning Data Retrieval")
print(f"-------------------------------")

#Loop through the cities in the city list 
for city in cities:  
    
    # Try statement to append calls where value is found 
    # Not all calls return data as OpenWeatherMap will not have have records in all the cities generated by CityPy module
    try: 
        response = requests.get(f"{url}&q={city}").json() 
        city_name.append(response["name"])
        cloudiness.append(response["clouds"]["all"])
        country.append(response["sys"]["country"])
        date.append(response["dt"])
        humidity.append(response["main"]["humidity"])
        max_temp.append(response["main"]["temp_max"])
        lat.append(response["coord"]["lat"])
        lng.append(response["coord"]["lon"])
        wind_speed.append(response["wind"]["speed"])
        city_record = response["name"]
        print(f"Processing Record {record} | {city_record}")
        print(f"{url}&q={city}")
        
        # Increase counter by one 
        record= record + 1
        
        # Wait a second in loop to not over exceed rate limit of API
        time.sleep(1.01)
        
    # If no record found "skip" to next call
    except:
        print("City not found. Skipping...")
    continue


# In[19]:


# Create a dictonary with the lists generated
weatherpy_dict = {
    "City": city_name,
    "Cloudiness":cloudiness, 
    "Country":country,
    "Date":date, 
    "Humidity": humidity,
    "Lat":lat, 
    "Lng":lng, 
    "Max Temp": max_temp,
    "Wind Speed":wind_speed
}

# Create a data frame from dictionary
weather_data = pd.DataFrame(weatherpy_dict)

# Display count of weather data values 
weather_data.count()


# In[27]:


# Save data frame to CSV
weather_data.to_csv('/Users/rogeralbarran/Desktop/BOOTCAMP/02-Homework/06-Python-APIs/Weather Python.csv')

# Display data frame head 
weather_data.head()


# In[33]:


# Scatter plot for City Latitude vs Max Temperature
plt.scatter(weather_data["Lat"], weather_data["Max Temp"], marker="o", s=10)

# Incorporate the other graph properties
plt.title("City Latitude vs. Max Temperature")
plt.ylabel("Max. Temperature (F)")
plt.xlabel("Latitude")
plt.grid(True)

# Show plot
plt.show()


# In[32]:


# Scatter plot for City Latitude vs Humidity
plt.scatter(weather_data["Lat"], weather_data["Humidity"], marker="o", s=10)

# Incorporate the other graph properties
plt.title("City Latitude vs. Humidity")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(True)

# Show plot
plt.show()


# In[34]:


# Scatter plot for City Latitude vs Cloudiness
plt.scatter(weather_data["Lat"], weather_data["Cloudiness"], marker="o", s=10)

# Incorporate the other graph properties
plt.title("City Latitude vs. Cloudiness")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(True)

# Show plot
plt.show()


# In[37]:


# Scatter plot for City Latitude vs Wind Speed
plt.scatter(weather_data["Lat"], weather_data["Wind Speed"], marker="o", s=10)

# Incorporate the other graph properties
plt.title("City Latitude vs. Wind Speed")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(True)

# Show plot
plt.show()


# In[ ]:


#Observations
1) The temp and latitude scatter plot show that temperature does increase as it nears the equator
2) The humidity and cloudiness scatter plots show no linear relationship.
3)Wind speed scatter plot demonstrated averages of about 10 miles per hour. It was interesting to the outlier that the data pulled. 

