import requests

api_address='http://api.openweathermap.org/data/2.5/weather?q=Tirunelveli&appid=c8dc3a2303c12e782847f3f1f4665aba'
json_data=requests.get(api_address).json()

def temp():
    temprature=round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description=json_data["weather"][0]["description"]
    return description