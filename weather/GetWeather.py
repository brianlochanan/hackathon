import json
import datetime


class GetWeather:
    with open("weather.txt") as f:
        data = json.load(f)
    time2 = data["data"][0]["tijd_nl"]
    timeW = datetime.datetime.strptime(time2, "%d-%m-%Y %H:%M")

    def __init__(self):
        pass

    # print(data)

    # print(data['plaatsnaam'][0]["plaats"])

    # time = datetime.datetime.now()

    # print(time)
    # print(time2)
    # print(timeW)

    def preweather(self, start):
        dif = start - self.timeW.hour
        s1 = {}
        Temperature = []
        Date = []
        WindSpeed = []
        Precipitations = []
        for i in range(dif):
            Temperature.append(self.data["data"][i]["temp"]), Date.append(self.data["data"][i]["tijd_nl"])
            # To transform the date into daytime form use datetime.datetime.strptime(Date[x], "%d-%m-%Y %H:%M")
            WindSpeed.append(self.data["data"][i]["windkmh"]), Precipitations.append(self.data["data"][i]["neersl"])

        s1.update({"Date": Date})
        s1.update({"Temperature": Temperature})
        s1.update({"Wind Speed": WindSpeed})
        s1.update({"Precipitations": Precipitations})
        return s1


    def postweather(self, end):
        dif2 = end - self.timeW.hour
        s2 = {}
        Temperature = []
        Date = []
        WindSpeed = []
        Precipitations = []
        for j in range(dif2, dif2 + 2):
            Temperature.append(self.data["data"][j]["temp"]), Date.append(self.data["data"][j]["tijd_nl"])
            # To transform the date into daytime form use datetime.datetime.strptime(Date[x], "%d-%m-%Y %H:%M")
            WindSpeed.append(self.data["data"][j]["windkmh"]), Precipitations.append(self.data["data"][j]["neersl"])

        s2.update({"Date": Date})
        s2.update({"Temperature": Temperature})
        s2.update({"Wind Speed": WindSpeed})
        s2.update({"Precipitations": Precipitations})
        y = json.dumps(s2)

        return y


    # print(preweather(16))
    # print(postweather(20))
