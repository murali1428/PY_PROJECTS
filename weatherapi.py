import requests
#from pprint import pprint
import time
def weather():

    api_key="62f758a4a8104eda9de74719252006"
    city="madurai"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response=requests.get(url)
    data=response.json()
    #pprint(data)

    weather_info={}
    weather_info.update({"temperature":response.json()['current']['temp_c']})
    weather_info.update({"pressure":response.json()['current']['pressure_in']})
    weather_info.update({"feelslike":response.json()['current']['feelslike_c']})
    weather_info.update({"speedkph":response.json()['current']['gust_kph']})
    print(weather_info)

while True:
    weather()
    time.sleep(5)


