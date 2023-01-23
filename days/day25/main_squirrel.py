
import pandas
'''import csv

with open('weather_data.csv') as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        if row[1].isdigit():
            temperatures.append(int(row[1]))
    print(temperatures)

data = pandas.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()

temps = data['temp'].to_list()

average_temp = (sum(temps)) / len(temps)
print(f'{average_temp:.2f}')

#or you may use methods in panda

average_temp = data['temp'].mean()
print(f'{average_temp:.2f}')

print(data['temp'].max())

#also the following method could be used

print(data.temp.max())

monday = data[data.day == "Monday"]
print(monday.temp * 1.8 + 32)'''


squirrels = pandas.read_csv('squirrels.csv')

count = squirrels['Primary Fur Color'].value_counts().tolist()

colors = squirrels['Primary Fur Color'].dropna().drop_duplicates().tolist()

new_data = {'Fur Color': colors, 'Count': count}

file = pandas.DataFrame(new_data)
file.to_csv('squirrel_count.csv')



