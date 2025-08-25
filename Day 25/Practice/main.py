# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)


import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250824.csv")

grey_squirrel_count = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

count_data = pd.DataFrame(data_dict)

count_data.to_csv("squirrel_count.csv")