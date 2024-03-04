import requests


url = ("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,"
       "wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

r = requests.get(url)
print(r.text)
data = r.json()
print(data["current_units"]['time'])
print(data["current"]['time'])

o = requests.get("https://media.licdn.com/dms/image/D4E03AQEvK4-dEjsvJQ/profile-displayphoto-shrink_800_800/0"
                 "/1705611282331?e=1715212800&v=beta&t=lx9_8SuwcsDVhYUor33bML6GI5PMAVJKJ1MGpW6DD-8")

with open("orisha.png", mode='wb') as ori:
    ori.write(o.content)
