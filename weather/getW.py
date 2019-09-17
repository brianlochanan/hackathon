import json
import datetime

with open("weather.txt") as f:
    data = json.load(f)
    print(data)

print(data['plaatsnaam'][0]["plaats"])

time = datetime.datetime.now()
time2 = data["data"][0]["tijd_nl"]
timeW = datetime.datetime.strptime(time2, "%d-%m-%Y %H:%M")
print(time)
print(time2)
print(timeW)


def preweather(start):
    dif = start - timeW.hour
    s1 = []
    for i in range(dif):
        s1.append([data["data"][i]["tijd_nl"], data["data"][i]["temp"],
                   data["data"][i]["windkmh"], data["data"][i]["neersl"]])

    return s1


def postweather(end):
    dif2 = end - timeW.hour
    s2 = []
    for j in range(dif2 + 1, dif2 + 3):
        s2.append([data["data"][j]["tijd_nl"], data["data"][j]["temp"],
                   data["data"][j]["windkmh"], data["data"][j]["neersl"]])

    return s2

