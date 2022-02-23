# Forecast file
import pandas

data = pandas.read_csv("weather_data.csv")

# Converting CSV to dictionary -> DataFrame
data_dict = data.to_dict()

# Get temperature column, change it to list and working with it -> Series
temp_list = data["temp"].to_list()

d_mean = data["temp"].mean()
d_max = data["temp"].max()

# Get Data in Columns
data["condition"]
data.condition

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# Squirrel data challenge
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"]

cinnamon_coloured = len(data[data["Primary Fur Color"] == "Gray"])
black_coloured = len(data[data["Primary Fur Color"] == "Black"])
gray_coloured = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_table = {
    "FurColor": ["Cinnamon", "Black", "Gray"],
    "Count": [cinnamon_coloured, black_coloured, gray_coloured]
}
pandas.DataFrame(squirrel_table).to_csv("squirrel_count.csv")
