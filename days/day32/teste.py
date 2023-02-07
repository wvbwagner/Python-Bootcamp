import pandas

data = pandas.read_csv('birthdays.csv')

name = 'Wagner'

libdic = {row.name: row for (index, row) in data.iterrows()}

if name in libdic:
    bday = libdic[name]
    print(bday['day'], bday['month'])