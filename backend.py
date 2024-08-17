import requests
from datetime import datetime


def get_data(days, place, option):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid=c36dc31faacc8defd30107f5ecb14ec4"
    data = requests.request(url=url, method="GET")
    filtered_1 = data.json()["list"]
    x = 8*days
    info_list = []
    date_list = []
    if option == "Temperature":
        for num in range(0,x):
            date = filtered_1[num]["dt_txt"]
            date_list.append(date)
            info_list.append(filtered_1[num]["main"]["temp"]/10)
    elif option == "Sky":
        for num in range(0,x):
            info_list.append(filtered_1[num]["weather"][0]["main"])
            date = filtered_1[num]["dt_txt"]
            date_list.append(date)

    return date_list, info_list
