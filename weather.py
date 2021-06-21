import requests
import datetime

location = "delhi"#str(input("Enter the city name:"))

api_key = "87d845b0b6cf29baa1a73cc34b067a95"
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")
print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity      :",hmdt, '%')
print("Current wind speed    :",wind_spd ,'kmph')

logfile = open("weather_log.txt","a")
logfile.write("-------------------------------------------------------------\n")
logfile.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
logfile.write("-------------------------------------------------------------\n")

logfile.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
logfile.write("Current weather desc  :{} \n".format(weather_desc))
logfile.write("Current Humidity      :{} %\n".format(hmdt))
logfile.write("Current wind speed    :{} kmph \n".format(wind_spd))
logfile.close()

