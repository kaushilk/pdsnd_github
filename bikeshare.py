import time
import pandas as pd
import numpy as np

print("Lets take a look at some bikeshare data!")

cities = { 'c': './chicago.csv',
           'n': './new_york_city.csv',
           'w': './washington.csv' }
months = range(1,13)


def prompt_data():
    prompts = []
    city = input("Which city would you like to see data from? (c)Chicago, (n)New York or (w)Washington? \n")
    while city not in cities.keys():
        city = input("please enter a valid response:(c)Chicago, (n)New York or (w)Washington \n")

    month = int(input("Which month would you like to see data from? Please use numeric value \n"))
    while month not in months:
        month = int(input("please enter a valid number \n"))
    prompts.append(city)
    prompts.append(month)
    raw_data = input("would you like to see raw data? (y) or (n) \n")
    while raw_data not in ["n", "y"]:
        raw_data = input("please answer (y) or (n)")
    if raw_data == "y":
        num_raw_rows = input("how many rows? \n")
        prompts.append(num_raw_rows)
    else:
        prompts.append(0)
    return prompts

prompts = prompt_data()
cit = prompts[0]

city_data = pd.read_csv(cities[cit])
city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
city_data['month'] = city_data['Start Time'].dt.month
city_month_data = city_data['month'] == prompts[1]
num_data = prompts[2]
final_data = city_data[city_month_data]

# print raw data with correct city and month
if prompts[2] == 0:
    print("No raw data requested")
else:
    print("\n \n --Final Data-- \n")
    print(final_data.head(int(num_data)))

#mean Trip Duration
print("\n Average trip time: {}".format(final_data["Trip Duration"].mean()))
# most common gender
print("\n Most common gender: {}".format(final_data["Gender"].mode()))
# most common start station
print("\n Most common start station: {}".format(final_data["Start Station"].mode()))
# most common end station
print("\n Most common end station: {}".format(final_data["End Station"].mode()))
