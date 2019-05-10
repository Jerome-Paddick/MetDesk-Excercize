from datetime import datetime
import matplotlib.pyplot as plt


class Temperature:
    def __init__(self, data):
        self.data = data
        self.temperature_list = [item["surface_temp"] for item in data]

    def min(self):
        return min(self.temperature_list)

    def max(self):
        return max(self.temperature_list)

    def range(self):
        return round(self.max() - self.min(), 1)

    def mean(self):
        return round(sum(self.temperature_list)/len(self.temperature_list),1)

    def median(self):
        sorted_list = sorted(self.temperature_list)
        half = len(self.temperature_list)//2
        mid_low = sorted_list[half]
        mid_high = sorted_list[-half-1]
        return (mid_low+mid_high)/2

    def warmest_weekday(self, weekday=0):
        """ :param weekday: -> integer corresponding to weekday where monday = 0 and sunday = 7 """
        warmest_temp = max([item["surface_temp"] for item in self.data if item["date"].weekday() == weekday])
        return [item for item in self.data if item["surface_temp"] == warmest_temp]

    def line_plot(self):
        date_list = [item["date"] for item in self.data]
        plt.plot_date(date_list, self.temperature_list, '-o')
        plt.title("Surface Temperature UK")
        plt.ylabel("Temperature °C")
        plt.xlabel("Dates")
        plt.xticks(rotation=45)
        plt.show()


def read_data(start_date=0, end_date=0):
    with open("data/metdesk data.csv") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            try:
                line_split = line.split(",")
                date = datetime.strptime(line_split[1], '"%Y-%m-%d %H:%M:%S"')
                surface_temp = float(line_split[3])
                if -50 < surface_temp < 50 and (start_date < date if start_date else True) and\
                                               (date < end_date if end_date else True):
                    data.append({"date": date,"surface_temp": surface_temp})
            except (ValueError, IndexError, TypeError):
                pass
        return sorted(data, key=lambda k: k['date'])


T = Temperature(data=read_data())

# print("min", T.min())
# print("max", T.max())
# print("range", T.range())
# print("mean", T.mean())
# print("median", T.median())
# print("warmest", T.warmest_weekday(0))
# T.line_plot()
