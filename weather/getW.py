import json
import datetime

with open("weather.txt") as f:
    data = json.load(f)
    # print(data)

# print(data['plaatsnaam'][0]["plaats"])

# time = datetime.datetime.now()
time2 = data["data"][0]["tijd_nl"]
timeW = datetime.datetime.strptime(time2, "%d-%m-%Y %H:%M")

# print(time)
# print(time2)
# print(timeW)


def preweather(start):
    dif = start - timeW.hour
    s1 = {}
    Temperature = []
    Date = []
    WindSpeed = []
    Precipitations = []
    for i in range(dif):
        Temperature.append(data["data"][i]["temp"]), Date.append(data["data"][i]["tijd_nl"])
        # To transform the date into daytime form use datetime.datetime.strptime(Date[x], "%d-%m-%Y %H:%M")
        WindSpeed.append(data["data"][i]["windkmh"]), Precipitations.append(data["data"][i]["neersl"])

    s1.update({"Date": Date})
    s1.update({"Temperature": Temperature})
    s1.update({"Wind Speed": WindSpeed})
    s1.update({"Precipitations": Precipitations})
    y = json.dumps(s1)
    return y


def postweather(end):
    dif2 = end - timeW.hour
    s2 = {}
    Temperature = []
    Date = []
    WindSpeed = []
    Precipitations = []
    for j in range(dif2, dif2 + 2):
        Temperature.append(data["data"][j]["temp"]), Date.append(data["data"][j]["tijd_nl"])
        # To transform the date into daytime form use datetime.datetime.strptime(Date[x], "%d-%m-%Y %H:%M")
        WindSpeed.append(data["data"][j]["windkmh"]), Precipitations.append(data["data"][j]["neersl"])

    s2.update({"Date": Date})
    s2.update({"Temperature": Temperature})
    s2.update({"Wind Speed": WindSpeed})
    s2.update({"Precipitations": Precipitations})
    y = json.dumps(s2)

    return y


# print(preweather(16))
# print(postweather(20))
