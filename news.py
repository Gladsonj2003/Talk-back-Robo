import requests

api_address="https://newsapi.org/v2/everything?q=keyword&apiKey=95f5c72ddc914a17a4c6b65137fe9622"

json_data=requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1)+", "+json_data["articles"][i]["title"]+".")
    return ar

arr=news()