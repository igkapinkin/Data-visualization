import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = "Loading data/data/sitka_weather_2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    heafer_row = next(reader)

    # for index, column_header in enumerate(heafer_row):
    #     print(index, column_header)

    # Получение дат, температурных минимумов и максимумов из файла
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Нанесение данных на диаграмму
    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Форматирование  диаграммы
    plt.title("Daily high and lows  temperatures - 2021", fontsize=20)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()